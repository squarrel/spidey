from kivy.core.window import Window
from kivy.properties import ListProperty
import math
from helpers import solve


win_x = Window.size[0]
win_y = Window.size[1]
alive = True
LEVELS = [16, 25, 36, 49, 64]

class Base(object):

	current_level = LEVELS[2]
	boxes = {}
	slices = []
	intersections = {}
	divisions = int(math.sqrt(current_level))
	switch = None

	def __init__(self, **kwargs):
		super(Base, self).__init__(**kwargs)

	def initiate_level(self):
		# initiate levels (sort of), prepare boxes
		for i in xrange(1, self.current_level + 1):
			self.boxes[i] = False
		#print "boxes", self.boxes

		# setup slices
		for j in xrange(self.divisions):
			self.slices.append((100 / self.divisions) * j / 100.0)
			#print(j)
		self.slices.append(1.0)
		#print "divisions", self.divisions
		#print "slices", self.slices
