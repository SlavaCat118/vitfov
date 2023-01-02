from vitfov import utility
from vitfov.containers.container import Container

class Effects(object):

	def __init__(self):
		self.chorus = Chorus()
		self.compressor = Compressor()
		self.delay = Delay()
		self.distortion = Distortion()
		self.eq = Eq()
		self.flanger = Flanger()
		self.phaser = Phaser()
		self.reverb = Reverb()
		self.filters = [Filter("1"), Filter("2")]
		self.filter_fx = FilterFx()
		self.effects = [
			self.chorus,
			self.compressor,
			self.delay,
			self.distortion,
			self.eq,
			self.flanger,
			self.phaser,
			self.reverb,
			self.filter_fx
		] + self.filters

	def __str__(self):
		string = ""
		for effect in self.effects:
			string += type(effect).__name__ + " : " + str(effect) + ("\n"*2)
		return string

	def initialize(self, keys=None, exclude=None):
		loopthrough = utility.get_loopthrough(keys, exclude, self.effects)
		for effect in loopthrough:
			effect.initialize()

	def randomize(self, keys=None, exclude=None):
		loopthrough = utility.get_loopthrough(keys, exclude, self.effects)
		for effect in loopthrough:
			effect.randomize()

	def translate(self):
		base = {}
		for i in self.effects:
			base |= i.translate()
		return base

class Chorus(Container):

	def __init__(self):
		self.lookup = {
			"cutoff": [8.0, 136.0, 60.0],
			"delay_1": [-10.0, -5.64386, -9.0],
			"delay_2": [-10.0, -5.64386, -7.0],
			"dry_wet": [0.0, 1.0, 0.5],
			"feedback": [-0.95, 0.95, 0.4],
			"frequency": [-6.0, 3.0, -3.0],
			"mod_depth": [0.0, 1.0, 0.5],
			"on": [0.0, 1.0, 0.0, True],
			"spread": [0.0, 1.0, 1.0],
			"sync": [0.0, 3.0, 1.0],
			"tempo": [0.0, 10.0, 4.0],
			"voices": [1.0, 4.0, 4.0],
		}
		super().__init__(self.lookup, "chorus_")

class Compressor(Container):

	def __init__(self):
		self.lookup = {
			"attack": [0.0, 1.0, 0.5],
			"band_gain": [-30.0, 30.0, 11.7],
			"band_lower_ratio": [-1.0, 1.0, 0.8],
			"band_lower_threshold": [-80.0, 0.0, -36.0],
			"band_upper_ratio": [0.0, 1.0, 0.857],
			"band_upper_threshold": [-80.0, 0.0, -25.0],
			"enabled_bands": [0.0, 3, 0.0],
			"high_gain": [-30.0, 30.0, 16.3],
			"high_lower_ratio": [-1.0, 1.0, 0.8],
			"high_lower_threshold": [-80.0, 0.0, -35.0],
			"high_upper_ratio": [0.0, 1.0, 1.0],
			"high_upper_threshold": [-80.0, 0.0, -30.0],
			"low_gain": [-30.0, 30.0, 16.3],
			"low_lower_ratio": [-1.0, 1.0, 0.8],
			"low_lower_threshold": [-80.0, 0.0, -35.0],
			"low_upper_ratio": [0.0, 1.0, 0.9],
			"low_upper_threshold": [-80.0, 0.0, -28.0],
			"mix": [0.0, 1.0, 1.0],
			"on": [0.0, 1.0, 0.0, True],
			"release": [0.0, 1.0, 0.5]
		}
		super().__init__(self.lookup, "compressor_")

class Delay(Container):

	def __init__(self):
		self.lookup = {
			"aux_frequency": [-2.0, 9.0, 2.0],
			"aux_sync": [0.0, 3.0, 1.0],
			"aux_tempo": [4.0, 12.0, 9.0],
			"dry_wet": [0.0, 1.0, 0.3334],
			"feedback": [-1.0, 1.0, 0.5],
			"filter_cutoff": [8.0, 136.0, 60.0],
			"filter_spread": [0.0, 1.0, 1.0],
			"frequency": [-2.0, 9.0, 2.0],
			"on": [0.0, 1.0, 0.0, True],
			"style": [0.0, 3.0, 0.0],
			"sync": [0.0, 3.0, 1.0],
			"tempo": [4.0, 12.0, 9.0]
		}
		super().__init__(self.lookup, "delay_")

