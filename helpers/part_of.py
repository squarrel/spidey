'''
Figure out which lines are intersecting.

TODO:
- some crosspoints are not recognized.
'''

class PartOf(object):

	dir_first = ''
	dir_second = ''

	def get_direction(self, p, q, r, s):
		direction = ''
		# figure out the direction of lines, north-east, north-west...
		if p < q and r < s:
			direction = 'NE'
		elif p > q and r < s:
			direction = 'NW'
		elif p < q and r > s:
			direction = 'SE'
		elif p > q and r > s:
			direction = 'SW'
		elif p == q and r < s:
			direction = 'N'
		elif p == q and r < s:
			direction = 'S'
		elif p < q and r == s:
			direction = 'E'
		elif p < q and r == s:
			direction = 'W'
		return direction

	def direction(self, *args):
		x1, x2, y1, y2 = args[0], args[1], args[2], args[3]
		a1, a2, b1, b2 = args[4], args[5], args[6], args[7]

		self.dir_first = self.get_direction(x1, x2, y1, y2)
		self.dir_second = self.get_direction(a1, a2, b1, b2)

	def part_of(self, *args):
		x1, x2, y1, y2 = args[0], args[1], args[2], args[3]
		a1, a2, b1, b2 = args[4], args[5], args[6], args[7]
		self.direction(x1, x2, y1, y2, a1, a2, b1, b2)
		x, y = args[8], args[9]
		dir_first = self.dir_first
		dir_second = self.dir_second		

		# ---- NE
		if dir_first == 'NE' and dir_second == 'NE':
			if x1 < x < x2 and y1 < y < y2 \
			and a1 < x < a2 and b1 < y < b2:
				return True
		elif dir_first == 'NE' and dir_second == 'NW':
			if x1 < x < x2 and y1 < y < y2 \
			and a2 < x < a1 and b1 < y < b2:
				return True
		elif dir_first == 'NE' and dir_second == 'SE':
			if x1 < x < x2 and y1 < y < y2 \
			and a1 < x < a2 and b2 < y < b1:
				return True
		elif dir_first == 'NE' and dir_second == 'SW':
			if x1 < x < x2 and y1 < y < y2 \
			and a2 < x < a1 and b2 < y < b1:
				return True
		# -
		elif dir_first == 'NE' and dir_second == 'N':
			if x1 < x < x2 and y1 < y < y2 \
			and a1 == x and b1 < y < b2:
				return True
		elif dir_first == 'NE' and dir_second == 'S':
			if x1 < x < x2 and y1 < y < y2 \
			and a1 == x and b2 < y < b1:
				return True
		elif dir_first == 'NE' and dir_second == 'E':
			if x1 < x < x2 and y1 < y < y2 \
			and a1 < x < a2 and b1 == y:
				return True
		elif dir_first == 'NE' and dir_second == 'W':
			if x1 < x < x2 and y1 < y < y2 \
			and a2 < x < a1 and b1 == y:
				return True
		# ---- NW
		elif dir_first == 'NW' and dir_second == 'NE':
			if x2 < x < x1 and y1 < y < y2 \
			and a1 < x < a2 and b1 < y < y2:
				return True
		elif dir_first == 'NW' and dir_second == 'NW':
			if x2 < x < x1 and y1 < y < y2 \
			and a2 < x < a1 and b1 < y < y2:
				return True
		elif dir_first == 'NW' and dir_second == 'SE':
			if x2 < x < x1 and y1 < y < y2 \
			and a1 < x < a2 and b2 < y < y1:
				return True
		elif dir_first == 'NW' and dir_second == 'SW':
			if x2 < x < x1 and y1 < y < y2 \
			and a2 < x < a1 and b2 < y < y1:
				return True
		# -
		elif dir_first == 'NW' and dir_second == 'N':
			if x2 < x < x1 and y1 < y < y2 \
			and a1 == x and b1 < y < b2:
				return True
		elif dir_first == 'NW' and dir_second == 'S':
			if x2 < x < x1 and y1 < y < y2 \
			and a1 == x and b2 < y < b1:
				return True
		elif dir_first == 'NW' and dir_second == 'E':
			if x2 < x < x1 and y1 < y < y2 \
			and a1 < x < a2 and b1 == y:
				return True
		elif dir_first == 'NW' and dir_second == 'W':
			if x2 < x < x1 and y1 < y < y2 \
			and a2 < x < a1 and b1 == y:
				return True
		# ---- SE
		elif dir_first == 'SE' and dir_second == 'NE':
			if x1 < x < x2 and y2 < y < y1 \
			and a1 < x < a2 and b1 < y < b2:
				return True
		elif dir_first == 'SE' and dir_second == 'NW':
			if x1 < x < x2 and y2 < y < y1 \
			and a2 < x < a1 and b1 < y < b2:
				return True
		elif dir_first == 'SE' and dir_second == 'SE':
			if x1 < x < x2 and y2 < y < y1 \
			and a1 < x < a2 and b2 < y < b1:
				return True
		elif dir_first == 'SE' and dir_second == 'SW':
			if x1 < x < x2 and y2 < y < y1 \
			and a2 < x < a1 and b2 < y < b1:
				return True
		# -
		elif dir_first == 'SE' and dir_second == 'N':
			if x1 < x < x2 and y2 < y < y1 \
			and a1 == x and b1 < y < b2:
				return True
		elif dir_first == 'SE' and dir_second == 'S':
			if x1 < x < x2 and y2 < y < y1 \
			and a1 == x and b2 < y < b1:
				return True
		elif dir_first == 'SE' and dir_second == 'E':
			if x1 < x < x2 and y2 < y < y1 \
			and a1 < x < a2 and b1 == y:
				return True
		elif dir_first == 'SE' and dir_second == 'W':
			if x1 < x < x2 and y2 < y < y1 \
			and a2 < x < a1 and b1 == y:
				return True
		# ---- SW
		elif dir_first == 'SW' and dir_second == 'NE':
			if x2 < x < x1 and y2 < y < y1 \
			and a1 < x < a2 and b1 < y < b2:
				return True
		elif dir_first == 'SW' and dir_second == 'NW':
			if x2 < x < x1 and y2 < y < y1 \
			and a2 < x < a1 and b1 < y < b2:
				return True
		elif dir_first == 'SW' and dir_second == 'SE':
			if x2 < x < x1 and y2 < y < y1 \
			and a1 < x < a2 and b2 < y < b1:
				return True
		elif dir_first == 'SW' and dir_second == 'SW':
			if x2 < x < x1 and y2 < y < y1 \
			and a2 < x < a1 and b2 < y < b1:
				return True
		# -
		elif dir_first == 'SW' and dir_second == 'N':
			if x2 < x < x1 and y2 < y < y1 \
			and a1 == x and b1 < y < b2:
				return True
		elif dir_first == 'SW' and dir_second == 'S':
			if x2 < x < x1 and y2 < y < y1 \
			and a1 == x and b2 < y < b1:
				return True
		elif dir_first == 'SW' and dir_second == 'E':
			if x2 < x < x1 and y2 < y < y1 \
			and a1 < x < a2 and b1 == y:
				return True
		elif dir_first == 'SW' and dir_second == 'W':
			if x2 < x < x1 and y2 < y < y1 \
			and a2 < x < a1 and b1 == y:
				return True
		# ---- N
		elif dir_first == 'N' and dir_second == 'NE':
			if x1 == x and y1 < y < y2 \
			and a1 < x < a2 and b1 < y < b2:
				return True	
		elif dir_first == 'N' and dir_second == 'NW':
			if x1 == x and y1 < y < y2 \
			and a2 < x < a1 and b1 < y < b2:
				return True
		elif dir_first == 'N' and dir_second == 'SE':
			if x1 == x and y1 < y < y2 \
			and a1 < x < a2 and b2 < y < b1:
				return True
		elif dir_first == 'N' and dir_second == 'SW':
			if x1 == x and y1 < y < y2 \
			and a2 < x < a1 and b2 < y < b1:
				return True
		# --
		elif dir_first == 'N' and dir_second == 'N':
			if x1 == x and y1 < y < y2 \
			and a1 == x and b1 < y < b2:
				return True
		elif dir_first == 'N' and dir_second == 'S':
			if x1 == x and y1 < y < y2 \
			and a1 < x < a2 and b1 < y < b2:
				return True
		elif dir_first == 'N' and dir_second == 'E':
			if x1 == x and y1 < y < y2 \
			and a1 < x < a2 and b1 == y:
				return True
		elif dir_first == 'N' and dir_second == 'W':
			if x1 == x and y1 < y < y2 \
			and a2 < x < a1 and b1 == y:
				return True
		# ---- S
		elif dir_first == 'S' and dir_second == 'NE':
			if x1 == x and y2 < y < y1 \
			and a1 < x < a2 and b1 < y < b2:
				return True
		elif dir_first == 'S' and dir_second == 'NW':
			if x1 == x and y2 < y < y1 \
			and a2 < x < a1 and b1 < y < b2:
				return True
		elif dir_first == 'S' and dir_second == 'SE':
			if x1 == x and y2 < y < y1 \
			and a1 < x < a2 and b2 < y < b1:
				return True
		elif dir_first == 'S' and dir_second == 'SW':
			if x1 == x and y2 < y < y1 \
			and a2 < x < a1 and b2 < y < b1:
				return True
		# --
		elif dir_first == 'S' and dir_second == 'N':
			if x1 == x and y2 < y < y1 \
			and a1 == x and b1 < y < b2:
				return True
		elif dir_first == 'S' and dir_second == 'S':
			if x1 == x and y2 < y < y1 \
			and a1 == x and b2 < y < b1:
				return True
		elif dir_first == 'S' and dir_second == 'E':
			if x1 == x and y2 < y < y1 \
			and a1 < x < a2 and b1 == y:
				return True
		elif dir_first == 'S' and dir_second == 'W':
			if x1 == x and y2 < y < y1 \
			and a2 < x < a1 and b1 == y:
				return True
		# ---- E
		elif dir_first == 'E' and dir_second == 'NE':
			if x1 < x < x2 and y1 == y \
			and a1 < x < a2 and b1 < y < b2:
				return True
		elif dir_first == 'E' and dir_second == 'NW':
			if x1 < x < x2 and y1 == y \
			and a2 < x < a1 and b1 < y < b2:
				return True
		elif dir_first == 'E' and dir_second == 'SE':
			if x1 < x < x2 and y1 == y \
			and a1 < x < a2 and b2 < y < b1:
				return True
		elif dir_first == 'E' and dir_second == 'SW':
			if x1 < x < x2 and y1 == y \
			and a2 < x < a1 and b2 < y < b1:
				return True
		# --
		elif dir_first == 'E' and dir_second == 'N':
			if x1 < x < x2 and y1 == y \
			and a1 == x and b1 < y < b2:
				return True
		elif dir_first == 'E' and dir_second == 'S':
			if x1 < x < x2 and y1 == y \
			and a2 == x and b2 < y < b1:
				return True
		elif dir_first == 'E' and dir_second == 'E':
			if x1 < x < x2 and y1 == y \
			and a1 < x < a2 and b2 == y:
				return True
		elif dir_first == 'E' and dir_second == 'W':
			if x1 < x < x2 and y1 == y \
			and a2 < x < a1 and b2 == y:
				return True
		# ---- W
		elif dir_first == 'W' and dir_second == 'NE':
			if x2 < x < x1 and y1 == y \
			and a1 < x < a2 and b1 < y < b2:
				return True
		elif dir_first == 'W' and dir_second == 'NW':
			if x2 < x < x1 and y1 == y \
			and a2 < x < a1 and b1 < y < b2:
				return True
		elif dir_first == 'W' and dir_second == 'SE':
			if x2 < x < x1 and y1 == y \
			and a1 < x < a2 and b2 < y < b1:
				return True
		elif dir_first == 'W' and dir_second == 'SW':
			if x2 < x < x1 and y1 == y \
			and a2 < x < a1 and b2 < y < b1:
				return True
		# --
		elif dir_first == 'W' and dir_second == 'N':
			if x2 < x < x1 and y1 == y \
			and a1 == x and b1 < y < b2:
				return True
		elif dir_first == 'W' and dir_second == 'S':
			if x2 < x < x1 and y1 == y \
			and a2 == x and b2 < y < b1:
				return True
		elif dir_first == 'W' and dir_second == 'E':
			if x2 < x < x1 and y1 == y \
			and a1 < x < a2 and b1 == y:
				return True
		elif dir_first == 'W' and dir_second == 'W':
			if x2 < x < x1 and y1 == y \
			and a2 < x < a1 and b1 == y:
				return True

		return False
