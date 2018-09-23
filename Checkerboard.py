#A Board class. exactly 1 is instatiated per game. All tiles and Tori have references to it.
#Top left is (0, 0). Moving down increases the first value. Moving right increases the second.

from Piece import Piece
from Tile import Tile
from consts import *

class Checkerboard():
	def __init__(self):
		self.grid = []
		
		for y in range(boardHeight): #this outer loop creates the entire board
			self.grid.append([]) # create the "row" sub-arrays
			for x in range(boardWidth): #this inner loop creates each tile
				
				if (y%2==0 and x%2==0) or (y%2==1 and x%2==1): #determining tile color
					self.grid[y].append(Tile(y, x, "red", self))
				else:
					self.grid[y].append(Tile(y, x, "black", self))
				
				#the active color is the tile color that Pieces can move on.
				#We place Pieces initially here
				if self.grid[y][x].color == activeColor: 
					if(y < 3):
						self.grid[y][x].item = Piece(0, y, x, self) #top 3 rows of the board
					elif(y > 4):
						self.grid[y][x].item = Piece(1, y, x, self) #bottom three rows
