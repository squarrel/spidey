from kivy.core.window import Window
from kivy.factory import Factory
from kivy.clock import Clock
from kivy.properties import NumericProperty, StringProperty
from kivent_core.systems.gamesystem import GameSystem
from kivent_core.managers.resource_managers import (
	texture_manager, model_manager)
from random import randint, choice


win_x = Window.size[0]
win_y = Window.size[1]

class SpiderSystem(GameSystem):

	system_id = StringProperty('spider_system')
	x = NumericProperty(.15)
	y = NumericProperty(.15)

	def __init__(self, *args, **kwargs):
		super(SpiderSystem, self).__init__(*args, **kwargs)

	# start spider system
	def start(self):
		self.draw_stuff()
		Clock.schedule_interval(self.update, 1.0 / 60.0)
		
	def stop(self):
		self.destroy_created_entity(self.spider)

	def draw_stuff(self):
		ent_id = self.create_spider(self.x, self.y)

	def destroy_created_entity(self, ent_id):
		self.gameworld.remove_entity(ent_id)

	def create_spider(self, x, y):
		vert_mesh_key = choice(['star1-4', 'star1-4-2'])
		create_dict = {
			'position': (win_x * x, win_y * y),
			'renderer': {'texture': 'star1',
				'vert_mesh_key': vert_mesh_key},
			'spider_system': {},
			}
		self.spider = self.gameworld.init_entity(create_dict, ['position',
			'renderer', 'spider_system'])

	def update(self, dt):
		entities = self.gameworld.entities
		for component in self.components:
			if component is not None:
				entity_id = component.entity_id
				pos = entities[entity_id].position
				if 0 <= pos.x <= win_x and 0 <= pos.y <= win_y:
					pos.x = win_x * self.x
					pos.y = win_y * self.y
		
		'''entity = self.gameworld.entities[self.spider]
		pos = entity.position
		if 0 <= pos.x <= win_x and 0 <= pos.y <= win_y:
			pos.x = win_x * self.x
			pos.y = win_y * self.y'''


Factory.register('SpiderSystem', cls=SpiderSystem)
