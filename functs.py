import pygame
from consts import *
from random import randint

def draw_tiles(b, screen):
	
	for y in range(boardWidth):
		for x in range(boardHeight):
			TIQ = b.grid[y][x]
			color = TIQ.color
			img = pygame.image.load(color+"Tile.png")
			img = pygame.transform.scale(img, (tileWidth, tileHeight))
			screen.blit(img, (x*tileWidth, y*tileHeight))

	pygame.display.flip()
	
def populateCheckers(b, screen):	
	for y in range(boardHeight):
		for x in range(boardWidth):
			if b.grid[y][x].item != None:
				img = pygame.image.load(b.grid[y][x].item.imagePath)
				img = pygame.transform.scale(img, (tileWidth, tileHeight))
				screen.blit(img, (x*tileWidth, y*tileHeight))

	pygame.display.flip()	

def drawInfoZone(b, screen):
	pygame.draw.rect(screen, WHITE, infoZoneRect, 0)
	pygame.display.update(infoZoneRect)

def blitToScreen(b, screen, item, y, x):
	img = pygame.image.load(b.grid[y][x].item.imagePath)
	img = pygame.transform.scale(img, (tileWidth, tileHeight))
	screen.blit(img, (x*tileWidth, y*tileHeight))
	
#Given a tile's coordinates, makes it glow yellow
def	highlight(b, screen, y, x):

	TIQ = b.grid[y][x] #tile in question
	color = TIQ.color
	img = pygame.image.load(color+"TileHighlight.png")
	img = pygame.transform.scale(img, (tileWidth, tileHeight))
	screen.blit(img, (x*tileWidth, y*tileHeight))
	
	thing = b.grid[y][x].item
	if(thing != None):
		blitToScreen(b, screen, thing, y, x)
	pygame.display.flip()#update(pygame.Rect(x*tileWidth, y*tileHeight, tileWidth, tileHeight))
	b.grid[y][x].isHighlighted = True

#Shuts off all glowing tiles, wherever they might be. Might be more efficient to keep track of any highlited tiles instead of checking all
def unHighlightAll(b, screen):
	for y in range(boardHeight):
		for x in range(boardWidth):
			if(b.grid[y][x].isHighlighted == True):
				
				TIQ = b.grid[y][x] #tile in question

				tileImg = pygame.transform.scale(pygame.image.load(TIQ.color+"Tile.png"), (tileWidth, tileHeight))
				screen.blit(tileImg, (x*tileWidth, y*tileHeight))
				
				thing = TIQ.item
				if(thing != None):
					blitToScreen(b, screen, thing, y, x)
				
				pygame.display.update(pygame.Rect(x*tileWidth, y*tileHeight, tileWidth, tileHeight))
				
				TIQ.isHighlighted = False

#this method verifes if a Piece can move to it.
#Assuming the Piece is legally able to move in the direction defined by the offsets,
#this method checks if the Piece can move there or if it can jump an enemy there.
def validMove(b, screen, choiceTile, yOffset, xOffset):
	
	if choiceTile.x + xOffset < 0 or choiceTile.x + xOffset > 7 or choiceTile.y + yOffset < 0 or choiceTile.y + yOffset > 7:
		return
	destTile = b.grid[choiceTile.y + yOffset][choiceTile.x + xOffset]

	if destTile.item == None:
		highlight(b, screen, destTile.y, destTile.x)

	elif type(destTile.item).__name__ == "Piece" and choiceTile.item.team != destTile.item.team: #for jumping. the method now checks the space beyond the enemy tile.
		if xOffset < 0: 
			xOffset -=1
		else: 
			xOffset +=1
		if yOffset < 0: 
			yOffset -=1
		else: 
			yOffset +=1

		if choiceTile.x + xOffset < 0 or choiceTile.x + xOffset > 7 or choiceTile.y + yOffset < 0 or choiceTile.y + yOffset > 7:
			return
		destTile = b.grid[choiceTile.y + yOffset][choiceTile.x + xOffset]
		if destTile.item == None:
			highlight(b, screen, destTile.y, destTile.x)				

