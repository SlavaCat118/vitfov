from vitfov.containers.container import Container

class Envelope(Container):

	def __init__(self, num = 0):

		self.num = num
		self.lookup = {
			"attack": [0.0, 2.37842, 0.1495],
			"attack_power": [-20.0, 20.0, 0.0],
			"decay": [0.0, 2.37842, 1.0],
			"decay_power": [-20.0, 20.0, -2.0],
			"delay": [0.0, 1.4142135624, 0.0],
			"hold": [0.0, 1.4142135624, 0.0],
			"release": [0.0, 2.37842, 0.5476],
			"release_power": [-20.0, 20.0, -2.0],
			"sustain": [0.0, 1.0, 1.0]
		}

		super().__init__(self.lookup, "env_" + str(self.num) + "_")

	def randomize(self, keys=None, exclude=["delay"]):
		super().randomize(keys, exclude)