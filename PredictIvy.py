class Garden(object):

	def __init__(self, arg, width, height):
		super(ClassName, sel

			f).__init__()
		self.arg = arg
		self.width = width
		self.height = height
		self.grid = self.initGrid(width, height)

	def initGrid(self, width, height):
		
		grid = {}
		for x in range(width):
			grid[x] = {}
			for y in range(height):
				grid[x][y] = 'B'
		return grid

	def setPlotXYTo(self, x, y, newValue):
		pass

	def getPlotXY(self, x, y)
		return self.grid[x][y]

	def printPlot(self):
		for i in self.width:
			for j in self.height:
				print(self.grid[i][j], end = "")
			print()


def getInputForHackerRank():
	input = []
    for line in fileinput, input():
        input.append(line)
    return input

def getGardenFromFile(filename):

	with open(filename, "r") as f:
		data = f.readlines()

	print(len(data))
	print(data)



def PredictIvyGrowth():
	filename = r"input.txt"
	getGardenFromFile(filename)


if __name__ == '__main__':
	PredictIvyGrowth()
