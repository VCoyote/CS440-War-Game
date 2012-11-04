#!/usr/bin/env python2
from game_board import Board
from render_game import render_game, pygame, clock
from minimax import calculate_minimax
from copy import deepcopy

board = Board('boards/Punxsutawney.txt')
print(board)

print (calculate_minimax('green','blue',board, 0, 0,0,None))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    render_game(board)

    pygame.display.flip()
    clock.tick(30)
