'''
Calculate the crosspoints of lines.

TODO:
- neke tacke preseka fale
'''
from kivy.core.window import Window
import part_of


win_x = Window.size[0]
win_y = Window.size[1]

# calculations for determining the interesctions between all the existing lines.
class Solve(object):

	crosspoints = []
	memo = []
	part_of = part_of.PartOf()
	total = 0

	def collect(self, points):
		#print('len(points)', len(points))
		if len(points) >= 8:

			i = 0
			j = i + 2
			
			while i <= len(points) - 5:
				while j <= len(points) - 3:
					if len(self.memo) != 0:

						if [i, j] in self.memo:
							#print "not unique intersection point"
							#print "self.memo:", self.memo
							#print "self.memo[k][0], self.memo[k][1]:", self.memo[k][0], self.memo[k][1]
							#print "i, j:", i, j
							#print "points length:", len(points)
							#print "i:", i
							#print "j:", j
							pass
						else:
							#print "new lines evaluated"
							#print "self.memo:", self.memo
							#print "self.memo[k][0], self.memo[k][1]:", self.memo[k][0], self.memo[k][1]
							#print "i, j:", i, j
							#print "points length:", len(points)
							#print "i:", i
							#print "j:", j
							self.intersection(
								points[i],
								points[i+1],
								points[i+2],
								points[i+3],
								points[j],
								points[j+1],
								points[j+2],
								points[j+3],
								i, j
								)

					else:
						#print "i:", i
						#print "j:", j
						self.intersection(
							points[i],
							points[i+1],
							points[i+2],
							points[i+3],
							points[j],
							points[j+1],
							points[j+2],
							points[j+3],
							i, j
							)
					j += 2
				i += 2
				j = i + 2

	# do the math. build equations for lines and solve them for each couple of lines.
	def intersection(self, x1, y1, x2, y2, a1, b1, a2, b2, i, j):

		#print "x1, y1, x2, y2: ",  x1, y1, x2, y2
		#print "a1, b1, a2, b2: ", a1, b1, a2, b2

		# just helper vars
		i1 = y1 - y2
		j1 = x1 - x2
		i2 = b1 - b2
		j2 = a1 - a2

		# figure out the slopes
		m1 = 0
		m2 = 0
		if j1 != 0:  # escape division by zero exception
			m1 = round(i1 / float(j1), 2)
		if j2 != 0:
			m2 = round(i2 / float(j2), 2)

		# another helper var
		m_dif = m1 - m2
		#print "m1, m2, m_dif", m1, m2, m_dif

		# figure out x and y
		x = 0
		if m_dif != 0:
			x = ((m1*x1) - (m2*a1) + b1 - y1) / float(m_dif)
		y = (m1*x) - (m1*x1) + y1

		# round them up
		x = round(x, 2)
		y = round(y, 2)
		#print "intersection point, x, y", x, y

		# if the intersection is anywhere on the lines themselves, include the intersection
		if x > 0 and y > 0 and x < win_x and y < win_y:  # and x != x1 and x != a1 and x != x2 and x != a2:
			#print "intersection point, x, y", x, y
			#self.crosspoints.append([x, y])
			#print "x1, x2, y1, y2, a1, a2, b1, b2, x, y"
			#print x1, x2, y1, y2, a1, a2, b1, b2, x, y
			
			if self.part_of.part_of(x1, y1, x2, y2, a1, b1, a2, b2, x, y):
				#print "crosspoint acknowledged", self.total
				self.crosspoints.append([x, y])
				#print('crosspoints', self.crosspoints)
				self.memo.append([i, j])
				#print("self.memo", self.memo)
				#self.total += 1
			else:
				self.memo.append([i, j])

	def clear(self):
		del self.crosspoints[:]
		del self.memo[:]
		self.total = 0