class Distortion(Container):

	def __init__(self):
		self.distortion_types = ["soft_clip","hard_clip","linear_fold","sine_fold","bit_crush","down_sample"]
		self.lookup = {
			"drive": [-30, 30, 0.0],
			"filter_blend": [0.0, 2.0, 0.0],
			"filter_cutoff": [8.0, 136.0, 80.0],
			"filter_order": [0.0, 2.0, 0.0],
			"filter_resonance": [0.0, 1.0, 0.5],
			"mix": [0.0, 1.0, 1.0],
			"on": [0.0, 1.0, 0.0, True],
			"type": [0.0, 5.0, 0.0]
		}
		super().__init__(self.lookup, "distortion_")

class Filter(Container):

	def __init__(self, num="", lookup=None):
		self.num = num
		self.filter_types = {
			"analog": ["12db", "24db", "notch_blend", "notch_spread", "b_p_n"],
			"dirty": ["12db", "24db", "notch_blend", "notch_spread", "b_p_n"],
			"ladder": ["12db", "24db", "notch_blend", "notch_spread", "b_p_n"],
			"digital": ["12db", "24db", "notch_blend", "notch_spread", "b_p_n"],
			"diode": ["low_shelf", "low_cut"],
			"formant": ["aoie", "aiuo"],
			"comb": ["low_high_comb", "low_high_flange+", "low_high_flange-", "spread_comb", "spread_flange+", "spread_flange-"],
			"phaser": ["positive", "negative"]
		}
		self.filter_models = list(self.filter_types.keys()) # for convenience
		self.lookup = {
			"blend": [0.0, 2.0, 0.0],
			"blend_transpose": [0.0, 84.0, 42.0],
			"cutoff": [8.0, 136.0, 60.0, ],
			"drive": [0.0, 20.0, 0.0],
			"filter_input": [0.0, 25.0, 0.0],
			"formant_resonance": [0.3, 1.0, 0.85],
			"formant_spread": [-1.0, 1.0, 0.0],
			"formant_transpose": [-12.0, 12.0, 0.0],
			"formant_x": [0.0, 1.0, 0.5],
			"formant_y": [0.0, 1.0, 0.5],
			"keytrack": [-1.0, 1.0, 0.0],
			"mix": [0.0, 1.0, 1.0],
			"model": [0.0, 7.0, 0.0, True],
			"on": [0.0, 1.0, 0.0, True],
			"resonance": [0.0, 1.0, 0.5],
			"style": [0.0, 0.0, 0.0, True],
		} if lookup is None else lookup
		super().__init__(self.lookup, prefix="filter_"+num+"_")
	
	def set_model(self, model):
		# The upper model limit is relative to the number of filter styles in a model
		# So this set function is necessary to update that value each ".set()"
		if type(model) in [int, float]:
			self.params["model"] = model
			self.lookup["style"][1] = len(self.filter_types[self.filter_models[int(model)]]) - 1
		elif type(model) == str:
			self.params["model"] = self.filter_models.index(model)
			self.lookup["style"][1] = len(self.filter_types[int(model)]) - 1

		if self.is_valid("style") is False:
			self.params["style"] = self.upper("style")

	def set(self, param, value):
		# This makes working with filters consistent with the rest of the containers
		# Split into two methods to help with organization and separation 
		if param == "model":
			self.set_model(value)
		else:
			super().set(param, value)

