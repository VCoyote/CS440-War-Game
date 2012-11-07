#!/usr/bin/env python2
from game_board import Board
from render_game import render_game, pygame, clock, click
from minimax import calculate_minimax
from abprune import calculate_abprune
from debug_ai import debug_ai

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
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button:
            click(event.pos, board)


    # if ai can make a move, do it
    if current_turn == 'blue':
        move = calculate_abprune('blue', 'green', board)
        to_capture = move[1]

        board.capture(to_capture, team='blue')
        board.next_turn()

    render_game(board)
	
    pygame.display.flip()
    clock.tick(30)
