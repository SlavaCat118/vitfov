import json, pprint

import vitfov

from vitfov import containers

def to_json(obj):
	return json.dumps(obj, indent = 4, sort_keys=True)

def from_json(text):
	return json.loads(text)

def to_vital(obj):
	toRet = None
	if isinstance(obj, containers.Effects) is True:
		toRet = effects_to_vital(obj)
	elif hasattr(obj, "translate") and callable(obj.translate):
		toRet = obj.translate()

	if toRet is not None:
		return to_json(toRet)
	else:
		raise ValueError("obj was not valid for translating, make sure it has a .translate() method")

def effects_to_vital(obj):
	params = {}
	for effect in obj.effects:
		params.update(effect.translate())
	return params

def from_vital(params): # Make better

	preset = containers.Preset()
	preset.receive(params)
	return preset