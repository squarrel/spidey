from kivy.core.window import Window
from kivent_core.systems.gamesystem import GameSystem
from kivy.factory import Factory
from kivy.properties import StringProperty, NumericProperty
from kivy.clock import Clock
from random import randint, choice


win_x = Window.size[0]
win_y = Window.size[1]

class TyrantSystem(GameSystem):

	system_id = StringProperty('tyrant_system')
	tyrants = {}
	active = False

	def __init__(self, *args, **kwargs):
		super(TyrantSystem, self).__init__(*args, **kwargs)
		self.tyrant = None

	def start(self):
		self.draw_stuff()
		self.active = True
		Clock.schedule_interval(self.update, 1.0 / 60.0)

	def stop(self):
		self.active = False
		entities = self.gameworld.entities
		for component in self.components:
			if component is not None:
				entity_id = component.entity_id
				self.remove_tyrant(entity_id)
		Clock.unschedule(self.update)

	def pause(self):
		self.active = False

	def resume(self):
		self.active = True

	def draw_stuff(self):
		if self.active:
			dir_to = choice(['N', 'S', 'W', 'E'])

			if dir_to == 'N':
				image = 'beetle_up'
			elif dir_to == 'S':
				image = 'beetle_down'
			elif dir_to = 'W':
				image = 'beetle_left'
			elif dir_to == 'E':
				image = 'beetle_right'
			x, y = randint(0, win_x), randint(0, win_y)

		ent_id = self.create_tyrant(x, y, image)
		self.tyrants[ent_id] = [dir_to, 3]

	def remove_tyrant(self, ent_id):
		self.gameworld.remove_entity(ent_id)

	def create_tyrant(self, x, y, image):
		vert_mesh_key = 'beetle_left'
		create_dict = {
			'position': (win_x * x, win_y * y),
			'renderer': {'texture': image,
						'vert_mesh_key': image},
			'tyrant_system': {},
			}
		return self.gameworld.init_entity(create_dict, ['position',
			'renderer', 'tyrant_system'])

	def update(self, dt):
		entities = self.gameworld.entities
		for component in self.components:
			if component is not None:
				entity_id = component.entity_id
				pos = entities[entity_id].position
				pos.x = win_x * self.x
				pos.y = win_y * self.y
				current_box = self.boxes.current_box(pos.x, pos.y)
				# targetbox is where the spider is at
				target_box = self.boxes.current_box(self.spider_system.x, 
													self.spider_system.y)
				#print self.spider_system.x
				#print self.spider_system.y
				#print self.boxes


Factory.register('TyrantSystem', cls=TyrantSystem)
