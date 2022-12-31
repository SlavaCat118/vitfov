from vitfov.containers.container import Container

class RandomLfo(Container):

	def __init__(self, num=0):
		self.lookup = {
			"style":[0.0, 3, 0.0],
			"frequency":[-7.0, 9.0, 1.0],
			"sync":[0.0, 4, 1.0],
			"tempo":[0.0, 12.0, 8.0],
			"stereo":[0.0, 1.0, 0.0],
			"sync_type":[0.0, 1.0, 0.0],
			"keytrack_transpose":[-60.0, 36.0, -12.0],
			"keytrack_tune":[-1.0, 1.0, 0.0]
		}
		self.num = num

		super().__init__(lookup=self.lookup, prefix="random_"+str(self.num)+"_")


