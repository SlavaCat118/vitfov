import random

from vitfov import vitfov_const

from vitfov.containers.container import Container

class MatrixWires(Container):

	def __init__(self):
		self.lookup = {
			"amount": [-1.0, 1.0, 0.0, False],
			"bipolar": [0.0, 1.0, 0.0, True],
			"bypass": [0.0, 1.0, 0.0, True],
			"power": [-10.0, 10.0, 0.0, False],
			"stereo": [0.0, 1.0, 0.0, True]
		}
		self.prefix = "modulation_"
		self.params = {}

		self.initialize()

	def initialize(self):
		for i in range(0,64):
			for j in list(self.lookup.keys()):
				self.params[self._pname(i+1,j)] = self.init(j)

	def is_valid(self, wire, param, value=None):
		if value is None:
			value = self.get(wire, param)
		return value <= self.upper(param) and value >= self.lower(param)

	def get(self, wire, param):
		return self.params[self._pname(wire, param)]

	def set(self, wire, param, value):
		if self.is_valid(wire, param, value) is False:
			bounds = [self.lower(param), self.upper(param)]
			print("{'" + self._pname(wire,param) + "': " + str(value) + "} out of range " + str(bounds) + "; could lead to preset failure.")
		
		self.params[self._pname(wire,param)] = value

	def randomize(self, start=0, end=64, keys=None, exclude=["bypass"]):
		loopthrough = [i for i in self.lookup.keys() if i not in exclude] if keys is None else keys
		for i in range(start,end):
			for j in loopthrough:
				val = round(random.uniform(self.lower(j),self.upper(j)), vitfov_const.float_res)
				if self.lookup[j][3] is True:
					val = random.randrange(self.lower(j),self.upper(j)+1)

				self.params[self._pname(i+1,j)] = val

	def _pname(self, wire, param):
		return str(wire)+"_"+param