#Moves a torus from its current location to a desired adjacent Tile, GIVEN THAT THE DEST TILE IS VALID(HIGHLIGHTED). 
#Returns true if the move happened. False if not.
def move(b, screen, choiceTile, team):

	global player1Score
	global player2Score

	toMove = choiceTile.item

	#take new input. if THAT is on a highlighted tile, move the torus there, unhighlight all, return true. else, unhighlight all and return False
	while 1:
		for event in pygame.event.get():
			
			if(pygame.mouse.get_pressed()[0]):
			
				location = pygame.mouse.get_pos()
				y = int(location[1]/tileHeight)
				x = int(location[0]/tileWidth)

				if x >= boardWidth: 
					unHighlightAll(b, screen)
					return False

				destTile = b.grid[y][x]
				
				if(destTile.isHighlighted == True): #this means the move goes through
					
					# if the offset was 2, remove the jumped Piece and change the score.
					# get the average of choiceTile.x and destTile.x, same for y, and set the tile at that coord pair's item to None. and then clean it.
					# before u kill it, get the team and lower that team's score by 1.

					if abs(destTile.x - choiceTile.x) == 2: #a jump has occurred
						
						deadPieceY = int((destTile.y + choiceTile.y)/2)
						deadPieceX = int((destTile.x + choiceTile.x)/2)
						
						deadPieceTile = b.grid[deadPieceY][deadPieceX]
						deadPiece = deadPieceTile.item
						
						deadPieceTile.item = None
						if deadPiece.team == 0:
							player1Score-=1
						else:
							player2Score-=1

						deadTileImg = pygame.transform.scale(pygame.image.load(deadPieceTile.color+"Tile.png"), (tileWidth, tileHeight))
						screen.blit(deadTileImg, (deadPieceX*tileWidth, deadPieceY*tileHeight))
						pygame.display.update(pygame.Rect(deadPieceX*tileWidth, deadPieceY*tileHeight, tileWidth, tileHeight))



					choiceTile.item.y = destTile.y
					choiceTile.item.x = destTile.x ####ehhh???? The purpose of this is for easy access to row and col for abilities. not sure if it works yet

					#Also, not sure if changing Tile references here is good...
					destTile.item = choiceTile.item

					#this block deals with the Ascension of Kings
					moveGuy = destTile.item
					if moveGuy.team == 0 and destTile.y == 7:
						moveGuy.king = True
						moveGuy.imagePath = "redKing.png"
					
					elif moveGuy.team == 1 and destTile.y == 0:
						moveGuy.king = True
						moveGuy.imagePath = "blackKing.png"
					
					blitToScreen(b, screen, destTile.item, destTile.y, destTile.x)
					


					choiceTile.item = None
					color = choiceTile.color
					img = pygame.image.load(color+"Tile.png")
					img = pygame.transform.scale(img, (tileWidth, tileHeight))
					screen.blit(img, (choiceTile.x*tileWidth, choiceTile.y*tileHeight))
					pygame.display.flip()
					unHighlightAll(b, screen)


					#the logic for kings SHOULD BE already taken care of but graphics are not	

					return True

				else:
					unHighlightAll(b, screen)
					return False

			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_F4):
				exit()

#Each turn, tell the player that its their turn.
#Other tasks: display available powers, chatbox, FF button
def updateInfoZone(b, screen, currentTeam):

	global player1Score
	global player2Score

	pygame.draw.rect(screen, WHITE, infoZoneRect)
	screen.blit(ARIAL.render("Player " + str(currentTeam + 1) + ", Your Turn", 0, BLACK), (infoZoneLeft+35, infoZoneTop))

	screen.blit(ARIAL.render("Player 1's Score: " + str(player1Score), 0, BLACK), (infoZoneLeft+35, infoZoneTop + 100))
	screen.blit(ARIAL.render("Player 2's Score: " + str(player2Score), 0, BLACK), (infoZoneLeft+35, infoZoneTop + 130))

	pygame.display.update(infoZoneRect)



#Should notify the winner if they destroyed all enemy pieces. A tie is also possible.
#returns true if the game is over, and false if not.
#if this returns true, break the game loop.
def endCheck():
	
	global player1Score
	global player2Score

	if player2Score == 0 or player1Score == 0:
		return True
	
	return False	


def displayResults(b, screen):
	
	global player1Score
	global player2Score

	pygame.draw.rect(screen, WHITE, infoZoneRect)
	
	if(player1Score == 0 and player2Score == 0):
		screen.blit(ARIAL.render("It's a Tie!", 0, BLACK), (infoZoneLeft+35, infoZoneTop)) #Impossible to get a tie without the Kamikaze or Bombs powers
	elif(player1Score == 0):
		screen.blit(ARIAL.render("Player 2 Wins!", 0, BLACK), (infoZoneLeft+35, infoZoneTop))
	elif(player2Score == 0):
		screen.blit(ARIAL.render("Player 1 Wins!", 0, BLACK), (infoZoneLeft+35, infoZoneTop))

	pygame.display.update(infoZoneRect)

