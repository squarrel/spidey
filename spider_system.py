from kivy.core.window import Window
from kivy.factory import Factory
from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivent_core.systems.gamesystem import GameSystem
from kivent_core.managers.resource_managers import (
	texture_manager, model_manager)
from random import randint, choice


win_x = Window.size[0]
win_y = Window.size[1]
	
class SpiderSystem(GameSystem):

	x = NumericProperty(.15)
	y = NumericProperty(.15)

	def __init__(self, *args, **kwargs):
		super(SpiderSystem, self).__init__(*args, **kwargs)

	def start(self):
		self.draw_stuff()
		Clock.schedule_interval(self.update, 1.0 / 60.0)
		
	def draw_stuff(self):
		ent_id = self.create_spider(self.x, self.y)

	def destroy_created_entity(self, ent_id, dt):
		self.gameworld.remove_entity(ent_id)

	def create_spider(self, x, y):
		vert_mesh_key = choice(['star1-4', 'star1-4-2'])
		create_dict = {
			'position': (win_x * x, win_y * y),
			'renderer': {'texture': 'star1',
				'vert_mesh_key': vert_mesh_key},
			}
		self.spider = self.gameworld.init_entity(create_dict, ['position',
			'renderer'])

	def update(self, dt):
		entity = self.gameworld.entities[self.spider]
		pos = entity.position
		pos.x = win_x * self.x
		pos.y = win_y * self.y

		'''# char and background texture movement
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


Factory.register('SpiderSystem', cls=SpiderSystem)
