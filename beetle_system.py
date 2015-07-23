from kivy.core.window import Window
from kivent_core.systems.gamesystem import GameSystem
from kivent_core.managers.resource_managers import (
	texture_manager, model_manager)
from kivy.factory import Factory
from kivy.clock import Clock
from random import randint, choice

texture_manager.load_atlas('assets/background_objects.atlas')
model_manager.load_textured_rectangle(4, 7., 7., 'star1', 'star1-4')
model_manager.load_textured_rectangle(4, 10., 10., 'star1', 'star1-4-2')

win_x = Window.size[0]
win_y = Window.size[1]

class BeetleSystem(GameSystem):

	beetles_count = 0
	beetles = {}

	def __init__(self, *args, **kwargs):
		super(BeetleSystem, self).__init__(*args, **kwargs)

	def start(self):
		self.draw_stuff()
		Clock.schedule_interval(self.update, 1.0 / 60.0)

	def draw_stuff(self):
		dir_from = choice(['N', 'S', 'W', 'E'])

		if dir_from == 'N':
			x, y = randint(0, win_x), win_y + (win_y / 20)
		elif dir_from == 'S':
			x, y = randint(0, win_x), 0 - (win_y / 20)
		elif dir_from == 'W':
			x, y = 0 - (win_x / 20), randint(0, win_y)
		elif dir_from == 'E':
			x, y = win_x + (win_x / 20), randint(0, win_y)

		ent_id = self.create_beetle(x, y)
		self.beetles[self.beetles_count] = [dir_from, x, y]
		self.beetles_count += 1
		#print(self.beetles)
		#print(self.beetles_count)

	def destroy_created_entity(self, ent_id, dt):
		self.gameworld.remove_entity(ent_id)
		#self.app.count -= 1

	def create_beetle(self, x, y):
		vert_mesh_key = choice(['star1-4', 'star1-4-2'])
		create_dict = {
			'position': (x, y),
			'renderer': {'texture': 'star1',
				'vert_mesh_key': vert_mesh_key},
			}
		return self.gameworld.init_entity(create_dict, ['position',
			'renderer'])

	def update(self, dt):
		entities = self.gameworld.entities
		for b in xrange(self.beetles_count):
			#print('b', b)
			pos = entities[b].position
			dir_from = self.beetles[b][0]
			if dir_from == 'N':
				pos.y -= .15
			elif dir_from == 'S':
				pos.y += .15
			elif dir_from == 'W':
				pos.x += .15
			elif dir_from == 'E':
				pos.x -= .15

		'''
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


Factory.register('BeetleSystem', cls=BeetleSystem)
