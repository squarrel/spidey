from kivy.core.window import Window
from kivent_core.systems.gamesystem import GameSystem
from kivent_core.gameworld import GameWorld
from kivy.factory import Factory
from kivy.properties import StringProperty, NumericProperty
from kivy.clock import Clock
from random import randint, choice
from boxes import Boxes
from base import Base
from panel import Panel


win_x = Window.size[0]
win_y = Window.size[1]
base = Base()

class BeetleSystem(GameSystem):

	system_id = StringProperty('beetle_system')
	beetles = {}
	score = 0
	score_ = StringProperty(str(score))
	active = False

	def __init__(self, *args, **kwargs):
		super(BeetleSystem, self).__init__(*args, **kwargs)

	def start(self):
		Clock.schedule_interval(self.draw_stuff, 1.0 / 3.0)
		self.active = True
		Clock.schedule_interval(self.update, 1.0 / 60.0)

	def stop(self):
		self.active = False
		entities = self.gameworld.entities
		for component in self.components:
			if component is not None:
				entity_id = component.entity_id
				self.remove_beetle(entity_id)
		Clock.unschedule(self.update)
		Clock.unschedule(self.draw_stuff)

	def pause(self):
		self.active = False

	def resume(self):
		self.active = True

	def draw_stuff(self, dt):
		if self.active:
			dir_to = choice(['N', 'S', 'W', 'E'])

			if dir_to == 'N':
				x, y = randint(0, win_x), 0
				image = 'beetle_up'
			elif dir_to == 'S':
				x, y = randint(0, win_x), win_y
				image = 'beetle_down'
			elif dir_to == 'W':
				x, y = win_x, randint(0, win_y)
				image = 'beetle_left'
			elif dir_to == 'E':
				x, y = 0, randint(0, win_y )
				image = 'beetle_right'

			ent_id = self.create_beetle(x, y, image)
			# add the beetle to the dictionary along with values for
			# direction, energy and 'waiting' value
			self.beetles[ent_id] = [dir_to, 3, 20]
			#print(self.beetles)

	def set_image(self, dir_to):
		if dir_to == 'N':
			image = 'beetle_up'
			return image

	def remove_beetle(self, ent_id):
		self.gameworld.remove_entity(ent_id)

	def create_beetle(self, x, y, image):
		create_dict = {
			'position': (x, y),
			'renderer': {'texture': image,
				'vert_mesh_key': image},
			'beetle_system': {},
			}
		return self.gameworld.init_entity(create_dict, ['position',
			'renderer', 'beetle_system'])

	def update(self, dt):
		if self.active:
			entities = self.gameworld.entities

			for component in self.components:
				if component is not None:
					entity_id = component.entity_id
					pos = entities[entity_id].position
					render_comp = entities[entity_id].renderer
					current_box = self.boxes.current_box(pos.x, pos.y)
					div = base.divisions
					remove_beetle = self.remove_beetle
					dist_x = win_x / 20
					dist_y = win_y / 20
					#print("current_box", current_box)

					# for a given direction and current position
					if self.beetles[entity_id][0] == 'N':
						# calculate the next box
						next_box = current_box + base.divisions
						#print dir_to, current_box, next_box

						if next_box in xrange(1, base.current_level):
							# if the next box is a trap
							if base.boxes[next_box]:
								# when a beetle reaches it
								if pos.y > (((next_box - 1) / div) * (win_y / div)) - dist_y:
									# make a turn to a different direction
									self.beetles[entity_id][0] = choice(['W', 'E'])
									# reduce beetle energy by 1
									self.beetles[entity_id][1] -= 1
									# activate the 'wait for it' switch
									# by reducing its third value by 1.
									self.beetles[entity_id][2] -= 1
									# change beetle's texture to suit the new direction
									if self.beetles[entity_id][0] == 'W':
										render_comp.texture_key = 'beetle_left'
									else:
										render_comp.texture_key = 'beetle_right'

									# if the bettle has no energy left
									if self.beetles[entity_id][1] == 0:
										# remove it
										self.remove_beetle(entity_id)
										# and add score to the player
										self.score += 1
										self.score_ = str(self.score)
										break
									else:
										continue

						# make the beetle pause and/or continue
						if 0 < self.beetles[entity_id][2] < 20:
							self.beetles[entity_id][2] -= 1
						elif self.beetles[entity_id][2] == 0:
							self.beetles[entity_id][2] = 20
						else:
							pos.y += .95

					elif self.beetles[entity_id][0] == 'S':
						next_box = current_box - base.divisions
						#print dir_to, current_box, next_box
						if next_box in xrange(1, base.current_level):
							if base.boxes[next_box]:
								if pos.y < (((next_box - 1) / div) * (win_y / div)) + win_y / div + dist_y:
									self.beetles[entity_id][0] = choice(['W', 'E'])
									self.beetles[entity_id][1] -= 1
									self.beetles[entity_id][2] -= 1
									if self.beetles[entity_id][0] == 'W':
										render_comp.texture_key = 'beetle_left'
									else:
										render_comp.texture_key = 'beetle_right'

									if self.beetles[entity_id][1] == 0:
										self.remove_beetle(entity_id)
										self.score += 1
										self.score_ = str(self.score)
										break
									else:
										continue

						if 0 < self.beetles[entity_id][2] < 20:
							self.beetles[entity_id][2] -= 1
						elif self.beetles[entity_id][2] == 0:
							self.beetles[entity_id][2] = 20
						else:
							pos.y -= .95

					elif self.beetles[entity_id][0] == 'W':
						next_box = current_box - 1
						#print dir_to, current_box, next_box
						if next_box in xrange(1, base.current_level):
							if base.boxes[next_box]:
								if pos.x < (((next_box - 1) % div) * (win_x / div)) + win_x / div + dist_x:
									self.beetles[entity_id][0] = choice(['N', 'S'])
									self.beetles[entity_id][1] -= 1
									self.beetles[entity_id][2] -= 1
									if self.beetles[entity_id][0] == 'N':
										render_comp.texture_key = 'beetle_up'
									else:
										render_comp.texture_key = 'beetle_down'

									if self.beetles[entity_id][1] == 0:
										self.remove_beetle(entity_id)
										self.score += 1
										self.score_ = str(self.score)
										break
									else:
										continue

						if 0 < self.beetles[entity_id][2] < 20:
							self.beetles[entity_id][2] -= 1
						elif self.beetles[entity_id][2] == 0:
							self.beetles[entity_id][2] = 20
						else:
							pos.x -= .95

					elif self.beetles[entity_id][0] == 'E':
						next_box = current_box + 1
						#print dir_to, current_box, next_box
						if next_box in xrange(1, base.current_level):
							if base.boxes[next_box]:
								if pos.x > (((next_box - 1) % div) * (win_x / div)) - dist_x:
									self.beetles[entity_id][0] = choice(['N', 'S'])
									self.beetles[entity_id][1] -= 1
									self.beetles[entity_id][2] -= 1
									if self.beetles[entity_id][0] == 'N':
										render_comp.texture_key = 'beetle_up'
									else:
										render_comp.texture_key = 'beetle_down'

									if self.beetles[entity_id][1] == 0:
										self.remove_beetle(entity_id)
										self.score += 1
										self.score_ = str(self.score)
										break
									else:
										continue

						if 0 < self.beetles[entity_id][2] < 20:
							self.beetles[entity_id][2] -= 1
						elif self.beetles[entity_id][2] == 0:
							self.beetles[entity_id][2] = 20
						else:
							pos.x += .95

					if pos.x < 0 or pos.x > win_x or pos.y < 0 or pos.y > win_y:
						self.remove_beetle(entity_id)


Factory.register('BeetleSystem', cls=BeetleSystem)
