from kivy.core.window import Window
from kivy.properties import ListProperty, NumericProperty
from kivy.factory import Factory
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Ellipse, Color
from helpers import solve
from spider_system import SpiderSystem
from boxes import Boxes


win_x = Window.size[0]
win_y = Window.size[1]
solve = solve.Solve()

class Web(Widget):

	points = ListProperty([win_x * .5, win_y * .5])
	points2 = ListProperty([win_x * 4, win_y * .4])
	prev_len = 0

	def draw_web(self):
		a = round(win_x * self.spider_system.x, 2)
		b = round(win_y * self.spider_system.y, 2)
		#print "a, b", a, b
		self.points = self.points + list([a, b])
		#print "self.points", self.points

		# make calculations with points
		solve.collect(self.points)

		# draw them crosspoints, if there are new ones.
		if self.prev_len != len(solve.crosspoints):
			#print('len(crosspoints)', len(solve.crosspoints))
			#print('crosspoints', solve.crosspoints)
			#print('draw')
			for i in xrange(0, len(solve.crosspoints)): # <--- here bug
				#print('to draw')
				#print "len(crosspoints)", len(solve.crosspoints), "prev_len", self.prev_len
				#print solve.crosspoints[-i][0], solve.crosspoints[-i][1]
				with self.canvas:
					Color(1,0.9,0)
					Ellipse(pos=(solve.crosspoints[-i][0], solve.crosspoints[-i][1]), size = (15, 15))
					# change boxes colors accordingly
					self.boxes.print_boxes(solve.crosspoints[-i][0], solve.crosspoints[-i][1])
				self.prev_len = len(solve.crosspoints)
				#print "prev_len", self.prev_len
