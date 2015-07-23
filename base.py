from kivy.core.window import Window


win_x = Window.size[0]
win_y = Window.size[1]

class Base(object):
	
	ALIVE = True
	LEVELS = [16, 25, 36, 49, 64]
	current_level = LEVELS[0]
	
	boxes = {}
	slices = []
	intersections = {}
	crosspoints = []
	points = ListProperty([500, 500])
	points2 = ListProperty([400, 400])
	prev_len = 0
	divisions = int(math.sqrt(current_level))
	solve = solve.Solve()
	beetles = []
