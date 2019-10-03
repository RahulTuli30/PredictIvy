DELIMITER = ","

class Garden(object):

	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.grid = self.initGrid(width, height)
	
	def __str__(self):
		garden = []
		for i in range(self.width):
			garden.append("".join([self.grid[i][j] for j in range(self.height)]))
		garden = "\n".join(garden) 	
		return garden
	
	def initGrid(self, width, height):
		
		grid = {}
		for x in range(width):
			grid[x] = {}
			for y in range(height):
				grid[x][y] = 'B'
		return grid

	def setPlotXYTo(self, x, y, newValue):
		 if self.grid[x][y] == 'B':
		 	self.grid[x][y] = newValue
		 else:
		 	self.done()

	def getPlotXY(self, x, y):
		return self.grid[x][y]
		
def getInstructions(config):
	instructions = []
	for elem in config:
		instructions.append(elem.split(DELIMITER))
	return instructions


def updateGarden(garden, config):
	instructions = getInstructions(config)
	executeInstructionsOnGarden(garden, instructions)

def executeInstructionsOnGarden(garden,instructions):
	for instruction in instructions:
		if instruction[0].isalpha():
			garden.setPlotXYTo(x=int(instruction[1]), y=int(instruction[2]), newValue=instruction[0])

def getGardenFromFile(filename):
	data = readFile(filename)
	width, height=getWidthAndHeight(data)
	data = data[1:] #removing first line  
	garden = Garden(width, height)
	updateGarden(garden, data)
	return garden


def readFile(filename):
	with open(filename, "r") as f:
		data = f.readlines()
	return data

def getWidthAndHeight(data):
	first_line = data[0]
	width, height = (int(i) for i in first_line.strip().split(DELIMITER))
	#print(width, height)
	return width, height

def PredictIvyGrowth():
	filename = r"input.txt"
	garden = getGardenFromFile(filename)
	print(garden)


if __name__ == '__main__':
	PredictIvyGrowth()
