from vitfov.containers.info import Info
from vitfov.containers.settings import Settings

class Preset(object):

	def __init__(self, info=None, settings=None):
		self.settings = Settings() if settings is None else settings
		self.info = Info() if info is None else info

	def receive(self, params):
		self.info.receive(params)
		self.settings.receive(params)
		return params

	def randomize(self):
		self.settings.randomize()

	def initialize(self):
		self.settings.initialize()

	def translate(self):
		return self.info.translate() | {"settings":self.settings.translate()}