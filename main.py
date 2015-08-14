# Spidey Scientist

from kivy.app import App
print('imported kivy')
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import StringProperty, NumericProperty, ListProperty
from kivy.uix.screenmanager import Screen

from random import randint, choice
import math
from math import radians, pi, sin, cos
from functools import partial

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

from spider_system import SpiderSystem
from beetle_system import BeetleSystem
from boxes import Boxes
from base import Base
from web import Web
from panel import Panel


win_x = Window.size[0]
win_y = Window.size[1]
base = Base()

class SpideyGame(Widget):

	go_right = False
	go_left = False
	go_up = False
	go_down = False
	speed = .003

	def __init__(self, **kwargs):
		super(SpideyGame, self).__init__(**kwargs)
		self.gameworld.init_gameworld(['renderer', 'position'],
			callback=self.init_game)

		# keyboard
		self._keyboard = Window.request_keyboard(self._keyboard_closed, self, 'text')
		if self._keyboard.widget:
			pass
		self._keyboard.bind(on_key_down=self._on_keyboard_down)
		self._keyboard.bind(on_key_up=self._on_keyboard_up)

		self.screens = self.gameworld.gamescreenmanager

	def init_game(self):
		self.setup_states()
		state = 'stop'
		self.set_state(state)
		base.initiate_level()
		print("Initiated the level")
		Clock.schedule_interval(self.update, 1.0 / 60.0)

	# the update function; runs always
	def update(self, dt):
		# depending on wich screen is active, perform specific updates
		if self.screens.current == 'menu':
			pass

		elif self.screens.current == 'main':
			# character movement, background texture movement, animation
			if self.go_right:
				self.spider_system.x += self.speed
				#self.t += .1
				#self.ani = 'pas_ani.zip'	
			elif self.go_left:
				self.spider_system.x -= self.speed
				#self.t -= .1
				#self.ani = 'pas_ani.zip'
			elif self.go_up:
				self.spider_system.y += self.speed
				#self.ani = 'pas_ani.zip'	
			elif self.go_down:
				self.spider_system.y -= self.speed
				#self.ani = 'pas_ani.zip'	
			#else: self.ani = 'data/pauk.jpg'

			# if one of the switches is turned, 
			# perform an action and turn it off.
			if base.switch == 'play':
				self.start_game()
				base.switch = None
			elif base.switch == 'pause':
				self.pause_game()
				base.switch = None
			elif base.switch == 'resume':
				self.resume_game()
				base.switch = None
			elif base.switch == 'stop':
				self.stop_game()
				base.switch = None

		elif self.screens.current == 'message':
			if base.switch == 'stop':
				self.stop_game()
				base.switch = None

		elif self.screens.current == 'settings':
			pass

	# setup different states to be used in the game;
	# currently only one state type is used.
	def setup_states(self):
		self.gameworld.add_state(state_name='stop',
			systems_added=['renderer'],
			systems_removed=[], systems_paused=['renderer'],
			systems_unpaused=[],
			screenmanager_screen='menu')

		self.gameworld.add_state(state_name='play',
			systems_added=['renderer'],
			systems_removed=[], systems_paused=[],
			systems_unpaused=['renderer'],
			screenmanager_screen='main')

		self.gameworld.add_state(state_name='pause',
			systems_added=['renderer'],
			systems_removed=[], systems_paused=['renderer'],
			systems_unpaused=[],
			screenmanager_screen='message')

	# change state
	def set_state(self, *args):
		self.gameworld.state = args[0]

	# start main game
	def start_game(self):
		state = 'play'
		self.set_state(state)

		self.beetle_system.start()
		print("Beetle system started")
		self.spider_system.start()
		print("Spider system started")

	# stop main game
	def stop_game(self):
		state = 'stop'
		self.set_state(state)

		self.beetle_system.stop()
		print("Beetle system stopped")
		self.spider_system.stop()
		print("Spider system stopped")

	# pause main game
	def pause_game(self):
		state = 'pause'
		self.set_state(state)

		self.beetle_system.pause()
		print("Beetle system paused")

	def resume_game(self):
		state = 'play'
		self.set_state(state)

		self.beetle_system.resume()
		print("Beetle system resumed")

	# keyboard rules
	def _keyboard_closed(self):
		print('My keyboard has been closed!')
		self._keyboard.unbind(on_key_down=self._on_keyboard_down)
		self._keyboard.unbind(on_key_up=self._on_keyboard_up)
		self._keyboard = None

	# capture the keyboard-down input and assign commands
	def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
		# for each key assign an action

		if self.screens.current == 'main':
			# actions for the spider
			if keycode[1] == 'right':
				self.go_right = True
			elif keycode[1] == 'left':
				self.go_left = True
			elif keycode[1] == 'up':
				self.go_up = True
			elif keycode[1] == 'down':
				self.go_down = True
			elif keycode[1] == 'spacebar':
				self.web.draw_web()

		elif self.screens.current == 'menu':
			if keycode[1] == 'enter':
				self.screens.current = 'main'
				base.switch = 'main'
			elif keycode[1] == 'escape':
				exit()

		elif self.screens.current == 'message':
			if keycode[1] == 'escape':
				self.screens.current = 'main'

		return True

	# capture the keyboard-up input and assign commands
	def _on_keyboard_up(self, keyboard, keycode):
		if self.screens.current == 'main':
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
		if self.screens.current == 'main':
			self.web.draw_web()
			#print "touched"
			#return True

class StatusPanel(Widget):
	fps = StringProperty(None)

	def __init__(self, **kwargs):
		super(StatusPanel, self).__init__(**kwargs)
		Clock.schedule_once(self.update_fps, .05)

	def update_fps(self, dt):
		self.fps = str(int(Clock.get_fps()))
		Clock.schedule_once(self.update_fps, .05)

class MenuScreen(Screen):
	def start_game(self):
		base.switch = 'play'

class MainScreen(Screen):
	def pause_game(self):
		base.switch = 'pause'

class MessageScreen(Screen):
	def resume_game(self):
		base.switch = 'resume'

	def stop_game(self):
		base.switch = 'stop'

class Settings(Screen):
	pass

class SpideyApp(App):
	pass

if __name__ == '__main__':
	SpideyApp().run()
