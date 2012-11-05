#!/usr/bin/env python2
from game_board import Board
from render_game import render_game, pygame, clock
from minimax import calculate_minimax
from abprune import calculate_abprune
from copy import deepcopy
from datetime import datetime

board = Board('boards/Punxsutawney.txt')
print(board)

max_team = 'green'
min_team = 'blue'
prune = None

a = datetime.now()
while len(board.open):
    result = calculate_minimax(max_team,min_team,board, 0, None)
    print result
    x = result[1][0]
    y = result[1][1]
    board.board[y][x].team = 'green'
    board.capture((x,y))
    board.greenpoints += board.board[y][x].value
    for neighbor in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if neighbor[0] < 5 and neighbor[0] >=0 and neighbor[1] <5 and neighbor[1] >=0:
            t = board.square_at(neighbor)
            if t.team == 'green':       
                for neighbor in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                    if neighbor[0] < 5 and neighbor[0] >=0 and neighbor[1] <5 and neighbor[1] >=0:
                        temp = board.square_at(neighbor)
                        if temp.team == 'blue':
                            temp.team = 'green'
                            board.greenpoints += temp.value
                            board.bluepoints -= temp.value
                break
    print str(board.greenpoints) + '%' + str(board.bluepoints)
    print board
    
    
    
    if not len(board.open):
        break;

    result = calculate_minimax(min_team,max_team,board, 0, None)
    print result
    x = result[1][0]
    y = result[1][1]
    board.board[y][x].team = 'blue'
    board.capture((x,y))
    board.bluepoints += board.board[y][x].value
    for neighbor in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if neighbor[0] < 5 and neighbor[0] >=0 and neighbor[1] <5 and neighbor[1] >=0:
            t = board.square_at(neighbor)
            if t.team == 'blue':       
                for neighbor in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                    if neighbor[0] < 5 and neighbor[0] >=0 and neighbor[1] <5 and neighbor[1] >=0:
                        temp = board.square_at(neighbor)
                        if temp.team == 'green':
                            temp.team = 'blue'
                            board.bluepoints += temp.value
                            board.greenpoints -= temp.value
                break
    print str(board.greenpoints) + '%' + str(board.bluepoints)
    print board

b = datetime.now() - a
print str(b.seconds) + 'seconds'
board = Board('boards/Punxsutawney.txt')
print(board)

max_team = 'green'
min_team = 'blue'
prune = None

a = datetime.now()
while  len(board.open):
    print len(board.open)
    result = calculate_abprune(max_team,min_team,board, 0, None)
    print result
    x = result[1][0]
    y = result[1][1]
    board.board[y][x].team = 'green'
    board.capture((x,y))
    board.greenpoints += board.board[y][x].value
    for neighbor in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if neighbor[0] < 5 and neighbor[0] >=0 and neighbor[1] <5 and neighbor[1] >=0:
            t = board.square_at(neighbor)
            if t.team == 'green':       
                for neighbor in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                    if neighbor[0] < 5 and neighbor[0] >=0 and neighbor[1] <5 and neighbor[1] >=0:
                        temp = board.square_at(neighbor)
                        if temp.team == 'blue':
                            temp.team = 'green'
                            board.greenpoints += temp.value
                            board.bluepoints -= temp.value
                break
    print str(board.greenpoints) + '%' + str(board.bluepoints)
    print board
    if not len(board.open):
        break;
    result = calculate_abprune(min_team,max_team,board, 0, None)
    print result
    x = result[1][0]
    y = result[1][1]
    board.board[y][x].team = 'blue'
    board.capture((x,y))
    board.bluepoints += board.board[y][x].value
    for neighbor in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if neighbor[0] < 5 and neighbor[0] >=0 and neighbor[1] <5 and neighbor[1] >=0:
            t = board.square_at(neighbor)
            if t.team == 'blue':       
                for neighbor in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                    if neighbor[0] < 5 and neighbor[0] >=0 and neighbor[1] <5 and neighbor[1] >=0:
                        temp = board.square_at(neighbor)
                        if temp.team == 'green':
                            temp.team = 'blue'
                            board.bluepoints += temp.value
                            board.greenpoints -= temp.value
                break
    print str(board.greenpoints) + '%' + str(board.bluepoints)
    print board

b = datetime.now()-a
print str(b.seconds) + 'seconds'
    
while False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    render_game(board)

    pygame.display.flip()
    clock.tick(30)
