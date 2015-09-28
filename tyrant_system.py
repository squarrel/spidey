from kivy.core.window import Window
from kivent_core.systems.gamesystem import GameSystem
from kivy.factory import Factory
from kivy.properties import StringProperty, NumericProperty
from kivy.clock import Clock


win_x = Window.size[0]
win_y = Window.size[1]

class TyrantSystem(GameSystem):
	
	system_id = StringProperty('tyrant_system')
	x = NumericProperty(.15)
	y = NnumericProperty(.15)
	
	def __init__(self, *args, **kwargs):
		super(TyrantSystem, self).__init__(*args, **kwargs)
		
		self.tyrant = None

	def start(self):
		self.draw_stuff()
		Clock.schedule_interval(self.update, 1.0 / 60.0)

	def stop(self):
		Clock.unschedule(self.update)
		if self.tyrant:
			self.destroy_entity(tyrant)

	def draw_stuff(self):
		ent_id = self.create_tyrant(self.x, self.y)

	def destroy_entity(self, ent_id):
		self.gameworld.remove_entity(ent_id)

	def create_entity(self, x, y):
		vert_mesh_key = 'beetle_left'
		create_dict = {
			'position': (win_x * x, win_y * y),
			'renderer': {'texture': 'beetle_left',
						'vert_mesh_key': vert_mesh_key},
			'tyrant_system': {},
			}
		self.tyrant = self.gameworld.init_entity(create_dict, ['position',
			'renderer', 'tyrant_system'])

	def update(self, dt):
		entities = self.gameworld.entities
		for component in self.components:
			if component is not None:
				entity_id = component.entity_id
				pos = entities[entity_id].position
				if 0 <= pos.x <= win_x and 0 <= pos.y <= win_y:
					pos.x = win_x * self.x
					pos.y = win_y * self.y


Factory.register('TyrantSystem', cls=TyrantSystem)
