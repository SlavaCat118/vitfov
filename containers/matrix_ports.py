import json
import random

ports = ""

with open("vitfov/containers/ports.json","r") as f:
	ports = json.load(f)

destinations = ports["destinations"]
sources = ports["sources"]

dest_full = list()
sources_full = list()

for k, v in destinations.items():
	dest_full += v
for k, v in sources.items():
	sources_full += v

class MatrixPorts(object):

	def __init__(self): 
		self.ports = [{"source":"", "destination":""} for i in range(64)]

	def __str__(self):
		return str(self.ports)

	def initialize(self, start=0, end=64):
		for i in range(start, end):
			self.ports[i] = {"source":"", "destination":""}

	def randomize(self, start=0, end=64):
		for i in range(start,end):
			# Keeps a 'fair' randomization by picking a random section and then a random value
			# To add: source/destination restritions

			source_names = list(sources.keys())
			dest_names = list(destinations.keys())

			source_type = source_names[random.randrange(0,len(source_names))]
			dest_type = dest_names[random.randrange(0,len(dest_names))]

			self.ports[i]["source"] = sources[source_type][random.randrange(0,len(sources[source_type]))]
			self.ports[i]["destination"] = destinations[dest_type][random.randrange(0,len(destinations[dest_type]))]
			if "line_mapping" in self.ports[i]:
				self.ports[i]["line_mapping"].randomize()

	def translate(self):
		return self.ports

	def set(port, source, destination, line_mapping=None):
		self.ports[port]["source"] = source
		self.ports[port]["destination"] = destination
		if line_mapping is not None:
			self.ports[port]["line_mapping"] = line_mapping

	def get(port):
		return self.ports[port]

