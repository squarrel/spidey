from kivy.core.window import Window
from kivent_core.systems.gamesystem import GameSystem
from kivent_core.managers.resource_managers import (
	texture_manager, model_manager)
from kivy.factory import Factory
from kivy.clock import Clock
from random import randint, choice
from kivy.properties import StringProperty
from boxes import Boxes
from base import Base

texture_manager.load_atlas('assets/background_objects.atlas')
model_manager.load_textured_rectangle(4, 7., 7., 'star1', 'star1-4')
model_manager.load_textured_rectangle(4, 10., 10., 'star1', 'star1-4-2')

win_x = Window.size[0]
win_y = Window.size[1]
base = Base()

class BeetleSystem(GameSystem):

	system_id = StringProperty('beetle_system')
	beetles = {}

	def __init__(self, *args, **kwargs):
		super(BeetleSystem, self).__init__(*args, **kwargs)

	def start(self):
		Clock.schedule_interval(self.draw_stuff, 120.0 / 60.0)
		#Clock.schedule_once(self.draw_stuff)
		Clock.schedule_interval(self.update, 1.0 / 60.0)

	def draw_stuff(self, dt):
		dir_to = choice(['N', 'S', 'W', 'E'])

		if dir_to == 'N':
			x, y = randint(0, win_x), 0
		elif dir_to == 'S':
			x, y = randint(0, win_x), win_y
		elif dir_to == 'W':
			x, y = win_x, randint(0, win_y)
		elif dir_to == 'E':
			x, y = 0, randint(0, win_y)

		ent_id = self.create_beetle(x, y)
		self.beetles[ent_id] = dir_to
		#print(self.beetles)

	def remove_beetle(self, ent_id):
		self.gameworld.remove_entity(ent_id)

	def create_beetle(self, x, y):
		vert_mesh_key = choice(['star1-4', 'star1-4-2'])
		create_dict = {
			'position': (x, y),
			'renderer': {'texture': 'star1',
				'vert_mesh_key': vert_mesh_key},
			'beetle_system': {},
			}
		return self.gameworld.init_entity(create_dict, ['position',
			'renderer', 'beetle_system'])

	def update(self, dt):
		entities = self.gameworld.entities

		for component in self.components:
			if component is not None:
				entity_id = component.entity_id
				pos = entities[entity_id].position
				dir_to = self.beetles[entity_id]
				current_box = self.boxes.current_box(pos.x, pos.y)

				if dir_to == 'N':
					next_box = current_box + base.divisions
					print dir_to, current_box, next_box, base.boxes[next_box]
					if next_box in xrange(1, base.current_level):
						if base.boxes[next_box]:
							self.beetles[entity_id] = choice(['W', 'E'])
							continue
					pos.y += .15
				elif dir_to == 'S':
					next_box = current_box - base.divisions
					print dir_to, current_box, next_box, base.boxes[next_box]
					if next_box in xrange(1, base.current_level):
						if base.boxes[next_box]:
							self.beetles[entity_id] = choice(['W', 'E'])
							continue
					pos.y -= .15
				elif dir_to == 'W':
					next_box = current_box - 1
					print dir_to, current_box, next_box, base.boxes[next_box]
					if next_box in xrange(1, base.current_level):
						if base.boxes[next_box]:
							self.beetles[entity_id] = choice(['N', 'S'])
							continue
					pos.x -= .15
				elif dir_to == 'E':
					next_box = current_box + 1
					print dir_to, current_box, next_box, base.boxes[next_box]
					if next_box in xrange(1, base.current_level):
						if base.boxes[next_box]:
							self.beetles[entity_id] = choice(['N', 'S'])
							continue
					pos.x += .15

				if pos.x < 0 or pos.x > win_x or pos.y < 0 or pos.y > win_y:
					self.remove_beetle(entity_id)


Factory.register('BeetleSystem', cls=BeetleSystem)
