class Piece():

	def __init__(self, team, y, x, b):
		
		self.team = team #gonna be 0 or 1
		self.x = x
		self.y = y
		#note that being next to a wall or edge will limit this list. or ally presence
		self.board = b
		self.king = False #at first
		self.imagePath = "redPiece.png" if self.team == 0 else "blackPiece.png"

	def __str__(self):
		return "red" if self.team == 0 else "black"



