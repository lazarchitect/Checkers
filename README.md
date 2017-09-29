# Checkers
Took a break from the Quadradius thing to throw this together. It's just checkers... for now.

After completing Song Guesser, I decided to dive into one of my favorite project types, board games. 
As a tutorial project for other things I want to make, I chose the simplest board game I could think of.

The game works by selecting the piece you want to move, and then selecting a valid tile to which that piece can move.
It looks at tiles diagonally forward, but if the piece is a King, it looks backward too.
If a destination has an enemy piece on it, the game examines the tile directly beyond for validity.

The game ends when a player has zero valid moves. The sidebar keeps track of the score.
