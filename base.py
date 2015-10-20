from kivy.core.window import Window
from kivy.properties import ListProperty
import math
from helpers import solve


win_x = Window.size[0]
win_y = Window.size[1]

class Base(object):

	LEVELS = [16, 25, 36, 49, 64]
	current_level = LEVELS[0] # bug here?
	boxes = {}
	slices = []
	intersections = {}
	divisions = int(math.sqrt(current_level)) # hardcoded bug here
	switch = None
	transition = True
	LEV_1 = [
			0, 0, 0, win_y/4, win_x, win_y/4, 
			win_x, (win_y/4)*2, 0, (win_y/4)*2,
			0, (win_y/4)*3, win_x, (win_y/4)*3,
			win_x, win_y, 0, win_y,
			0, 0, win_x/4, 0, win_x/4, win_y,
			(win_x/4)*2, win_y, (win_x/4)*2, 0,
			(win_x/4)*3, 0, (win_x/4)*3, win_y,
			win_x, win_y, win_x, 0, 0, 0
			]
	LEV_2 = [
			0, 0, 0, win_y/5, win_x, win_y/5,
			win_x, (win_y/5)*2, 0, (win_y/5)*2,
			0, (win_y/5)*3, win_x, (win_y/5)*3,
			win_x, (win_y/5)*4, 0, (win_y/5)*4,
			0, win_y, win_x, win_y, 0, win_y,
			0, 0, win_x/5, 0, win_x/5, win_y,
			(win_x/5)*2, win_y, (win_x/5)*2, 0,
			(win_x/5)*3, 0, (win_x/5)*3, win_y,
			(win_x/5)*4, win_y, (win_x/5)*4, 0,
			win_x, 0, win_x, win_y, win_x, 0, 0, 0
			]
	LEV_3 = [
			0, 0, 0, win_y/6, win_x, win_y/6,
			win_x, win_y
			]
	LEVEL_MAP = [LEV_1, LEV_2, LEV_3]

	def __init__(self, **kwargs):
		super(Base, self).__init__(**kwargs)

	def initiate_level(self):
		# prepare boxes
		for i in xrange(1, self.current_level + 1):
			self.boxes[i] = False
		#print "boxes", self.boxes
		#print "divisions", self.divisions

		# prepare slices
		for j in xrange(self.divisions):
			self.slices.append((100 / self.divisions) * j / 100.0)
			#print(j)
		self.slices.append(1.0)
		#print "divisions", self.divisions
		#print "slices", self.slices

	def clear_level(self):
		self.boxes.clear()
		del self.slices[:]
		self.intersections.clear()
		self.divisions = int(math.sqrt(self.current_level))
		#print "--->", self.divisions
