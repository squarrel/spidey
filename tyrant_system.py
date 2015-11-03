from kivy.core.window import Window
from kivent_core.systems.gamesystem import GameSystem
from kivy.factory import Factory
from kivy.properties import StringProperty, NumericProperty
from kivy.clock import Clock
from random import randint, choice
from base import Base


win_x = Window.size[0]
win_y = Window.size[1]

class TyrantSystem(GameSystem):

	tyrants = {}
	active = False
	on_mark = False

	def __init__(self, *args, **kwargs):
		super(TyrantSystem, self).__init__(*args, **kwargs)
		self.tyrant = None

	def start(self):
		self.active = True
		self.draw_stuff()
		Clock.schedule_interval(self.update, 1.0 / 60.0)
		#Clock.schedule_interval(self.check_vars, 2.0 / 1.0)

	def check_vars(self, dt):
		print "tyrant boxes", self.base.boxes
		print "tyrant slices", self.base.slices
		print "tyrant current_level", self.base.current_level
		print "tyrant divisions", self.base.divisions

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
				x, y = randint(0, win_x), 15
				image = 'beetle_up'
			elif dir_to == 'S':
				x, y = randint(0, win_x), win_y - 15
				image = 'beetle_down'
			elif dir_to == 'W':
				x, y = win_x - 15, randint(0, win_y)
				image = 'beetle_left'
			elif dir_to == 'E':
				x, y = 15, randint(0, win_y)
				image = 'beetle_right'

			ent_id = self.create_tyrant(x, y, image)
			#print "starting x, y", x, y
			self.tyrants[ent_id] = [dir_to, 3]
			#print self.tyrants

	def remove_tyrant(self, ent_id):
		self.gameworld.remove_entity(ent_id)

	def create_tyrant(self, x, y, image):
		create_dict = {
			'position': (x, y),
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
				direction = self.tyrants[entity_id][0]
				render_comp = entities[entity_id].renderer

				tyrant_box = self.boxes.current_box(pos.x, pos.y)
				#print "tyrant_box", tyrant_box
				spider_x = round(self.spider_system.x, 2)
				spider_y = round(self.spider_system.y, 2)
				spider_box = self.boxes.current_box(spider_x, spider_y)
				div = self.base.divisions
				#print "base.divisions", base.divisions
				# current row where the tyrant is
				tyrant_row = (tyrant_box / div) + 1
				spider_row = (spider_box / div) + 1
				#print win_x, "x", win_y
				#print "tyrant.x, tyrant.y", pos.x, pos.y
				#print "spider_x, spider_y", spider_x, spider_y
				#print "self.tyrants[entity_id][0]", self.tyrants[entity_id][0]
				#print base.boxes
				#print "tyrant_box", tyrant_box
				#print "spider_box", spider_box
				#print "tyrant_row", tyrant_row
				#print "spider_row", spider_row

				if direction == 'N':
					pos.y += .30
				elif direction == 'S':
					pos.y -= .30
				elif direction == 'W':
					pos.x -= .30
				elif direction == 'E':
					pos.x += .30

				if tyrant_row == spider_row:
					if pos.x > spider_x:
						#print "should be W now"
						self.tyrants[entity_id][0] = 'W'
					elif pos.x < spider_x:
						#print "should be E now"
						self.tyrants[entity_id][0] = 'E'
				elif tyrant_row > spider_row:
					#print "should be S now"
					self.tyrants[entity_id][0] = 'S'
				elif tyrant_row < spider_row:
					#print "should be N now"
					self.tyrants[entity_id][0] = 'N'

				if tyrant_box == spider_box:
					#print "BEATEN!"
					pass

				if pos.x < 10 or pos.x > win_x - 10 or pos.y < 10 or pos.y > win_y - 10:
					#self.remove_tyrant(entity_id)
					self.tyrants[entity_id][0] = self.reverse(direction)
					#print "tyrant removed, cause out of screen"

	def reverse(self, direction):
		if direction == 'N':
			return 'S'
		elif direction == 'S':
			return 'N'
		elif direction == 'W':
			return 'E'
		elif direction == 'E':
			return 'W'

Factory.register('TyrantSystem', cls=TyrantSystem)
