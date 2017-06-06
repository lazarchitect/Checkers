import pygame

from Checkerboard import Checkerboard

from consts import *
from functs import *

pygame.init()
b = Checkerboard()

screen = pygame.display.set_mode(screensize)

ARIAL = pygame.font.SysFont("arial", 30)

#initialize the board state
draw_tiles(b, screen)
populateCheckers(b, screen)

#Intialize the "info zone"
drawInfoZone(b, screen)

currentTeam = 0 # 0 is red, 1 is black
gameOver = False

#Gameplay loop
while 1:

	updateInfoZone(b, screen, currentTeam)

	for event in pygame.event.get():
		if(pygame.mouse.get_pressed()[0]):

			unHighlightAll(b, screen)

			location = pygame.mouse.get_pos()
			y = int(location[1]/tileHeight)
			x = int(location[0]/tileWidth)
			
			if x >= boardWidth: #if they clicked on the infoZone
				break

			choiceTile = b.grid[y][x]
			if type(choiceTile.item).__name__ == "Piece" and choiceTile.item.team == currentTeam:
				selectedPiece = choiceTile.item

				#team 0 goes down. team 1 goes up.
				if selectedPiece.team == 0 or selectedPiece.king == True:
					validMove(b, screen, choiceTile, 1,  1) #down right
					validMove(b, screen, choiceTile, 1, -1) #down left

				if selectedPiece.team == 1 or selectedPiece.king == True:
					validMove(b, screen, choiceTile, -1,  1) #up right
					validMove(b, screen, choiceTile, -1, -1) #up left

				result = move(b, screen, choiceTile, currentTeam)
				
				#TODO: if selectedPiece arrived at a top or bottom and its not a king, MAKE IT SO.

				if result:
					#TODO: if they jumped, they go again (?)
					#else, do the following. 
					currentTeam = abs(1 - currentTeam)
					if endCheck():
						gameOver = True

		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_F4):
			exit()

	if(gameOver):
		break

#Game Over loop
displayResults(b, screen)
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_F4):
			exit()