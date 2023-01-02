import vitfov

from vitfov import utility
from vitfov import containers

import random

class Settings(object):

	def __init__(self, advanced=None, effects=None, envelopes=None,
				info=None, lfos=None, warps=None, matrix_ports=None,
				matrix_wires=None, randoms=None, voices=None,
				sample=None, random_seeds=None):
		self.advanced = containers.Advanced() if advanced is None else advanced
		self.effects = containers.Effects() if advanced is None else advanced
		self.envelopes = [containers.Envelope(i+1) for i in range(6)] if advanced is None else advanced
		self.lfos = [containers.Lfo(i+1) for i in range(8)] if advanced is None else advanced
		self.custom_warps = [containers.Lfo(i+1) for i in range(3)] if advanced is None else advanced
		self.matrix_ports = containers.MatrixPorts() if advanced is None else advanced
		self.matrix_wires = containers.MatrixWires() if advanced is None else advanced
		self.randoms = [containers.RandomLfo(i+1) for i in range(4)] if advanced is None else advanced
		self.voices = [containers.Voice(i+1) for i in range(3)] if advanced is None else advanced
		self.sample = containers.Sample() if advanced is None else advanced
		self.random_seeds = [{"seed":4} for i in range(3)] if random_seeds is None else random_seeds
		self.settings = [
			self.advanced,
			*self.envelopes,
			*self.lfos,
			*self.randoms,
			*self.voices,
			*self.effects.effects, # Get the actual effects
			self.sample,
			self.matrix_ports,
			self.matrix_wires,
			*self.custom_warps,
			*self.random_seeds
		]
	def randomize(self, keys=None, exclude=None):
		loopthrough = utility.get_loopthrough(keys, exclude, self.settings)
		for i in loopthrough:
			if type(i) == dict:
				i["seed"] = random.uniform(0,999.9)
			else:
				i.randomize()
				
	def initialize(self, keys=None, exclude=None):
		loopthrough = utility.get_loopthrough(keys, exclude, self.settings)
		for i in loopthrough:
			if type(i) == dict:
				i["seed"] = 5
			else:
				i.randomize()

		for i in range(3):
			self.voices[i].set("destination",i)

	def receive(self, params):
		params = params.pop("settings")

		# exclude randomSeeds and ports (non container components) 
		# and warps (technically a container, but confilcts with the LFOS)
		# and wires (also container, but has a different set function)

		for i in self.settings[:-8]: 
			# for key in i.params:
			# 	i.set(key, params.pop(i.prefix+key))
			i.receive(params)

		# Random Seeds handling
		seeds = params.pop("random_values", self.random_seeds)
		for n, i in enumerate(self.random_seeds):
			self.random_seeds[n]["seed"] = seeds[n]["seed"]

		# Ports handling
		ports = params.pop("modulations")
		self.matrix_ports.ports = ports

		# Wires handling
		for i in self.matrix_wires.params:
			self.matrix_wires.params[i] = params.pop(self.matrix_wires.prefix + i)

		# Warps handling
		warps = params.pop("custom_warps", [i.translate() for i in self.custom_warps])
		for n, i in enumerate(self.custom_warps):
			i.receive_lfo(warps[n])

		# Give the LFOs the lfo data (same as warps)
		lfos = params.pop("lfos")
		for n, i in enumerate(self.lfos):
			i.receive_lfo(lfos[n])

		# Give Voices wavetable data
		wavetables = params.pop("wavetables")
		for n, i in enumerate(self.voices):
			i.receive_wavetable(wavetables[n])

		# Give Sample sample data
		sample = params.pop("sample")
		self.sample.receive(sample)

		return params

	def translate(self):
		base = (self.advanced.translate() |
				self.matrix_wires.translate() |
				self.sample.translate() | 
				self.effects.translate())
		for i in self.envelopes:
			base |= i.translate()
		base["lfos"] = list()
		for i in self.lfos:
			lfo, params = i.translate(True, True)
			base |= params
			base["lfos"].append(lfo)
		base["custom_warps"] = list()
		for i in self.custom_warps:
			lfo = i.translate(True)
			base["custom_warps"].append(lfo)
		base["modulations"] = self.matrix_ports.translate()
		for i in self.randoms:
			base |= i.translate()
		base['wavetables'] = []
		for i in self.voices:
			base |= i.translate()
			base["wavetables"].append(i.wavetable.translate())
		base["random_values"] = self.random_seeds
		return base
