# Spidey Scientist

from kivy.app import App
print('imported kivy')
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import StringProperty, NumericProperty, ListProperty
from kivy.uix.screenmanager import Screen

import kivent_core
import kivent_cymunk
from kivent_core.gameworld import GameWorld
from kivent_core.systems.renderers import RotateRenderer
from kivent_core.systems.position_systems import PositionSystem2D
from kivent_core.systems.rotate_systems import RotateSystem2D
from kivent_core.systems.gamesystem import GameSystem
from kivent_core.managers.resource_managers import texture_manager

from spider_system import SpiderSystem
from beetle_system import BeetleSystem
from tyrant_system import TyrantSystem
from boxes import Boxes
from base import Base
from web import Web
from panel import Panel


texture_manager.load_atlas('assets/beetles.atlas')
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
		self.load_models()
		state = 'stop'
		self.set_state(state)
		base.initiate_level()
		self.boxes.draw_background(base.LEV_1)
		print("level initiated", win_x, "x", win_y)
		Clock.schedule_interval(self.update, 1.0 / 60.0)

	def load_models(self):
		model_manager = self.gameworld.model_manager
		model_manager.load_textured_rectangle('vertex_format_4f', 1., 1., 'beetle_up', 'beetle_up')
		model_manager.load_textured_rectangle('vertex_format_4f', 1., 1., 'beetle_down', 'beetle_down')
		model_manager.load_textured_rectangle('vertex_format_4f', 1., 1., 'beetle_left', 'beetle_left')
		model_manager.load_textured_rectangle('vertex_format_4f', 1., 1., 'beetle_right', 'beetle_right')

	# the update function; runs always
	def update(self, dt):
		# depending on wich screen is active, perform specific updates
		if self.screens.current == 'menu':
			if base.switch == 'play':
				self.start_game()
				base.switch = None

		elif self.screens.current == 'main':
			# character movement, background texture movement, animation
			if self.go_right:
				if self.spider_system.x * win_x < win_x - 5:
					self.spider_system.x += self.speed
				#self.t += .1
				#self.ani = 'pas_ani.zip'
			elif self.go_left:
				if self.spider_system.x * win_x > 5:
					self.spider_system.x -= self.speed
				#self.t -= .1
				#self.ani = 'pas_ani.zip'
			elif self.go_up:
				if self.spider_system.y * win_y < win_y - 5:
					self.spider_system.y += self.speed
				#self.ani = 'pas_ani.zip'	
			elif self.go_down:
				if self.spider_system.y * win_y > 5:
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

		#self.beetle_system.start()
		self.spider_system.start()
		#self.tyrant_system.start()
		#print("beetle system started")
		print("spider system started")
		#print("tyrant system started")

	# stop main game
	def stop_game(self):
		state = 'stop'
		self.set_state(state)

		self.beetle_system.stop()
		self.spider_system.stop()
		self.tyrant_system.stop()
		print("beetle system stopped")
		print("spider system stopped")
		print("tyrant system stopped")

	# pause main game
	def pause_game(self):
		self.beetle_system.pause()
		self.spider_system.stop()
		self.tyrant_system.stop()
		print("beetle system paused")
		print("spider system stopped")
		print("tyrant system stopped")
		
		state = 'pause'
		self.set_state(state)

	def resume_game(self):
		state = 'play'
		self.set_state(state)

		self.beetle_system.resume()
		self.spider_system.start()
		self.tyrant_system.start()
		print("beetle system resumed")
		print("spider system started")
		print("tyrant system started")

	# keyboard rules
	def _keyboard_closed(self):
		print('My keyboard has been closed!')
		self._keyboard.unbind(on_key_down=self._on_keyboard_down)
		self._keyboard.unbind(on_key_up=self._on_keyboard_up)
		self._keyboard = None

	# capture the keyboard down input and assign commands
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
			
			elif keycode[1] == 'escape':
				self.screens.switch = 'message'
				base.switch = 'pause'

		elif self.screens.current == 'menu':
			if keycode[1] == 'enter':
				self.screens.current = 'main'
				base.switch = 'play'
			elif keycode[1] == 'escape':
				exit()

		elif self.screens.current == 'message':
			if keycode[1] == 'escape':
				self.screens.current = 'main'
				base.switch = 'play'

		return True

	# capture the keyboard up input and assign commands
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

	# for touch screens
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
