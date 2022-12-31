import random

import vitfov

from vitfov import vitfov_const
from vitfov import utility

class Container(object):
	""" A generalized contailer for Vital parameters with min, max, and init values """

	def __init__(self, lookup=None, prefix=""):
		self.prefix = prefix
		self.params = {}

		# value : [min, max, init, whole_step]
		self.lookup = dict() if lookup is None else lookup
		self.initialize()

	def __str__(self):
		return str(self.params)

	def initialize(self, keys=None, exclude=None):
		loopthrough = utility.get_loopthrough(keys, exclude, list(self.lookup.keys()))
		for key in loopthrough:
			self.params[key] = self.init(key)

	def randomize(self, keys=None, exclude=None):
		loopthrough = utility.get_loopthrough(keys, exclude, list(self.lookup.keys()))
		for param in loopthrough:
			value = round(random.uniform(self.lower(param), self.upper(param)), vitfov_const.float_res)
			if self.whole_step(param) is True:
				value = round(value)
			self.set(param, value)

	def set(self, param, value):
		if self.is_valid(param, value) is False and vitfov_const.warn_possible_problems:
			bounds = [self.lower(param), self.upper(param)]
			print("{'" + param + "': " + str(value) + "} out of range " + str(bounds) + "; could lead to preset failure.")
		
		self.params[param] = value

	def get(self, param):
		return self.params[param]

	def is_valid(self, param, value = None):
		if value is None:
			# makes it easier to check if a value is currently valid,
			# or if it will be valid at a given value
			value = self.get(param)

		return value >= self.lower(param) and value <= self.upper(param)

	# upper, lower, and init are for readability
	def lower(self, param):
		return self.lookup[param][0]

	def upper(self, param):
		return self.lookup[param][1]

	def init(self, param):
		return self.lookup[param][2]

	def whole_step(self, param):
		if len(self.lookup[param]) > 3:
			return self.lookup[param][3]
		else:
			return False

	def translate(self):
		newDict = {}
		for k, v in self.params.items():
			newDict[self.prefix + k] = v

		return newDict

	def receive(self, params):
		for k, v in self.params.items():
			self.set(k, params.pop(self.prefix+k, v))