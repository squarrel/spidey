from kivy.core.window import Window
from kivy.factory import Factory


win_x = Window.size[0]
win_y = Window.size[1]

class Boxes(Widget):
	
	def print_boxes(self, x, y):
		i = 1
		j = 1
		k = 1
		while i <= len(self.slices) - 1:
			while j <= len(self.slices) - 1:
				#print j - 1, j
				#print i - 1, i
				#print "slices[j]", self.slices[j]
				#print win_x * self.slices[j-1], win_x * self.slices[j], x
				#print win_y * self.slices[i-1], win_y * self.slices[i], y
				if win_x * self.slices[j-1] < x <= win_x * self.slices[j] \
				and win_y * self.slices[i-1] < y < win_y * self.slices[i] \
				and self.boxes[k] == False:
					#print "Box", i, j
					self.boxes[k] = True
					with self.canvas.after:
						color = Color(.7, .7, .7, .3)
						Rectangle(size=(win_x * self.slices[1], win_y * self.slices[1]),
							pos=(win_x * self.slices[j-1], win_y * self.slices[i-1]))
				j += 1
				k += 1

			j = 1
			i += 1

Factory.register('Boxes', cls=Boxes)
