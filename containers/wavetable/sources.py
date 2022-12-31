import random

import vitfov

from vitfov import containers
from vitfov.containers.wavetable import Component

# class WaveSource(Component):

# 	def __init__(self, keyframes=None):

# 		self.lookup = {
# 			"interpolation":[0.0,5.0,1.0]
# 		}
# 		self.keyframes = list() if keyframes is None else keyframes
# 		super().__init__(type="Wave Source", keyframes=self.keyframes,
# 						lookup=self.lookup, 
# 						keyframe_class=vitfov.containers.wavetable.kfWaveSource())

# class LineSource(Component):

# 	def __init__(self, keyframes=None):

# 		self.keyframes = list() if keyframes is None else keyframes
# 		super().__init__(type="Line Source", keyframes=self.keyframes, 
# 						keyframe_class=vitfov.containers.wavetable.kfLineSource())

# 	def translate(self):

# 		base = super().translate()
# 		return base | {
# 			"num_points":len(self.keyframes)
# 		}

# class AudioSource(Component):

# 	def __init__(self, keyframes=None):

# 		self.lookup = {
# 			"audio_sample_rate":[44100.0,44101.0,44100], # I have no idea
# 			"fade_style":[0.0,4.0,0.0],
# 			"phase_style":[0.0,3.0,0.0],
# 			"random_seed":[-9999999999.0,9999999999.0,0.0],
# 			"window_size":[1.0,9999.9,2048.0] # I have no idea
# 		}
# 		self.keyframes = list() if keyframes is None else keyframes
# 		self.audio_file = ""
# 		self.normalize_gain = False
# 		self.normalize_mult = False
# 		super().__init__(type="Audio File Source", keyframes=self.keyframes,
# 						lookup=self.lookup, 
# 						keyframe_class=vitfov.containers.wavetable.kfAudioSource())

# 	def receive(self, params):
# 		super().receive(params)
# 		self.audio_file = params.pop("audio_file")
# 		self.normalize_gain = params.pop("normalize_gain")
# 		self.normalize_mult = params.pop("normalize_mult")

# 	def translate(self):

# 		base = super().translate()
# 		return base | {
# 			"audio_file":self.audio_file,
# 			"normalize_gain":self.normalize_gain,
# 			"normalize_mult":self.normalize_mult
# 		}