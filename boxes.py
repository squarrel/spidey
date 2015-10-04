from kivy.core.window import Window
from kivy.factory import Factory
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color, Line
from base import Base


win_x = Window.size[0]
win_y = Window.size[1]
base = Base()

class Boxes(Widget):

	def print_boxes(self, x, y):
		i = 1
		j = 1
		k = 1
		while i <= len(base.slices) - 1:
			while j <= len(base.slices) - 1:
				#print j - 1, j
				#print i - 1, i
				#print "slices[j]", self.slices[j]
				#print win_x * self.slices[j-1], win_x * self.slices[j], x
				#print win_y * self.slices[i-1], win_y * self.slices[i], y
				if win_x * base.slices[j-1] < x <= win_x * base.slices[j] \
				and win_y * base.slices[i-1] < y < win_y * base.slices[i] \
				and base.boxes[k] == False: # could be imporoved here for speed
					#print "Box", i, j
					base.boxes[k] = True
					with self.canvas.after:
						color = Color(.7, .7, .7, .3)
						Rectangle(size=(win_x * base.slices[1], win_y * base.slices[1]),
							pos=(win_x * base.slices[j-1], win_y * base.slices[i-1]))
				j += 1
				k += 1

			j = 1
			i += 1

	def current_box(self, x, y):
		i = 1
		j = 1
		k = 1
		#print "base.slices", base.slices
		while i <= len(base.slices) - 1:
			#print "i", i
			while j <= len(base.slices) - 1:
				#print "j", j
				if win_x * base.slices[j-1] <= x <= win_x * base.slices[j] \
				and win_y * base.slices[i-1] <= y <= win_y * base.slices[i]:
					return k
				#else:
					#print "--->", win_y * base.slices[i-1], y, win_y * base.slices[i]
					#print("k", k)
					#return None
				j += 1
				k += 1

			j = 1
			i += 1

	def draw_background(self, lev):
		# draw background
		div = base.divisions
		with self.canvas.before:
			color = Color(.7, .7, .7, .3)
			Line(points=lev, width=3)

Factory.register('Boxes', cls=Boxes)
