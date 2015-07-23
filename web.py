from kivy.core.window import Window
from kivy.properties import ListProperty, NumericProperty
from kivy.factory import Factory
from kivy.uix.widget import Widget
from helpers import solve


win_x = Window.size[0]
win_y = Window.size[1]
solve = solve.Solve()

class Web(Widget):

	char_x = NumericProperty(.1)
	char_y = NumericProperty(.1)
	points = ListProperty([500, 500])
	points2 = ListProperty([400, 400])
	prev_len = 0

	def draw_web(self):
		a = round(win_x * self.char_x, 2)
		b = round(win_y * self.char_y, 2)
		#print "a, b", a, b
		self.points = self.points + list([a, b])
		#print "self.points", self.points

		# make calculations with points
		solve.collect(self.points)
		print('len(solve.crosspoints)', len(solve.crosspoints))

		# draw them crosspoints, if there are new ones.
		if self.prev_len != len(solve.crosspoints):
			print('draw')
			for i in xrange(1, len(solve.crosspoints) - self.prev_len):
				print "len(crosspoints)", len(solve.crosspoints), "prev_len", self.prev_len
				print solve.crosspoints[-i][0], solve.crosspoints[-i][1]
				with self.canvas:
					Color(1,0.9,0)
					Ellipse(pos=(solve.crosspoints[-i][0], solve.crosspoints[-i][1]), size = (15, 15))
					# change boxes colors accordingly
					self.print_boxes(solve.crosspoints[-i][0], solve.crosspoints[-i][1])
				self.prev_len = len(solve.crosspoints)
				print "prev_len", self.prev_len
