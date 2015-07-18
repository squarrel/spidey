# Spidey Scientist
from kivy.app import App
print('imported kivy')
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window
from random import randint, choice
import math
from math import radians, pi, sin, cos
from helpers import solve, part_of
import kivent_core
import kivent_cymunk
from kivent_core.gameworld import GameWorld
from kivent_core.managers.resource_managers import texture_manager
from kivent_core.rendering.vertmesh import VertMesh
from kivent_core.systems.renderers import RotateRenderer
from kivent_core.systems.position_systems import PositionSystem2D
from kivent_core.systems.rotate_systems import RotateSystem2D
from kivy.properties import StringProperty, NumericProperty, ListProperty
from functools import partial

texture_manager.load_atlas('assets/background_objects.atlas')

ALIVE = True
LEVELS = [16, 36, 64]

class SpideyGame(Widget):

	current_level = LEVELS[0]
	win_x = Window.size[0]
	win_y = Window.size[1]
	char_x = NumericProperty(.1)
	char_y = NumericProperty(.1)
	char2_x = NumericProperty(.3)
	char2_y = NumericProperty(.3)
	ball_x = NumericProperty(.5)
	ball_y = NumericProperty(.5)
	change_x = .007
	change_y = .007

	go_right = False
	go_left = False
	go_up = False
	go_down = False

	boxes = {}
	slices = []
	intersections = {}
	crosspoints = []
	points = ListProperty([500, 500])
	points2 = ListProperty([400, 400])
	prev_len = 0
	divisions = int(math.sqrt(current_level))
	solve = solve.Solve()

	def __init__(self, **kwargs):
		super(SpideyGame, self).__init__(**kwargs)
		self.gameworld.init_gameworld(
			['cymunk_physics', 'rotate_renderer', 'rotate', 'position'],
			callback=self.init_game)

		'''# keyboard
		self._keyboard = Window.request_keyboard(self._keyboard_closed, self, 'text')
		if self._keyboard.widget:
			pass # what is this?
		self._keyboard.bind(on_key_down=self._on_keyboard_down)
		self._keyboard.bind(on_key_up=self._on_keyboard_up)'''

		# initiate levels (sort of), prepare boxes
		for i in xrange(1, self.current_level + 1):
			self.boxes[i] = False
		print "boxes", self.boxes

		# setup slices
		for j in xrange(self.divisions):
			self.slices.append((100 / self.divisions) * j / 100.0)
			#print(j)
		self.slices.append(1.0)
		#print "divisions", self.divisions
		print "slices", self.slices

		solve.win_x = self.win_x
		solve.win_y = self.win_y

	def init_game(self):
		state = 'menu'
		self.setup_states()
		self.set_state(state)
		self.draw_some_stuff()
		Clock.schedule_interval(self.update, 1.0 / 60.0)

	def destroy_created_entity(self, ent_id, dt):
		self.gameworld.remove_entity(ent_id)
		self.app.count -= 1

	def draw_some_stuff(self):
		size = Window.size
		w, h = size[0], size[1]
		delete_time = 2.5
		create_asteroid = self.create_asteroid
		destroy_ent = self.destroy_created_entity
		for x in range(100):
			pos = (randint(0, w), randint(0, h))
			ent_id = create_asteroid(pos)
			Clock.schedule_once(partial(destroy_ent, ent_id), delete_time)
		self.app.count += 100

	def create_asteroid(self, pos):
		x_vel = randint(-500, 500)
		y_vel = randint(-500, 500)
		angle = radians(randint(-360, 360))
		angular_velocity = radians(randint(-150, -150))
		shape_dict = {'inner_radius': 0, 'outer_radius': 20,
			'mass': 50, 'offset': (0, 0)}
		col_shape = {'shape_type': 'circle', 'elasticity': .5,
			'collision_type': 1, 'shape_info': shape_dict, 'friction': 1.0}
		col_shapes = [col_shape]
		physics_component = {'main_shape': 'circle',
			'velocity': (x_vel, y_vel),
			'position': pos, 'angle': angle,
			'angular_velocity': angular_velocity,
			'vel_limit': 250,
			'ang_vel_limit': angular_velocity,
			'vel_limit': 250,
			'ang_vel_limit': radians(200),
			'mass': 50, 'col_shapes': col_shapes}
		create_component_dict = {'cymunk_physics': physics_component,
			'rotate_renderer': {'texture': 'asteroid1',
			'size': (45, 45),
			'render': True},
			'position': pos, 'rotate': 0, }
		component_order = ['position', 'rotate', 'rotate_renderer',
			'cymunk_physics',]
		return self.gameworld.init_entity(
			create_component_dict, component_order)

	# The main update section
	def update(self, dt):
		'''
		# char and background texture movement
		if self.go_right:
			self.char_x += self.change_x
			self.t += .1
			#self.ani = 'pas_ani.zip'	
		elif self.go_left:
			self.char_x -= self.change_x
			self.t -= .1
			#self.ani = 'pas_ani.zip'
		elif self.go_up:
			self.char_y += self.change_y
			#self.ani = 'pas_ani.zip'	
		elif self.go_down:
			self.char_y -= self.change_y
			#self.ani = 'pas_ani.zip'	
		else: self.ani = 'data/pauk.jpg'	

		# collisions
		self.character_1.hit(self.ball)
		self.character_2.hit(self.character_1)

		# ai movement of char 2. not very smart
		self.char2_x += self.speed_char2
		if self.char2_x >= .6:
			self.speed_char2 = -.001
		if self.char2_x <= .2:
			self.speed_char2 = .001

		# ai movement of ball
		self.ball_x += self.speed_char3
		if self.ball_x >= .9:
			self.speed_char3 = -.004
		if self.ball_x <= .1:
			self.speed_char3 = .004'''

		self.gameworld.update(dt)

	def setup_states(self):
		self.gameworld.add_state(state_name='menu',
			systems_added=['rotate_renderer'],
			systems_removed=[], systems_paused=[],
			systems_unpaused=['rotate_renderer'],
			screenmanager_screen='menu')

		self.gameworld.add_state(state_name='main',
			systems_added=['rotate_renderer'],
			systems_removed=[], systems_paused=[],
			systems_unpaused=['rotate_renderer'],
			screenmanager_screen='main')

		self.gameworld.add_state(state_name='message',
			systems_added=['rotate_renderer'],
			systems_removed=[], systems_paused=[],
			systems_unpaused=['rotate_renderer'],
			screenmanager_screen='message')

	def set_state(self, *args):
		self.gameworld.state = args[0]

	# Keyboard rules
	def _keyboard_closed(self):
		print('My keyboard has been closed!')
		self._keyboard.unbind(on_key_down=self._on_keyboard_down)
		self._keyboard.unbind(on_key_up=self._on_keyboard_up)
		self._keyboard = None

	# capture the keyboard DOWN input and assign commands
	def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
		#print keycode
		if keycode[1] == 'right':
			self.go_right = True
			print "righttt"
		elif keycode[1] == 'left':
			self.go_left = True
		elif keycode[1] == 'up':
			self.go_up = True
		elif keycode[1] == 'down':
			self.go_down = True
		elif keycode[1] == 'spacebar':
			self.draw_web()
		elif keycode[1] == 'enter':
			if App.get_running_app().sm.current == 'menu':
				App.get_running_app().sm.current = 'game'
		elif keycode[1] == 'backspace':
			if App.get_running_app().sm.current == 'game':
				App.get_running_app().sm.current = 'menu'
		elif keycode[1] == 'escape':
			if App.get_running_app().sm.current == 'menu':
				exit()
			elif App.get_running_app().sm.current == 'game':
				App.get_running_app().sm.current = 'menu'
		return True

	# capture the keyboard UP input and assign commands
	def _on_keyboard_up(self, keyboard, keycode):
		if keycode[1] == 'right':
			self.go_right = False
		if keycode[1] == 'left':
			self.go_left = False
		if keycode[1] == 'up':
			self.go_up = False
		if keycode[1] == 'down':
			self.go_down = False
		return True
	
	# for touch-screens
	def on_touch_down(self, touch):
		if super(SpideyGame, self).on_touch_down(touch):
			return True
		touch.grab(self)
		#self.points = self.points + list([self.win_x * self.char_x, self.win_y * self.char_y]) 
		self.draw_web()
		print "touched"
		#return True

	def print_boxes(self, x, y):
		i = 1
		j = 1
		k = 1
		while i <= len(self.slices) - 1:
			while j <= len(self.slices) - 1:
				#print j - 1, j
				#print i - 1, i
				#print "slices[j]", self.slices[j]
				#print self.win_x * self.slices[j-1], self.win_x * self.slices[j], x
				#print self.win_y * self.slices[i-1], self.win_y * self.slices[i], y
				if self.win_x * self.slices[j-1] < x <= self.win_x * self.slices[j] \
				and self.win_y * self.slices[i-1] < y < self.win_y * self.slices[i] \
				and self.boxes[k] == False:
					#print "Box", i, j
					self.boxes[k] = True
					with self.canvas.after:
						color = Color(.7, .7, .7, .3)
						Rectangle(size=(self.win_x * self.slices[1], self.win_y * self.slices[1]),
							pos=(self.win_x * self.slices[j-1], self.win_y * self.slices[i-1]))
				j += 1
				k += 1

			j = 1
			i += 1

	# add points to the map
	def draw_web(self):
		a = round(self.win_x * self.char_x, 2)
		b = round(self.win_y * self.char_y, 2)
		#print "a, b", a, b
		self.points = self.points + list([a, b])
		#print "self.points", self.points

		# make calculations with points
		self.solve.collect(self.points)

		# draw them crosspoints, if there are new ones.
		if self.prev_len != len(self.solve.crosspoints):
			for i in xrange(1, len(self.solve.crosspoints) - self.prev_len):
				print "len(crosspoints)", len(self.solve.crosspoints), "prev_len", self.prev_len
				print self.solve.crosspoints[-i][0], self.solve.crosspoints[-i][1]
				with self.canvas:
					Color(1,0.9,0)
					Ellipse(pos=(self.solve.crosspoints[-i][0], self.solve.crosspoints[-i][1]), size = (15, 15))
					# change boxes colors accordingly
					self.print_boxes(self.solve.crosspoints[-i][0], self.solve.crosspoints[-i][1])
				self.prev_len = len(self.solve.crosspoints)
				print "prev_len", self.prev_len

class DebugPanel(Widget):
	fps = StringProperty(None)

	def __init__(self, **kwargs):
		super(DebugPanel, self).__init__(**kwargs)
		Clock.schedule_once(self.update_fps, .05)

	def update_fps(self, dt):
		self.fps = str(int(Clock.get_fps()))
		Clock.schedule_once(self.update_fps, .05)

class SpideyApp(App):
	count = NumericProperty(0)

if __name__ == '__main__':
	SpideyApp().run()
