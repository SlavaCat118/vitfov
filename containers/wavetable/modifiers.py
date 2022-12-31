# import random

# import vitfov

# from vitfov import containers
# from vitfov.containers.wavetable import Component

# class PhaseShift(Component):

# 	def __init__(self, keyframes=None):

# 		self.lookup = {
# 			"style":[0.0,5.0,0.0]
# 		}
# 		super().__init__(type="Phase Shift", lookup=self.lookup, 
# 						keyframes=keyframes, 
# 						keyframe_class=vitfov.containers.wavetable.kfPhaseShift())

# class WaveWindow(Component):

# 	def __init__(self, keyframes=None):

# 		self.lookup = {
# 			"window_shape":[0.0,5.0,0.0]
# 		}
# 		super().__init__(type="Wave Window", lookup=self.lookup, 
# 						keyframes=keyframes, 
# 						keyframe_class=vitfov.containers.wavetable.kfWaveWindow())
	
# class FrequencyFilter(Component):

# 	def __init__(self, keyframes=None, normalize=False):

# 		self.lookup = {
# 			"style":[0.0,4.0,0.0]
# 		}
# 		self.normalize = normalize
# 		super().__init__(type="Frequency Filter", lookup=self.lookup, 
# 						keyframes=keyframes, 
# 						keyframe_class=vitfov.containers.wavetable.kfFrequencyFilter())

# 	def initialize(self):
# 		super().initialize()
# 		self.normalize = False

# 	def randomize(self):
# 		super().randomize()
# 		self.normalize = True if random.uniform(0.0,1.0) < 0.5 else False

# 	def receive(self, params):
# 		super().receive(params)
# 		self.normalize = params.pop("normalize")

# 	def translate(self):
# 		base = super().translate()
# 		return base | {
# 			"normalize":self.normalize
# 		}

# class SlewLimiter(Component):

# 	def __init__(self, keyframes=None):

# 		super().__init__(type="Slew Limiter", keyframes=keyframes, 
# 						keyframe_class=vitfov.containers.wavetable.kfSlewLimiter())
	
# class WaveFolder(Component):

# 	def __init__(self, keyframes=None):

# 		super().__init__(type="Wave Folder", keyframes=keyframes, 
# 						keyframe_class=vitfov.containers.wavetable.kfWaveFolder())
	
# class WaveWarp(Component):

# 	def __init__(self, keyframes=None, horizontal_asymmetric=False,
# 		vertical_asymmetric=False):

# 		self.horizontal_asymmetric = horizontal_asymmetric
# 		self.vertical_asymmetric = vertical_asymmetric
# 		super().__init__(type="Wave Warp", keyframes=keyframes, 
# 						keyframe_class=vitfov.containers.wavetable.kfWaveWarp())

# 	def initialize(self):
# 		super().initialize()
# 		self.horizontal_asymmetric = False
# 		self.vertical_asymmetric = False

# 	def randomize(self):
# 		super().randomize()
# 		self.horizontal_asymmetric = (
# 			True if random.uniform(0.0,1.0) < 0.5 else False)
# 		self.vertical_asymmetric = (
# 			True if random.uniform(0.0,1.0) < 0.5 else False)

# 	def receive(self, params):
# 		super().receive(params)
# 		self.horizontal_asymmetric = params.pop("horizontal_asymmetric")
# 		self.vertical_asymmetric = params.pop("vertical_asymmetric")

# 	def translate(self):
# 		base = super().translate()
# 		return base | {
# 			"horizontal_asymmetric":self.horizontal_asymmetric,
# 			"vertical_asymmetric":self.vertical_asymmetric
# 		}

# 	