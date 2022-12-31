from vitfov import vitfov_const

from vitfov.containers import wavetable

from vitfov.containers.container import Container
from vitfov.containers.wavetable import components
from vitfov.containers.wavetable import keyframes

type_match = {
	"Wave Source":components.WaveSource().__class__,
	"Line Source":components.LineSource().__class__,
	"Audio File Source":components.AudioSource().__class__,
	"Phase Shift":components.PhaseShift().__class__,
	"Frequency Filter":components.FrequencyFilter().__class__,
	"Wave Window":components.WaveWindow().__class__,
	"Slew Limiter":components.SlewLimiter().__class__,
	"Wave Folder":components.WaveFolder().__class__,
	"Wave Warp":components.WaveWarp().__class__
}

class Wavetable(object):

	def __init__(self, author="", full_normalize=True, groups=None,
				name="Init", remove_all_dc=True, version=vitfov_const.version):

		self.author = author
		self.full_normalize = full_normalize
		self.groups = list() if groups is None else groups
		self.name = name
		self.remove_all_dc = remove_all_dc
		self.version = version

		# source = wavetable.LineSource()
		# frame = source.add_keyframe(1)[0]
		# frame.line.set_points(wavetable.LINE_SAW)
		# self.build_group(source)

	def add_groups(self, *groups):
		self.groups += list(groups)

	def build_group(self, source, *modifiers):
		self.add_groups(Group([source, *modifiers]))

	def initialize(self):
		for i in self.groups:
			i.initialize()

	def randomize(self):
		for i in self.groups:
			i.randomize()

	def receive(self, wavetable):
		self.author = wavetable.pop("author", self.author)
		self.full_normalize = wavetable.pop("full_normalize", self.full_normalize)
		self.name = wavetable.pop("name", self.name)
		self.remove_all_dc = wavetable.pop("remove_all_dc", self.remove_all_dc)
		self.version = wavetable.pop("version", self.version)

		# Destructively build a new groups object
		groups = []
		for i in wavetable.pop("groups"):
			group = Group()
			group.receive(i)
			groups.append(group)

		self.groups = groups


	def translate(self):
		return {
			"author":self.author,
			"full_normalize":self.full_normalize,
			"groups":[i.translate() for i in self.groups],
			"name":self.name,
			"remove_all_dc":self.remove_all_dc,
			"version":self.version
		}

class Group(object):

	def __init__(self, components=None):
		self.components = list() if components is None else components

	def add_components(self, *components):
		self.components += list(components)

	def randomize(self):
		for i in self.components:
			i.randomize()

	def initialize(self):
		for i in self.components:
			i.initialize()

	def receive(self, group):
		# Destructively make new components

		components = []
		for i in group.pop("components"):
			component = type_match[i["type"]]()
			component.receive(i)
			components.append(component)
		self.components = components

	def translate(self):
		return {"components":[i.translate() for i in self.components]}