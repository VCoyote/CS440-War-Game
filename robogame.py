#!/usr/bin/env python2
from game_board import Board, BlitzError
from render_game import render_game, pygame, clock, click
from minimax import calculate_minimax
from abprune import calculate_abprune
from debug_ai import debug_ai
import sys

DEBUG_AI = False

board = Board('boards/Punxsutawney.txt')
print(board)

if DEBUG_AI:
    # debug minimax
    debug_ai(board, calculate_minimax)

    # debug abpruning
    debug_ai(board, calculate_abprune)

while True:
    current_turn = board.turn

    #for event in pygame.event.get():
    #    if event.type == pygame.QUIT:
    #        sys.exit()
    #    elif event.type == pygame.MOUSEBUTTONDOWN and event.button:
    #        click(event.pos, board)


    # if ai can make a move, do it
    if current_turn == 'blue':
        depth = 5 - (len(board.open)/10)
        move = calculate_abprune('blue', 'green', board, depth )
        to_capture = move[1]

        try: 
            board.blitz(to_capture,current_turn)
        except BlitzError:
            board.drop(to_capture,current_turn)
        board.next_turn()
    else:
        depth = 5 - (len(board.open)/10)
        move = calculate_abprune('green', 'blue', board, depth)
        to_capture = move[1]

        try: 
            board.blitz(to_capture,current_turn)
        except BlitzError:
            board.drop(to_capture,current_turn)
        board.next_turn()

    render_game(board)
	
    pygame.display.flip()
    clock.tick(300)
