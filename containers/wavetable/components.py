import random

import vitfov

from vitfov.containers import wavetable
from vitfov.containers import Container

# BASE CLASS

class Component(Container):

	def __init__(self, type="", keyframes=None, lookup=None, keyframe_class=None):

		l = {"interpolation_style":[0.0,3.0,1.0]} 
		self.lookup = l if lookup is None else lookup | l
		self.keyframes = list() if keyframes is None else keyframes
		self.keyframe_class = Keyframe().__class__ if keyframe_class is None else keyframe_class.__class__
		self.type = type
		super().__init__(self.lookup)

	def add_keyframes(self, *keyframes):
		self.keyframes += list(keyframes)

	def add_keyframe(self, num=1):
		keyframes = [self.keyframe_class() for i in range(num)]
		self.add_keyframes(*keyframes)
		return keyframes

	def dist_frames(self):
		if len(self.keyframes) > 1:
			c = 256/(len(self.keyframes)-1)
			for n, i in enumerate(self.keyframes):
				i.set("position", n*c)

	def fix_frames(self):
		positions = sorted([i.position for i in self.keyframes])
		for n, i in enumerate(self.keyframes):
			i.position = positions[n]

	def randomize(self):
		super().randomize()
		for i in self.keyframes:
			i.randomize()

	def initialize(self):
		super().initialize()
		for i in self.keyframes:
			i.initialize()

	def receive(self, params):
		super().receive(params)
		self.type = params.pop("type")

		keyframes = []
		for i in params.pop("keyframes"):
			keyframe = self.keyframe_class()
			keyframe.receive(i)
			keyframes.append(keyframe)
		self.keyframes = keyframes

	def translate(self):
		base = super().translate()
		return base | {
			"keyframes":[i.translate() for i in self.keyframes],
			"type":self.type
			}

# SOURCES

class WaveSource(Component):

	def __init__(self, keyframes=None):

		self.lookup = {
			"interpolation":[0.0,5.0,1.0]
		}
		self.keyframes = list() if keyframes is None else keyframes
		super().__init__(type="Wave Source", keyframes=self.keyframes,
						lookup=self.lookup, 
						keyframe_class=wavetable.keyframes.kfWaveSource())

class LineSource(Component):

	def __init__(self, keyframes=None):

		self.keyframes = list() if keyframes is None else keyframes
		super().__init__(type="Line Source", keyframes=self.keyframes, 
						keyframe_class=wavetable.keyframes.kfLineSource())

	def translate(self):

		base = super().translate()
		return base | {
			"num_points":len(self.keyframes)
		}

class AudioSource(Component):

	def __init__(self, keyframes=None):

		self.lookup = {
			"audio_sample_rate":[44100.0,44101.0,44100], # I have no idea
			"fade_style":[0.0,4.0,0.0],
			"phase_style":[0.0,3.0,0.0],
			"random_seed":[-9999999999.0,9999999999.0,0.0],
			"window_size":[1.0,9999.9,2048.0] # I have no idea
		}
		self.keyframes = list() if keyframes is None else keyframes
		self.audio_file = ""
		self.normalize_gain = False
		self.normalize_mult = False
		super().__init__(type="Audio File Source", keyframes=self.keyframes,
						lookup=self.lookup, 
						keyframe_class=wavetable.keyframes.kfAudioSource())

	def receive(self, params):
		super().receive(params)
		self.audio_file = params.pop("audio_file")
		self.normalize_gain = params.pop("normalize_gain")
		self.normalize_mult = params.pop("normalize_mult")

	def translate(self):

		base = super().translate()
		return base | {
			"audio_file":self.audio_file,
			"normalize_gain":self.normalize_gain,
			"normalize_mult":self.normalize_mult
		}

# MODIFIERS

class PhaseShift(Component):

	def __init__(self, keyframes=None):

		self.lookup = {
			"style":[0.0,5.0,0.0]
		}
		super().__init__(type="Phase Shift", lookup=self.lookup, 
						keyframes=keyframes, 
						keyframe_class=wavetable.keyframes.kfPhaseShift())

class WaveWindow(Component):

	def __init__(self, keyframes=None):

		self.lookup = {
			"window_shape":[0.0,5.0,0.0]
		}
		super().__init__(type="Wave Window", lookup=self.lookup, 
						keyframes=keyframes, 
						keyframe_class=wavetable.keyframes.kfWaveWindow())
	
class FrequencyFilter(Component):

	def __init__(self, keyframes=None, normalize=False):

		self.lookup = {
			"style":[0.0,4.0,0.0]
		}
		self.normalize = normalize
		super().__init__(type="Frequency Filter", lookup=self.lookup, 
						keyframes=keyframes, 
						keyframe_class=wavetable.keyframes.kfFrequencyFilter())

	def initialize(self):
		super().initialize()
		self.normalize = False

	def randomize(self):
		super().randomize()
		self.normalize = True if random.uniform(0.0,1.0) < 0.5 else False

	def receive(self, params):
		super().receive(params)
		self.normalize = params.pop("normalize")

	def translate(self):
		base = super().translate()
		return base | {
			"normalize":self.normalize
		}

class SlewLimiter(Component):

	def __init__(self, keyframes=None):

		super().__init__(type="Slew Limiter", keyframes=keyframes, 
						keyframe_class=wavetable.keyframes.kfSlewLimiter())
	
class WaveFolder(Component):

	def __init__(self, keyframes=None):

		super().__init__(type="Wave Folder", keyframes=keyframes, 
						keyframe_class=wavetable.keyframes.kfWaveFolder())
	
class WaveWarp(Component):

	def __init__(self, keyframes=None, horizontal_asymmetric=False,
		vertical_asymmetric=False):

		self.horizontal_asymmetric = horizontal_asymmetric
		self.vertical_asymmetric = vertical_asymmetric
		super().__init__(type="Wave Warp", keyframes=keyframes, 
						keyframe_class=wavetable.keyframes.kfWaveWarp())

	def initialize(self):
		super().initialize()
		self.horizontal_asymmetric = False
		self.vertical_asymmetric = False

	def randomize(self):
		super().randomize()
		self.horizontal_asymmetric = (
			True if random.uniform(0.0,1.0) < 0.5 else False)
		self.vertical_asymmetric = (
			True if random.uniform(0.0,1.0) < 0.5 else False)

	def receive(self, params):
		super().receive(params)
		self.horizontal_asymmetric = params.pop("horizontal_asymmetric")
		self.vertical_asymmetric = params.pop("vertical_asymmetric")

	def translate(self):
		base = super().translate()
		return base | {
			"horizontal_asymmetric":self.horizontal_asymmetric,
			"vertical_asymmetric":self.vertical_asymmetric
		}
