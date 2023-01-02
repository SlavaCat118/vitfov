def get_loopthrough(keys=None, exclude=None, array=None):
	exclude = [] if exclude is None else exclude
	loopthrough = []
	if keys is None:
		loopthrough = [i for i in array if i not in exclude]
	else:
		loopthrough = keys
	return loopthrough