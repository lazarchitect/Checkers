import pygame
pygame.font.init()
#This file defines some variables for use in the main program. 

#Tile dimensions, in pixels
tileWidth = 100
tileHeight = 100
tilesize = (tileWidth, tileHeight)

#Board space dimensions, in Tiles
boardWidth = 8
boardHeight = 8

#Screen dimensions, in pixels
screenWidth = tileWidth*boardWidth + 400
screenHeight = tileHeight*boardHeight
screensize = (screenWidth, screenHeight)

infoZoneLeft = tileWidth * boardWidth
infoZoneTop = 0 
infoZoneWidth = 400
infoZoneHeight = screenHeight

infoZoneRect = pygame.Rect(infoZoneLeft, infoZoneTop, infoZoneWidth, infoZoneHeight)

#COLORS
WHITE = (255, 255, 255)
BLACK = (0,0,0)

#FONTS
ARIAL = pygame.font.SysFont("arial", 30)

#Player Scores
player1Score = 12
player2Score = 12