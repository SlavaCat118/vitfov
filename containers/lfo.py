import random

from vitfov import vitfov_const
from vitfov.containers.container import Container

class Lfo(Container):

	def __init__(self, num=0, name = "none", points=None, powers=None, prefix="lfo_"):

		self.num = num
		self.points = [] if points is None else points # 0 -> 1
		self.powers = [] if powers is None else powers # -10 -> 10
		self.smooth = False
		self.name = name
		self.lookup = {
			"phase": [0.0, 1.0, 0.0],
			"frequency": [-7.0, 9.0, 1.0],
			"sync": [0.0, 6, 1.0],
			"sync_type": [0.0, 4, 0.0],
			"fade_time": [0.0, 8.0, 0.0],
			"tempo": [0.0, 12.0, 7.0],
			"delay_time": [0.0, 4.0, 0.0],
			"smooth_mode": [0.0, 1.0, 1.0],
			"smooth_time": [-10.0, 4.0, -7.5],
			"stereo": [-0.5, 0.5, 0.0],
			"keytrack_transpose": [-60.0, 36.0, -12.0],
			"keytrack_tune": [-1.0, 1.0, 0.0]
		}

		super().__init__(self.lookup, prefix + str(self.num) + "_")

	def __str__(self):
		return str(self.translate())

	def randomize(self, num_points=10, points=True, powers=False, params=True, fixed_point_x=False):
		if params is True:
			super().randomize()

		if points is True:
			if fixed_point_x is True:
				x_points = [round(i/num_points, vitfov_const.float_res) for i in range(num_points)] + [1]
			else:
				x_points = sorted([0.0] + [round(random.uniform(0.0,1.0), vitfov_const.float_res) for i in range(num_points-2)]+[1.0])
			y_points = [round(random.uniform(0.0,1.0), vitfov_const.float_res) for i in range(num_points)]
			y_points.append(y_points[0])
	

			points = list(zip(x_points, y_points))
			new = []
			for i in points:
				new += list(i)

			self.points = new

		powers = self.powers
		if powers is True:
			powers = [round(random.uniform(-10.0,10.0), vitfov_const.float_res) for i in range(num_points)]
		else:
			powers = [0 for i in range(len(self.points)//2)]
		self.powers = powers

	def initialize(self):
		super().initialize()

		self.points = [0.0,1.0,0.5,0.0,1.0,1.0]
		self.powers = [0.0,0.0,0.0]
		self.smooth = False
		self.name = "Triangle"

	def set_points(self, points, fix_powers=True):

		self.points = points
		if fix_powers is True:
			self.powers = [0]*(len(points)//2)

	def receive_lfo(self, lfo):
		self.points = lfo["points"]
		self.powers = lfo["powers"]
		self.smooth = lfo["smooth"]
		self.name = lfo["name"]

	def translate(self, get_lfo=True, get_params=False):
		lfo = {
			"name":self.name,
			"points":self.points,
			"powers":self.powers,
			"smooth":self.smooth,
			"num_points":len(self.powers)
		}
		params = super().translate()

		if get_lfo is True:
			if get_params is True:
				return [lfo, params]
			return lfo
		return params
