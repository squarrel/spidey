'''
Figure out which lines are intersecting.

TODO:
- some crosspoints are not recognized.
'''

class PartOf(object):

	dir_first = ''
	dir_second = ''

	def get_direction(self, p1, q1, p2, q2):
		direction = ''
		# figure out the direction of lines, north-east, north-west...
		if p1 < p2 and q1 < q2:
			direction = 'NE'
		elif p1 > p2 and q1 < q2:
			direction = 'NW'
		elif p1 < p2 and q1 > q2:
			direction = 'SE'
		elif p1 > p2 and q1 > q2:
			direction = 'SW'
		elif p1 == p2 and q1 < q2:
			direction = 'N'
		elif p1 == p2 and q1 > q2:
			direction = 'S'
		elif p1 < p2 and q1 == q2:
			direction = 'E'
		elif p1 > p2 and q1 == q2:
			direction = 'W'
		#print "direction", direction
		return direction

	def direction(self, x1, y1, x2, y2, a1, b1, a2, b2):
		self.dir_first = self.get_direction(x1, y1, x2, y2)
		self.dir_second = self.get_direction(a1, b1, a2, b2)

	# see if the intersection point is anywhere on our lines
	def part_of(self, x1, y1, x2, y2, a1, b1, a2, b2, x, y):
		self.direction(x1, y1, x2, y2, a1, b1, a2, b2)
		dir_first = self.dir_first
		dir_second = self.dir_second

		# ---- NE
		if dir_first == 'NE' and dir_second == 'NE':
			if x1 < x < x2 and y1 < y < y2 \
			and a1 < x < a2 and b1 < y < b2:
				print("point")
				return True
		elif dir_first == 'NE' and dir_second == 'NW':
			if x1 < x < x2 and y1 < y < y2 \
			and a2 < x < a1 and b1 < y < b2:
				print("point")
				return True
		elif dir_first == 'NE' and dir_second == 'SE':
			if x1 < x < x2 and y1 < y < y2 \
			and a1 < x < a2 and b2 < y < b1:
				print("point")
				return True
		elif dir_first == 'NE' and dir_second == 'SW':
			if x1 < x < x2 and y1 < y < y2 \
			and a2 < x < a1 and b2 < y < b1:
				print("point")
				return True
		# -
		elif dir_first == 'NE' and dir_second == 'N':
			if x1 < x < x2 and y1 < y < y2 \
			and a1 == x and b1 < y < b2:
				print("point")
				return True
		elif dir_first == 'NE' and dir_second == 'S':
			if x1 < x < x2 and y1 < y < y2 \
			and a1 == x and b2 < y < b1:
				print("point")
				return True
		elif dir_first == 'NE' and dir_second == 'E':
			if x1 < x < x2 and y1 < y < y2 \
			and a1 < x < a2 and b1 == y:
				print("point")
				return True
		elif dir_first == 'NE' and dir_second == 'W':
			if x1 < x < x2 and y1 < y < y2 \
			and a2 < x < a1 and b1 == y:
				print("point")
				return True
		# ---- NW
		elif dir_first == 'NW' and dir_second == 'NE':
			if x2 < x < x1 and y1 < y < y2 \
			and a1 < x < a2 and b1 < y < y2:
				print("point")
				return True
		elif dir_first == 'NW' and dir_second == 'NW':
			if x2 < x < x1 and y1 < y < y2 \
			and a2 < x < a1 and b1 < y < y2:
				print("point")
				return True
		elif dir_first == 'NW' and dir_second == 'SE':
			if x2 < x < x1 and y1 < y < y2 \
			and a1 < x < a2 and b2 < y < y1:
				print("point")
				return True
		elif dir_first == 'NW' and dir_second == 'SW':
			if x2 < x < x1 and y1 < y < y2 \
			and a2 < x < a1 and b2 < y < y1:
				print("point")
				return True
		# -
		elif dir_first == 'NW' and dir_second == 'N':
			if x2 < x < x1 and y1 < y < y2 \
			and a1 == x and b1 < y < b2:
				print("point")
				return True
		elif dir_first == 'NW' and dir_second == 'S':
			if x2 < x < x1 and y1 < y < y2 \
			and a1 == x and b2 < y < b1:
				print("point")
				return True
		elif dir_first == 'NW' and dir_second == 'E':
			if x2 < x < x1 and y1 < y < y2 \
			and a1 < x < a2 and b1 == y:
				print("point")
				return True
		elif dir_first == 'NW' and dir_second == 'W':
			if x2 < x < x1 and y1 < y < y2 \
			and a2 < x < a1 and b1 == y:
				print("point")
				return True
		# ---- SE
		elif dir_first == 'SE' and dir_second == 'NE':
			if x1 < x < x2 and y2 < y < y1 \
			and a1 < x < a2 and b1 < y < b2:
				print("point")
				return True
		elif dir_first == 'SE' and dir_second == 'NW':
			if x1 < x < x2 and y2 < y < y1 \
			and a2 < x < a1 and b1 < y < b2:
				print("point")
				return True
		elif dir_first == 'SE' and dir_second == 'SE':
			if x1 < x < x2 and y2 < y < y1 \
			and a1 < x < a2 and b2 < y < b1:
				print("point")
				return True
		elif dir_first == 'SE' and dir_second == 'SW':
			if x1 < x < x2 and y2 < y < y1 \
			and a2 < x < a1 and b2 < y < b1:
				print("point")
				return True
		# -
		elif dir_first == 'SE' and dir_second == 'N':
			if x1 < x < x2 and y2 < y < y1 \
			and a1 == x and b1 < y < b2:
				print("point")
				return True
		elif dir_first == 'SE' and dir_second == 'S':
			if x1 < x < x2 and y2 < y < y1 \
			and a1 == x and b2 < y < b1:
				print("point")
				return True
		elif dir_first == 'SE' and dir_second == 'E':
			if x1 < x < x2 and y2 < y < y1 \
			and a1 < x < a2 and b1 == y:
				print("point")
				return True
		elif dir_first == 'SE' and dir_second == 'W':
			if x1 < x < x2 and y2 < y < y1 \
			and a2 < x < a1 and b1 == y:
				print("point")
				return True
		# ---- SW
		elif dir_first == 'SW' and dir_second == 'NE':
			if x2 < x < x1 and y2 < y < y1 \
			and a1 < x < a2 and b1 < y < b2:
				print("point")
				return True
		elif dir_first == 'SW' and dir_second == 'NW':
			if x2 < x < x1 and y2 < y < y1 \
			and a2 < x < a1 and b1 < y < b2:
				print("point")
				return True
		elif dir_first == 'SW' and dir_second == 'SE':
			if x2 < x < x1 and y2 < y < y1 \
			and a1 < x < a2 and b2 < y < b1:
				print("point")
				return True
		elif dir_first == 'SW' and dir_second == 'SW':
			if x2 < x < x1 and y2 < y < y1 \
			and a2 < x < a1 and b2 < y < b1:
				print("point")
				return True
		# -
		elif dir_first == 'SW' and dir_second == 'N':
			if x2 < x < x1 and y2 < y < y1 \
			and a1 == x and b1 < y < b2:
				print("point")
				return True
		elif dir_first == 'SW' and dir_second == 'S':
			if x2 < x < x1 and y2 < y < y1 \
			and a1 == x and b2 < y < b1:
				print("point")
				return True
		elif dir_first == 'SW' and dir_second == 'E':
			if x2 < x < x1 and y2 < y < y1 \
			and a1 < x < a2 and b1 == y:
				print("point")
				return True
		elif dir_first == 'SW' and dir_second == 'W':
			if x2 < x < x1 and y2 < y < y1 \
			and a2 < x < a1 and b1 == y:
				print("point")
				return True
		# ---- N
		elif dir_first == 'N' and dir_second == 'NE':
			if x1 == x and y1 < y < y2 \
			and a1 < x < a2 and b1 < y < b2:
				print("point")
				return True	
		elif dir_first == 'N' and dir_second == 'NW':
			if x1 == x and y1 < y < y2 \
			and a2 < x < a1 and b1 < y < b2:
				print("point")
				return True
		elif dir_first == 'N' and dir_second == 'SE':
			if x1 == x and y1 < y < y2 \
			and a1 < x < a2 and b2 < y < b1:
				print("point")
				return True
		elif dir_first == 'N' and dir_second == 'SW':
			if x1 == x and y1 < y < y2 \
			and a2 < x < a1 and b2 < y < b1:
				print("point")
				return True
		# --
		elif dir_first == 'N' and dir_second == 'N':
			if x1 == x and y1 < y < y2 \
			and a1 == x and b1 < y < b2:
				print("point")
				return True
		elif dir_first == 'N' and dir_second == 'S':
			if x1 == x and y1 < y < y2 \
			and a1 < x < a2 and b1 < y < b2:
				print("point")
				return True
		elif dir_first == 'N' and dir_second == 'E':
			if x1 == x and y1 < y < y2 \
			and a1 < x < a2 and b1 == y:
				print("point")
				return True
		elif dir_first == 'N' and dir_second == 'W':
			if x1 == x and y1 < y < y2 \
			and a2 < x < a1 and b1 == y:
				print("point")
				return True
		# ---- S
		elif dir_first == 'S' and dir_second == 'NE':
			if x1 == x and y2 < y < y1 \
			and a1 < x < a2 and b1 < y < b2:
				print("point")
				return True
		elif dir_first == 'S' and dir_second == 'NW':
			if x1 == x and y2 < y < y1 \
			and a2 < x < a1 and b1 < y < b2:
				print("point")
				return True
		elif dir_first == 'S' and dir_second == 'SE':
			if x1 == x and y2 < y < y1 \
			and a1 < x < a2 and b2 < y < b1:
				print("point")
				return True
		elif dir_first == 'S' and dir_second == 'SW':
			if x1 == x and y2 < y < y1 \
			and a2 < x < a1 and b2 < y < b1:
				print("point")
				return True
		# --
		elif dir_first == 'S' and dir_second == 'N':
			if x1 == x and y2 < y < y1 \
			and a1 == x and b1 < y < b2:
				print("point")
				return True
		elif dir_first == 'S' and dir_second == 'S':
			if x1 == x and y2 < y < y1 \
			and a1 == x and b2 < y < b1:
				print("point")
				return True
		elif dir_first == 'S' and dir_second == 'E':
			if x1 == x and y2 < y < y1 \
			and a1 < x < a2 and b1 == y:
				print("point")
				return True
		elif dir_first == 'S' and dir_second == 'W':
			if x1 == x and y2 < y < y1 \
			and a2 < x < a1 and b1 == y:
				print("point")
				return True
		# ---- E
		elif dir_first == 'E' and dir_second == 'NE':
			if x1 < x < x2 and y1 == y \
			and a1 < x < a2 and b1 < y < b2:
				print("point")
				return True
		elif dir_first == 'E' and dir_second == 'NW':
			if x1 < x < x2 and y1 == y \
			and a2 < x < a1 and b1 < y < b2:
				print("point")
				return True
		elif dir_first == 'E' and dir_second == 'SE':
			if x1 < x < x2 and y1 == y \
			and a1 < x < a2 and b2 < y < b1:
				print("point")
				return True
		elif dir_first == 'E' and dir_second == 'SW':
			if x1 < x < x2 and y1 == y \
			and a2 < x < a1 and b2 < y < b1:
				print("point")
				return True
		# --
		elif dir_first == 'E' and dir_second == 'N':
			if x1 < x < x2 and y1 == y \
			and a1 == x and b1 < y < b2:
				print("point")
				return True
		elif dir_first == 'E' and dir_second == 'S':
			if x1 < x < x2 and y1 == y \
			and a2 == x and b2 < y < b1:
				print("point")
				return True
		elif dir_first == 'E' and dir_second == 'E':
			if x1 < x < x2 and y1 == y \
			and a1 < x < a2 and b2 == y:
				print("point")
				return True
		elif dir_first == 'E' and dir_second == 'W':
			if x1 < x < x2 and y1 == y \
			and a2 < x < a1 and b2 == y:
				print("point")
				return True
		# ---- W
		elif dir_first == 'W' and dir_second == 'NE':
			if x2 < x < x1 and y1 == y \
			and a1 < x < a2 and b1 < y < b2:
				print("point")
				return True
		elif dir_first == 'W' and dir_second == 'NW':
			if x2 < x < x1 and y1 == y \
			and a2 < x < a1 and b1 < y < b2:
				print("point")
				return True
		elif dir_first == 'W' and dir_second == 'SE':
			if x2 < x < x1 and y1 == y \
			and a1 < x < a2 and b2 < y < b1:
				print("point")
				return True
		elif dir_first == 'W' and dir_second == 'SW':
			if x2 < x < x1 and y1 == y \
			and a2 < x < a1 and b2 < y < b1:
				print("point")
				return True
		# --
		elif dir_first == 'W' and dir_second == 'N':
			if x2 < x < x1 and y1 == y \
			and a1 == x and b1 < y < b2:
				print("point")
				return True
		elif dir_first == 'W' and dir_second == 'S':
			if x2 < x < x1 and y1 == y \
			and a2 == x and b2 < y < b1:
				print("point")
				return True
		elif dir_first == 'W' and dir_second == 'E':
			if x2 < x < x1 and y1 == y \
			and a1 < x < a2 and b1 == y:
				print("point")
				return True
		elif dir_first == 'W' and dir_second == 'W':
			if x2 < x < x1 and y1 == y \
			and a2 < x < a1 and b1 == y:
				print("point")
				return True

		return False
