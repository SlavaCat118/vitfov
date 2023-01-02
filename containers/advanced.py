from vitfov.containers.container import Container

class Advanced(Container):

	def __init__(self):
		self.lookup = {
			"beats_per_minute":[0.333,999.9,2],
			"bypass":[0.0,1.0,0.0, True],
			"effect_chain_order":[0.0, 362879.0, 0.0],
			"legato":[0.0,1.0,0.0, True],
			"macro_control_1":[0.0,1.0,0.0],
			"macro_control_2":[0.0,1.0,0.0],
			"macro_control_3":[0.0,1.0,0.0],
			"macro_control_4":[0.0,1.0,0.0],
			"mod_wheel":[0.0,1.0,0.0],
			"mpe_enabled":[0.0, 1.0, 0.0, True],
			"oversampling":[0.0, 3.0, 1.0],
			"pitch_bend_range":[0.0,48.0,2.0],
			"pitch_wheel":[-1.0, 1.0, 0.0],
			"polyphony":[1.0, 32, 8.0],
			"portamento_force":[0.0, 1.0, 0.0, True],
			"portamento_scale":[0.0, 1.0, 0.0, True],
			"portamento_slope":[-8.0, 8.0, 0.0],
			"portamento_time":[-10.0, 4.0, -10.0],
			"stereo_mode":[0.0, 1.0, 0.0, True],
			"stereo_routing":[0.0, 1.0, 1.0],
			"velocity_track":[-1.0, 1.0, 0.0],
			"view_spectrogram":[0.0, 2.0, 0.0],
			"voice_amplitude":[0.0, 1.0, 1.0],
			"voice_override":[0.0, 1.0, 0.0],
			"voice_priority":[0.0, 4.0, 4.0],
			"voice_transpose":[-48.0, 48.0, 0.0],
			"voice_tune":[-1.0, 1.0, 0.0],
			"volume":[0.0, 7399.4404, 5473.0404]
		}
		super().__init__(self.lookup)

	def randomize(self, keys=None, exclude=["bypass","volume",
					"voice_amplitude", "stereo_routing"]):
		super().randomize(keys, exclude)