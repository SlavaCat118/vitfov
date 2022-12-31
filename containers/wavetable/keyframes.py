import random
import math

from vitfov.containers.lfo import Lfo
from vitfov.containers import Container

# BASE CLASS

class Keyframe(Container):

	def __init__(self, lookup=None):

		l = {"position":[0.0,256.0,0.0]}
		self.lookup = l if lookup is None else l | lookup
		super().__init__(self.lookup)

# SOURCES

class kfWaveSource(Keyframe):

	def __init__(self, wave_data=""):

		super().__init__()
		self.wave_data = wave_data

	def receive(self, params):
		super().receive(params)
		self.wave_data = params.pop("wave_data", self.wave_data)

	def translate(self):
		base = super().translate()
		return base | {
			"wave_data":self.wave_data
		}

class kfLineSource(Keyframe):

	def __init__(self, line=None):

		self.lookup = {
			"pull_power":[0.0,5.0,0.0]
		}
		super().__init__(self.lookup)
		self.line = Lfo() if line is None else line

	def randomize(self):
		super().randomize()
		self.line.randomize()

	def receive(self, params):
		super().receive(params)
		self.line.receive_lfo(params.pop("line"))

	def translate(self):
		base = super().translate()
		return base | {
			"line":self.line.translate()
		}

class kfAudioSource(Keyframe):

	def __init__(self):

		self.lookup = {
			"window_fade":[0.0,1.0,1.0],
			"window_size":[1.0,9999.9,2048.0],
			"start_position":[0.0,10000.0,0.0] # TO BE FIXED
		}
		super().__init__(self.lookup)

# MODIFIERS

class kfPhaseShift(Keyframe):

	def __init__(self):

		self.lookup = {
			"mix":[0.0,1.0,1.0],
			"phase":[0.0,2*math.pi,0.0]
		}
		super().__init__(self.lookup)

class kfWaveWindow(Keyframe):

	def __init__(self):

		self.lookup = {
			"left_position":[0.0,1.0,0.25],
			"right_position":[0.0,1.0,0.75]
		}
		super().__init__(self.lookup)
	
class kfFrequencyFilter(Keyframe):

	def __init__(self):

		self.lookup = {
			"cutoff":[0.0,10.0,4.0],
			"shape":[0.0,1.0,0.5]
		}
		super().__init__(self.lookup)
	
class kfSlewLimiter(Keyframe):

	def __init__(self):

		self.lookup = {
			"down_run_rise":[0.0,1.0,0.0],
			"up_run_rise":[0.0,1.0,0.0]
		}
		super().__init__(self.lookup)
	
class kfWaveFolder(Keyframe):

	def __init__(self):

		self.lookup = {
			"fold_boost":[1.0,32.0,1.0]
		}
		super().__init__(self.lookup)
	
class kfWaveWarp(Keyframe):

	def __init__(self):

		self.lookup = {
			"horizontal_power":[-20.0,20.0,0.0],
			"vertical_power":[-20,20,0.0]
		}
		super().__init__(self.lookup)
	