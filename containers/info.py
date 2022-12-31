import vitfov

from vitfov import vitfov_const

class Info(object):

	def __init__(self, author="", comments="", 
				macro1="MACRO 1", macro2='MACRO 2', macro3="MACRO 3", 
				macro4="MACRO 4", preset_name="VITFOV_INIT", 
				preset_style=""):

		self.author = author
		self.comments = comments
		self.preset_style = preset_style
		self.preset_name = preset_name
		self.macro1 = macro1
		self.macro2 = macro2
		self.macro3 = macro3
		self.macro4 = macro4
		self.synth_version = vitfov_const.version

	def translate(self):
		return {
			"author":self.author,
			"comments":self.comments,
			"preset_style":self.preset_style,
			"preset_name":self.preset_name,
			"macro1":self.macro1,
			"macro2":self.macro2,
			"macro3":self.macro3,
			"macro4":self.macro4,
			"synth_version":self.synth_version
		}

	def receive(self, params):
		self.author = params.pop("author", self.author)
		self.comments = params.pop("comments", self.comments)
		self.preset_style = params.pop("preset_style", self.preset_style)
		self.preset_name = params.pop("preset_name", self.preset_name)
		self.macro1 = params.pop("macro1", self.macro1)
		self.macro2 = params.pop("macro2", self.macro2)
		self.macro3 = params.pop("macro3", self.macro3)
		self.macro4 = params.pop("macro4", self.macro4)
		self.synth_version = params.pop("synth_version", self.synth_version)

		return params