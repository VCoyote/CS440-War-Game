#!/usr/bin/env python2
from game_board import Board
from render_game import render_game, pygame, clock, mouse_move, mouse_down, mouse_up
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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down(event.pos, board)
        elif event.type == pygame.MOUSEMOTION:
            mouse_move(event.pos, board)
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_up(event.pos, board)


    # if ai can make a move, do it
    if current_turn == 'blue':
        print('ai')
        move = calculate_abprune('blue', 'green', board)
        to_capture = move[1]

        board.capture(to_capture, team='blue')
        board.next_turn()

        # processing may take a while, so prevent a huge even queue from filling up
        pygame.event.clear()

    render_game(board)
	
    pygame.display.flip()
    clock.tick(30)
