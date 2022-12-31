from vitfov.containers.container import Container
from vitfov.containers.wavetable import Wavetable


class Voice(Container):

	def __init__(self, num=0, wavetable=None):
		
		self.num = num
		self.lookup = {
			"destination":[0.0, 5.0, 0.0],
			"detune_power":[-5.0, 5.0, 1.5],
			"detune_range":[0.0, 48.0, 2.0],
			"distortion_amount":[0.0, 1.0, 0.5],
			"distortion_phase":[0.0, 1.0, 0.5],
			"distortion_spread":[-0.5, 0.5, 0.0],
			"distortion_type":[0.0, 12, 0.0],
			"frame_spread":[-128, 128, 0.0],
			"level":[0.0, 1.0, 0.70710678119],
			"midi_track":[0.0, 1.0, 1.0, True],
			"on":[0.0, 1.0, 0.0, True],
			"pan":[-1.0, 1.0, 0.0],
			"phase":[0.0, 1.0, 0.5],
			"random_phase":[0.0, 1.0, 1.0],
			"smooth_interpolation":[0.0, 1.0, 0.0, True],
			"spectral_morph_amount":[0.0, 1.0, 0.5],
			"spectral_morph_phase":[0.0,1.0,0.5],
			"spectral_morph_spread":[-0.5, 0.5, 0.0],
			"spectral_morph_type":[0.0, 15, 0.0],
			"spectral_unison":[0.0, 1.0, 1.0],
			"stack_style":[0.0, 13, 0.0],
			"stereo_spread":[0.0, 1.0, 1.0],
			"transpose":[-48.0, 48.0, 0.0],
			"transpose_quantize":[0.0, 8191.0, 0.0],
			"tune":[-1.0, 1.0, 0.0],
			"unison_blend":[0.0, 1.0, 0.8],
			"unison_detune":[0.0, 10.0, 4.472135955],
			"unison_voices":[1.0, 16.0, 1.0],
			"view_2d":[0.0, 2.0, 1.0],
			"wave_frame":[0.0, 256, 0.0]
		}

		self.wavetable = Wavetable() if wavetable is None else wavetable
		super().__init__(lookup=self.lookup, prefix="osc_"+str(self.num)+"_")

	def receive_wavetable(self, wavetable):
		self.wavetable.receive(wavetable)

	def initialize(self):
		super().initialize()
		self.wavetable.initialize()

	def randomize(self):
		super().randomize()
		self.wavetable.randomize()


class Sample(Container):

	def __init__(self, name="", samples="", length=44100, sample_rate=44100):
		self.name = name
		self.samples = samples
		self.length = length
		self.sample_rate = sample_rate
		self.lookup = {
			"bounce": [0.0, 1.0, 0.0],
			"destination": [0.0, 5.0, 3.0],
			"keytrack": [0.0, 1.0, 0.0, True],
			"level": [0.0, 1.0, 0.70710678119],
			"loop": [0.0, 1.0, 1.0],
			"on": [0.0, 1.0, 0.0, True],
			"pan": [-1.0, 1.0, 0.0],
			"random_phase": [0.0, 1.0, 0.0],
			"transpose": [-48.0, 48.0, 0.0],
			"transpose_quantize": [0.0, 8191.0, 0.0],
			"tune": [-1.0, 1.0, 0.0]
		}
		super().__init__(lookup=self.lookup, prefix="sample_")

	def initialize(self):
		super().initialize()
		self.name = ""
		self.samples = ""
		self.length = 44100
		self.sample_rate = 44100

	def receive(self, params):
		self.name = params.pop("name", self.name)
		self.samples = params.pop("samples", self.samples)
		self.length = params.pop("length", self.length)
		self.sample_rate = params.pop("sample_rate", self.sample_rate)


	def translate(self):
		base = super().translate()
		return base | {
			"sample": {
				"name":self.name,
				"samples":self.samples,
				"length":self.length,
				"sample_rate":self.sample_rate
			}
		}

