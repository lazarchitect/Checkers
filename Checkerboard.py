#A Board class. exactly 1 is instatiated per game. All tiles and Tori have references to it.
#Top left is (0, 0). Moving down increases the first value. Moving right increases the second.

from Piece import Piece
from Tile import Tile
from consts import *

class Checkerboard():
	def __init__(self):
		self.grid = []
		for y in range(boardHeight):
			self.grid.append([])
			for x in range(boardWidth):
				
				if (y%2==0 and x%2==0) or (y%2==1 and x%2==1):
					self.grid[y].append(Tile(y, x, "red", self))
				else:
					self.grid[y].append(Tile(y, x, "black", self))

				if self.grid[y][x].color == "red":
					if(y < 3):
						self.grid[y][x].item = Piece(0, y, x, self)
					elif(y > 4):
						self.grid[y][x].item = Piece(1, y, x, self)