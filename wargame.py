#!/usr/bin/env python2
from render_game import render_game, pygame, clock, mouse_move, mouse_down, mouse_up
from game_board import Board, BlitzError
from minimax import calculate_minimax
from abprune import calculate_abprune
from debug_ai import debug_ai
import sys, argparse

# constants
DEBUG_AI = False

# get board
args = argparse.ArgumentParser()
args.add_argument('-b', '--board', help='specify a custom board', type=str)
args = args.parse_args()

board_file = 'boards/Punxsutawney.txt'
if args.board:
    board_file = args.board

board = Board(board_file)
print(board)

if DEBUG_AI:
    # debug minimax
    debug_ai(board, calculate_minimax)

    # debug abpruning
    debug_ai(board, calculate_abprune)

while board.open:
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
        move = calculate_abprune('blue', 'green', board, 3)
        to_capture = move[1]

        try: 
            board.blitz(to_capture, current_turn)
        except BlitzError:
            board.drop(to_capture, current_turn)
        board.next_turn()

        # processing may take a while, so prevent a huge event queue from filling up
        pygame.event.clear()

    render_game(board)
	
    pygame.display.flip()
    clock.tick(30)

# let user see score until a button is pressed
pygame.event.set_blocked(pygame.MOUSEMOTION)
pygame.event.wait()
