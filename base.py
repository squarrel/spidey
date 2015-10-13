from kivy.core.window import Window
from kivy.properties import ListProperty
import math
from helpers import solve


win_x = Window.size[0]
win_y = Window.size[1]
alive = True
LEVELS = [16, 25, 36, 49, 64]

class Base(object):

	current_level = LEVELS[0]
	boxes = {}
	slices = []
	intersections = {}
	divisions = int(math.sqrt(current_level))
	switch = None
	LEV_1 = [0, 0, 0, win_y/divisions, win_x, win_y/divisions, 
			win_x, (win_y/divisions)*2, 0, (win_y/divisions)*2, 0, (win_y/divisions)*3,
			win_x, (win_y/divisions)*3, win_x, win_y,	0, win_y,
			0, 0, win_x/divisions, 0, win_x/divisions, win_y,
			(win_x/divisions)*2, win_y, (win_x/divisions)*2, 0,
			(win_x/divisions)*3, 0, (win_x/divisions)*3, win_y,
			win_x, win_y, win_x, 0, 0, 0]
	LEV_2 = []
	message = ''

	def __init__(self, **kwargs):
		super(Base, self).__init__(**kwargs)

	def initiate_level(self):
		# initiate levels, prepare boxes
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
		
	def clear_level(self):
		self.boxes = {}
		self.slices = []
		self.intersections = {}
