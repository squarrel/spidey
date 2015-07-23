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
from kivent_core.managers.resource_managers import (
	texture_manager, model_manager)
from kivent_core.rendering.vertmesh import VertMesh
from kivent_core.systems.renderers import RotateRenderer
from kivent_core.systems.position_systems import PositionSystem2D
from kivent_core.systems.rotate_systems import RotateSystem2D
from kivent_core.systems.gamesystem import GameSystem
from kivy.properties import StringProperty, NumericProperty, ListProperty
from functools import partial
from beetle_system import BeetleSystem
from boxes import Boxes
from base import Base
from web import Web


win_x = Window.size[0]
win_y = Window.size[1]
solve = solve.Solve()

class SpideyGame(Widget):

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
	base = Base()

	def __init__(self, **kwargs):
		super(SpideyGame, self).__init__(**kwargs)
		self.gameworld.init_gameworld(
			['renderer', 'position'],
			callback=self.init_game)

		'''# keyboard
		self._keyboard = Window.request_keyboard(self._keyboard_closed, self, 'text')
		if self._keyboard.widget:
			pass # what is this?
		self._keyboard.bind(on_key_down=self._on_keyboard_down)
		self._keyboard.bind(on_key_up=self._on_keyboard_up)'''

	def init_game(self):
		state = 'main'
		self.setup_states()
		self.set_state(state)
		
		self.base.initiate_level()
		print("Initiated level")
		self.beetle_system.start()
		print("Beetle system started")
		#self.draw_stuff()
		#Clock.schedule_interval(self.update, 1.0 / 60.0)

	def setup_states(self):
		self.gameworld.add_state(state_name='menu',
			systems_added=['renderer'],
			systems_removed=[], systems_paused=[],
			systems_unpaused=['renderer'],
			screenmanager_screen='menu')

		self.gameworld.add_state(state_name='main',
			systems_added=['renderer'],
			systems_removed=[], systems_paused=[],
			systems_unpaused=['renderer'],
			screenmanager_screen='main')

		self.gameworld.add_state(state_name='message',
			systems_added=['renderer'],
			systems_removed=[], systems_paused=[],
			systems_unpaused=['renderer'],
			screenmanager_screen='message')
			
		self.gameworld.add_state(state_name='settings',
			systems_added=['renderer'],
			systems_removed=[], systems_paused=[],
			systems_unpaused=['renderer'],
			screenmanager_screen='settings')

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
		#self.points = self.points + list([win_x * char_x, win_y * char_y]) 
		self.web.draw_web()
		#print "touched"
		#return True

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
