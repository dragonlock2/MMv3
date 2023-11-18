# Flood Fill algorithm based on https://github.com/bblodget/MicromouseSim
# Simulates mouse used in DeCal with angled sensors
# Written by Matthew Tran

import turtle, sys

CANVAS_BUFFER = 30
BOX_SIZE = 32

class Maze():
	def __init__(self, filename):
		self.readMaze(filename)
		self.checkMaze()
		self.setupCanvas()
		self.drawMaze()

	def readMaze(self, filename):
		f = open(filename, "r")
		self.maze = []
		for l in f.readlines():
			self.maze.append([int(i) for i in l.split()])
		self.maze = self.maze[::-1]
		self.MAZE_WIDTH = len(self.maze[0])
		self.MAZE_HEIGHT = len(self.maze)
		self.maze = [[self.maze[y][x] for y in range(self.MAZE_HEIGHT)] for x in range(self.MAZE_WIDTH)] #swap indices so maze[x][y]
		f.close()

	def checkMaze(self):
		flag = True
		for x in range(self.MAZE_WIDTH):
			for y in range(self.MAZE_HEIGHT):
				s = Maze.getWalls(self.maze[x][y])
				if (s[0] != Maze.getWalls(self.maze[x][(y+1)%self.MAZE_HEIGHT])[2]):
					flag = False
					print(x, y, "'s north IS WRONG")
				if (s[1] != Maze.getWalls(self.maze[(x+1)%self.MAZE_WIDTH][y])[3]):
					flag = False
					print(x, y, "'s east IS WRONG")
				if (s[2] != Maze.getWalls(self.maze[x][y-1])[0]):
					flag = False
					print(x, y, "'s south IS WRONG")
				if (s[3] != Maze.getWalls(self.maze[x-1][y])[1]):
					flag = False
					print(x, y, "'s west IS WRONG!")
		if flag:
			print("Maze file correct!")

	def setupCanvas(self):
		screenWidth = self.MAZE_WIDTH*BOX_SIZE + 2*CANVAS_BUFFER
		screenHeight = self.MAZE_HEIGHT*BOX_SIZE + 2*CANVAS_BUFFER
		axisOffset = -CANVAS_BUFFER - BOX_SIZE//2
		turtle.colormode(255)
		turtle.speed(0)
		turtle.delay(0)
		turtle.screensize(screenWidth, screenHeight)
		turtle.setworldcoordinates(axisOffset, axisOffset, screenWidth + axisOffset, screenHeight + axisOffset)

	def drawMaze(self):
		turtle.tracer(0, 0)
		for x in range(self.MAZE_WIDTH):
			for y in range(self.MAZE_HEIGHT):
				self.drawCell(x-0.5, y-0.5, Maze.getWalls(self.maze[x][y]))
		turtle.setpos(0, 0)
		turtle.setheading(90)
		turtle.update()
		turtle.tracer(1, 0)

	def drawCell(self, x, y, s):
		turtle.up()
		turtle.setpos(BOX_SIZE*x, BOX_SIZE*(y+1))
		turtle.setheading(0)
		for i in range(4):
			if (s[i]):
				turtle.down()
			turtle.forward(BOX_SIZE)
			turtle.right(90)
			turtle.up()

	def drawPath(self, path, color):
		if len(path) == 0:
			return
		turtle.color(color)
		turtle.up()
		turtle.setpos(path[0][0]*BOX_SIZE, path[0][1]*BOX_SIZE)
		turtle.down()
		for pos in path:
			x, y = pos[0]*BOX_SIZE, pos[1]*BOX_SIZE
			turtle.setheading(turtle.towards(x, y))
			turtle.setpos(x, y)
		turtle.color("black")

	def dijkstras(self, src, tar):
		paths = {}
		dists = {(src[0],src[1]):0}
		PQ = dists.copy()
		#perform dijkstras
		while len(PQ) != 0:
			# pop off PQ
			curr = min(PQ, key=lambda x: PQ[x])
			if curr == tar:
				break
			dist = PQ.pop(curr)
			# find neighbors
			walls = Maze.getWalls(self.maze[curr[0]][curr[1]])
			neighbors = []
			if not walls[0]:
				neighbors.append((curr[0], curr[1]+1))
			if not walls[1]:
				neighbors.append((curr[0]+1, curr[1]))
			if not walls[2]:
				neighbors.append((curr[0], curr[1]-1))
			if not walls[3]:
				neighbors.append((curr[0]-1, curr[1]))
			# relax all edges
			for n in neighbors:
				ndist = dists.setdefault(n, sys.maxsize)
				if dist + 1 < ndist:
					paths.setdefault(n, curr)
					dists[n] = dist + 1
					PQ.update({n:dist+1})
		# return paths
		p = []
		node = tar
		while node != src:
			p.append(node)
			node = paths[node]
		p.append(src)
		return p[::-1]

	def getCenters(self):
		c = [(self.MAZE_WIDTH//2, self.MAZE_HEIGHT//2)]
		if (self.MAZE_WIDTH % 2 == 0):
			c.append((c[0][0] - 1, c[0][1]))
		if (self.MAZE_HEIGHT % 2 == 0):
			c.append((c[0][0], c[0][1] - 1))
		if (self.MAZE_WIDTH % 2 == 0 and self.MAZE_HEIGHT % 2 == 0):
			c.append((c[0][0] - 1, c[0][1] - 1))
		return c

	# Static helper methods
	def manhattanDist(src, tar):
		return abs(src[0] - tar[0]) + abs(src[1] - tar[1])

	# 8 = North, 4 = East, 2 = South, 1 = West
	def getWalls(x):
		return (bool(x&8), bool(x&4), bool(x&2), bool(x&1))

class Karel():
	def __init__(self, maze):
		turtle.up()
		turtle.setheading(90)
		turtle.setpos(0, 0)
		turtle.color("black")
		self.x, self.y, self.dir, self.maze = 0, 0, 0, maze
		self.map = [[0 for i in range(maze.MAZE_HEIGHT)] for j in range(maze.MAZE_WIDTH)]
		self.recon = [[0 for i in range(maze.MAZE_HEIGHT)] for j in range(maze.MAZE_WIDTH)]
		self.gather()

	# Sensors
	def openFront(self):
		return not Maze.getWalls(self.maze.maze[self.x][self.y])[self.dir]

	# There are edges cases where including this is slower, but on average, its better
	def openFarFront(self):
		if not self.openFront():
			return True
		neighs = [(self.x, self.y+1), (self.x+1, self.y), (self.x, self.y-1), (self.x-1, self.y)]
		n = neighs[self.dir]
		return not Maze.getWalls(self.maze.maze[n[0]][n[1]])[self.dir]

	def openFrontLeft(self):
		if not self.openFront():
			return True
		neighs = [(self.x, self.y+1), (self.x+1, self.y), (self.x, self.y-1), (self.x-1, self.y)]
		n = neighs[self.dir]
		return not Maze.getWalls(self.maze.maze[n[0]][n[1]])[(self.dir-1)%4]

	def openFrontRight(self):
		if not self.openFront():
			return True
		neighs = [(self.x, self.y+1), (self.x+1, self.y), (self.x, self.y-1), (self.x-1, self.y)]
		n = neighs[self.dir]
		return not Maze.getWalls(self.maze.maze[n[0]][n[1]])[(self.dir+1)%4]

	# Movement
	def turnLeft(self):
		turtle.left(90)
		self.dir = (self.dir - 1) % 4
		self.gather()

	def turnRight(self):
		turtle.right(90)
		self.dir = (self.dir + 1) % 4
		self.gather()

	def forward(self):
		turtle.forward(BOX_SIZE)
		if self.dir == 0:
			self.y += 1
		elif self.dir == 1:
			self.x += 1
		elif self.dir == 2:
			self.y -= 1
		else: # self.dir == 3
			self.x -= 1
		self.gather()

	def gather(self): # note Arduino mod leaves negatives so need to fix that
		myUpdates, neighUpdates = (8, 4, 2, 1), (2, 1, 8, 4)
		neighs = [(self.x, self.y+1), (self.x+1, self.y), (self.x, self.y-1), (self.x-1, self.y)]
		n = neighs[self.dir]
		x, y = n
		neighneighs = [(x, y+1), (x+1, y), (x, y-1), (x-1, y)]
		if not self.openFront():
			self.recon[self.x][self.y] |= myUpdates[self.dir]
			if self.isValid(n):
				self.recon[n[0]][n[1]] |= neighUpdates[self.dir]
		if not self.openFarFront():
			nn = neighneighs[self.dir]
			if self.isValid(nn):
				self.recon[nn[0]][nn[1]] |= neighUpdates[self.dir]
		if not self.openFrontLeft():
			leftDir = (self.dir - 1) % 4
			self.recon[x][y] |= myUpdates[leftDir]
			nn = neighneighs[leftDir]
			if self.isValid(nn):
				self.recon[nn[0]][nn[1]] |= neighUpdates[leftDir]
		if not self.openFrontRight():
			rightDir = (self.dir + 1) % 4
			self.recon[x][y] |= myUpdates[rightDir]
			nn = neighneighs[rightDir]
			if self.isValid(nn):
				self.recon[nn[0]][nn[1]] |= neighUpdates[rightDir]

	def isValid(self, src):
		return src[0] >= 0 and src[0] < self.maze.MAZE_WIDTH and src[1] >= 0 and src[1] < self.maze.MAZE_HEIGHT

	# Algorithms

	# normal flood fill, assuming starting at (0, 0) and target center, and even maze dimensions
	def solveMazeFloodFill(self):
		# Given that we start with walls on right, left, and back
		self.recon[0][0] = 7

		# 1st run
		turtle.color("red")
		turtle.down()
		x = self.floodFillHelper(True)
		turtle.up()
		y = self.floodFillHelper(False)
		print("1st run - To: {}, From: {}".format(x, y))

		# 2nd run
		turtle.color("green")
		turtle.down()
		x = self.floodFillHelper(True)
		turtle.up()
		y = self.floodFillHelper(False)
		print("2nd run - To: {}, From: {}".format(x, y))

		#3rd run
		turtle.color("blue")
		turtle.down()
		x = self.floodFillHelper(True)
		turtle.up()
		y = self.floodFillHelper(False)
		print("3rd run - To: {}, From: {}".format(x, y))

		#4th run
		turtle.color("cyan")
		turtle.down()
		x = self.floodFillHelper(True)
		print("4th run - To: {}".format(x))
		turtle.up()

	def floodFillHelper(self, toCenter):
		l = 0
		self.floodFillUpdate(toCenter)
		while self.map[self.x][self.y] != 0:
			self.floodFillUpdate(toCenter)
			self.moveMin()
			l += 1
		return l

	def floodFillUpdate(self, toCenter): # some stacks, should optimize this, I believe it double counts a lot
		currentLevel, nextLevel = [], []
		for i in range(self.maze.MAZE_WIDTH):
			for j in range(self.maze.MAZE_HEIGHT):
				self.map[i][j] = sys.maxsize
		if toCenter:
			halfX, halfY = (self.maze.MAZE_WIDTH // 2) - 1, (self.maze.MAZE_HEIGHT // 2) - 1
			currentLevel.append((halfX, halfY))
			currentLevel.append((halfX+1, halfY))
			currentLevel.append((halfX, halfY+1))
			currentLevel.append((halfX+1, halfY+1))
		else:
			currentLevel.append((0,0))
		level = 0
		while True:
			while currentLevel:
				curr = currentLevel.pop()
				cd = self.map[curr[0]][curr[1]]
				if cd == sys.maxsize:
					self.map[curr[0]][curr[1]] = level
					x, y = curr
					o = Maze.getWalls(self.recon[x][y])
					neighs = [(x, y+1), (x+1, y), (x, y-1), (x-1, y)]
					for i in range(4):
						if self.isValid(neighs[i]) and not o[i]:
							nextLevel.append(neighs[i])
			if nextLevel:
				level += 1
				currentLevel = nextLevel
				nextLevel = []
			else:
				break

	def moveMin(self):
		d = [sys.maxsize] * 4
		w = Maze.getWalls(self.recon[self.x][self.y])
		neighs = [(self.x, self.y+1), (self.x+1, self.y), (self.x, self.y-1), (self.x-1, self.y)]
		for i in range(4):
			di = (self.dir + i) % 4
			n = neighs[di]
			if self.isValid(n) and not w[di]:
				d[i] = self.map[n[0]][n[1]]
		i = 0
		for j in range(4):
			if d[j] < d[i]:
				i = j
		if i == 0:
			self.forward()
		elif i == 1:
			self.turnRight()
			self.forward()
		elif i == 2:
			self.turnRight()
			self.turnRight()
			self.forward()
		else: # d == 3
			self.turnLeft()
			self.forward()

m = Maze(sys.argv[1])

if len(sys.argv) == 3:
	turtle.tracer(0, 0)

p = min([m.dijkstras((0,0), c) for c in m.getCenters()])
m.drawPath(p, (121, 252, 121))
print("Dijkstas:", len(p) - 1)

k = Karel(m)
k.solveMazeFloodFill()

if len(sys.argv) == 3:
	turtle.update()
	turtle.tracer(1, 0)

input("Press enter to continue...")