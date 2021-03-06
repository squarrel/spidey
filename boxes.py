from kivy.core.window import Window
from kivy.factory import Factory
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color, Line
from base import Base


win_x = Window.size[0]
win_y = Window.size[1]

class Boxes(Widget):

	def print_boxes(self, x, y):
		#print "boxes current_level, divisions", self.base.current_level, self.base.divisions
		#print "slices", self.base.slices
		#print "boxes", self.base.boxes
		i = 1
		j = 1
		k = 1
		while i <= len(self.base.slices) - 1:
			while j <= len(self.base.slices) - 1:
				#print j - 1, j
				#print i - 1, i
				#print "slices[j]", self.slices[j]
				#print win_x * self.slices[j-1], win_x * self.slices[j], x
				#print win_y * self.slices[i-1], win_y * self.slices[i], y
				if win_x * self.base.slices[j-1] < x <= win_x * self.base.slices[j] \
				and win_y * self.base.slices[i-1] < y < win_y * self.base.slices[i] \
				and self.base.boxes[k] == False: # could be imporoved here for speed
					#print "Box", i, j
					self.base.boxes[k] = True
					with self.canvas.after:
						color = Color(.7, .7, .7, .3)
						Rectangle(size=(win_x * self.base.slices[1], win_y * self.base.slices[1]),
							pos=(win_x * self.base.slices[j-1], win_y * self.base.slices[i-1]))
				j += 1
				k += 1

			j = 1
			i += 1

	def current_box(self, x, y):
		i = 1
		j = 1
		k = 1
		#print "base.slices", self.base.slices
		#print "base.boxes", self.base.boxes
		while i <= len(self.base.slices) - 1:
			#print "i", i
			while j <= len(self.base.slices) - 1:
				#print "j", j
				if win_x * self.base.slices[j-1] <= x <= win_x * self.base.slices[j] \
				and win_y * self.base.slices[i-1] <= y <= win_y * self.base.slices[i]:
					return k
				#else:
					#print "--->", win_y * self.base.slices[i-1], y, win_y * self.base.slices[i]
					#print("k", k)
					#return None
				j += 1
				k += 1

			j = 1
			i += 1

	def draw_background(self, lev):
		# clear canvas
		self.clear_background()

		#print "lev", lev
		with self.canvas.before:
			color = Color(.7, .7, .7, .3)
			Line(points=lev, width=3)

	def clear_background(self):
		self.canvas.before.clear()
		self.canvas.after.clear()


Factory.register('Boxes', cls=Boxes)
