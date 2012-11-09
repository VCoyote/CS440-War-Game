#!/usr/bin/env python2
from game_board import Board, BlitzError
from render_game import render_game, pygame, clock
from minimax import calculate_minimax, return_nodes_this_time
from abprune import calculate_abprune, return_nodes_this_time_ab
from debug_ai import debug_ai
import sys, argparse, time

DEBUG_AI = False

# get board
args = argparse.ArgumentParser()
args.add_argument('-b', '--board', help='specify a custom board', type=str)
args = args.parse_args()

board_file = 'boards/Punxsutawney.txt'
if args.board:
    board_file = args.board

board = Board(board_file)
total_time = 0
print(board)
if DEBUG_AI:
    # debug minimax
    debug_ai(board, calculate_minimax)

    # debug abpruning
    debug_ai(board, calculate_abprune)
total_nodes = 0
nodes_this_time = 0
nodes_this_time_array = []
while board.open:
    current_turn = board.turn
    temp_time = time.clock()
    #for event in pygame.event.get():
    #    if event.type == pygame.QUIT:
    #        sys.exit()
    #    elif event.type == pygame.MOUSEBUTTONDOWN and event.button:
    #        click(event.pos, board)


    # if ai can make a move, do it
    if current_turn == 'blue':
        depth = 3
        move = calculate_abprune('blue', 'green', board)
        to_capture = move[1]

        try: 
            board.blitz(to_capture,current_turn)
        except BlitzError:
            board.drop(to_capture,current_turn)
        board.next_turn()
    else:
        depth = 3
        move = calculate_abprune('green', 'blue', board)
        to_capture = move[1]

        try: 
            board.blitz(to_capture,current_turn)
        except BlitzError:
            board.drop(to_capture,current_turn)
        board.next_turn()
    total_time += time.clock() - temp_time
    render_game(board)
    nodes_this_time = return_nodes_this_time_ab()
    nodes_this_time_array.append(nodes_this_time)
    total_nodes += nodes_this_time
    print str(nodes_this_time) + current_turn
	
    pygame.display.flip()
    clock.tick(30)
print total_time
print board.points
print total_nodes
print nodes_this_time_array

