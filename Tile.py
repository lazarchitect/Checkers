#A class representing a tile on the board. 
#Mostly a way to keep track of data. Tiles don't do anything, per se. They just have things happen to them.

class Tile():
	def __init__(self, y, x, color, b):
		self.item = None
		self.x = x#location never gets changed but keeping a reference seems useful...
		self.y = y
		self.board = b
		self.color = color
		self.isHighlighted = False #This is true if the til is a valid move destination for the chosen torus, and false otherwise