class FilterFx(Filter):
	"""Because for SOME reason, fx filters DONT have FILTER INPUTS"""

	def __init__(self):
		self.lookup = {
			"blend": [0.0, 2.0, 0.0],
			"blend_transpose": [0.0, 84.0, 42.0],
			"cutoff": [8.0, 136.0, 60.0, ],
			"drive": [0.0, 20.0, 0.0],
			"formant_resonance": [0.3, 1.0, 0.85],
			"formant_spread": [-1.0, 1.0, 0.0],
			"formant_transpose": [-12.0, 12.0, 0.0],
			"formant_x": [0.0, 1.0, 0.5],
			"formant_y": [0.0, 1.0, 0.5],
			"keytrack": [-1.0, 1.0, 0.0],
			"mix": [0.0, 1.0, 1.0],
			"model": [0.0, 7.0, 0.0, True],
			"on": [0.0, 1.0, 0.0, True],
			"resonance": [0.0, 1.0, 0.5],
			"style": [0.0, 0.0, 0.0, True],
		}
		super().__init__("fx", lookup=self.lookup)

class Flanger(Container):

	def __init__(self):
		self.lookup = {
			"center": [8.0, 136.0, 64.0],
			"dry_wet": [0.0, 0.5, 0.5],
			"feedback": [-1.0, 1.0, 0.5],
			"frequency": [-5.0, 2.0, 2.0],
			"mod_depth": [0.0, 1.0, 0.5],
			"on": [0.0, 1.0, 0.0, True],
			"phase_offset": [0, 1.0, 0.33333333],
			"sync": [0.0, 3.0, 1.0],
			"tempo": [0.0, 10.0, 4.0]
		}
		super().__init__(self.lookup, "flanger_")

class Phaser(Container):

	def __init__(self):
		self.lookup = {
			"blend": [0.0, 2.0, 1.0],
			"center": [8.0, 136.0, 80.0],
			"dry_wet": [0.0, 1.0, 1.0],
			"feedback": [0.0, 1.0, 0.5],
			"frequency": [-5.0, 2.0, -3.0],
			"mod_depth": [0.0, 48.0, 24.0],
			"on": [0.0, 1.0, 0.0, True],
			"phase_offset":[0.0,1.0,0.333],
			"sync": [0.0, 3.0, 1.0],
			"tempo": [0.0, 10.0, 3.0]
		}
		super().__init__(self.lookup, "phaser_")

class Reverb(Container):

	def __init__(self):
		self.lookup = {
			"chorus_amount": [0.0, 1.0, 0.223607],
			"chorus_frequency": [-8.0, 3.0, -2.0],
			"decay_time": [-6.0, 6.0, 0.0],
			"delay": [0.0, 0.3, 0.0],
			"dry_wet": [0.0, 1.0, 0.25],
			"high_shelf_cutoff": [0.0, 128.0, 90.0],
			"high_shelf_gain": [-6.0, 0.0, -1.0],
			"low_shelf_cutoff": [0.0, 128.0, 0.0],
			"low_shelf_gain": [-6.0, 0.0, 0.0],
			"on":[0.0,1.0,0.0, True],
			"pre_high_cutoff": [0.0, 128.0, 110.0],
			"pre_low_cutoff": [0.0, 128.0, 0.0],
			"size": [0.0, 1.0, 0.5]
		}
		super().__init__(self.lookup, "reverb_")

class Eq(Container):

	def __init__(self):
		self.lookup = {
			"band_cutoff": [8.0, 136.0, 80.0],
			"band_gain": [-15.0, 15.0, 0.0],
			"band_mode": [0.0, 1.0, 0.0, True],
			"band_resonance": [0.0, 1.0, 0.4473],
			"high_cutoff": [8.0, 136.0, 100.0],
			"high_gain": [-15.0, 15.0, 0.0],
			"high_mode": [0.0, 1.0, 0.0, True],
			"high_resonance":[0.0, 1.0, 0.3163],
			"low_cutoff": [8.0, 136.0, 40.0],
			"low_gain": [-15.0, 15.0, 0.0],
			"low_mode": [0.0, 1.0, 0.0, True],
			"low_resonance": [0.0, 1.0, 0.3163],
			"on": [0.0, 1.0, 0.0, True]
		}
		super().__init__(self.lookup, "eq_")