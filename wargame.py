#!/usr/bin/env python2
from game_board import Board
from render_game import render_game, pygame, clock
from minimax import calculate_minimax
from abprune import calculate_abprune
from copy import deepcopy

board = Board('boards/Punxsutawney.txt')
print(board)

max_team = 'green'
min_team = 'blue'
max_score = 0
min_score = 0
prune = None


while not len(board.open):
    print len(board.open)
    result = calculate_minimax(max_team,min_team,board, 0, max_score, min_score, None)
    print result
    x = result[1][0]
    y = result[1][1]
    board.board[y][x].team = 'green'
    board.capture((x,y))
    max_score += board.board[y][x].value
    for neighbor in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if neighbor[0] < 5 and neighbor[0] >=0 and neighbor[1] <5 and neighbor[1] >=0:
            t = board.square_at(neighbor)
            if t.team == 'green':       
                for neighbor in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                    if neighbor[0] < 5 and neighbor[0] >=0 and neighbor[1] <5 and neighbor[1] >=0:
                        temp = board.square_at(neighbor)
                        if temp.team == 'blue':
                            temp.team = 'green'
                            max_score += temp.value
                            min_score -= temp.value
                break
    print board
    if not len(board.open):
        break;
    result = calculate_minimax(min_team,max_team,board, 0, min_score, max_score, None)
    print result
    x = result[1][0]
    y = result[1][1]
    board.board[y][x].team = 'blue'
    board.capture((x,y))
    min_score += board.board[y][x].value
    for neighbor in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if neighbor[0] < 5 and neighbor[0] >=0 and neighbor[1] <5 and neighbor[1] >=0:
            t = board.square_at(neighbor)
            if t.team == 'blue':       
                for neighbor in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                    if neighbor[0] < 5 and neighbor[0] >=0 and neighbor[1] <5 and neighbor[1] >=0:
                        temp = board.square_at(neighbor)
                        if temp.team == 'green':
                            temp.team = 'blue'
                            min_score += temp.value
                            max_score -= temp.value
                break
    print board

while len(board.open):
    print len(board.open)
    result = calculate_abprune(max_team,min_team,board, 0, max_score, min_score, None)
    print result
    x = result[1][0]
    y = result[1][1]
    board.board[y][x].team = 'green'
    board.capture((x,y))
    max_score += board.board[y][x].value
    for neighbor in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if neighbor[0] < 5 and neighbor[0] >=0 and neighbor[1] <5 and neighbor[1] >=0:
            t = board.square_at(neighbor)
            if t.team == 'green':       
                for neighbor in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                    if neighbor[0] < 5 and neighbor[0] >=0 and neighbor[1] <5 and neighbor[1] >=0:
                        temp = board.square_at(neighbor)
                        if temp.team == 'blue':
                            temp.team = 'green'
                            max_score += temp.value
                            min_score -= temp.value
                break
    print board
    if not len(board.open):
        break;
    result = calculate_abprune(min_team,max_team,board, 0, min_score, max_score, None)
    print result
    x = result[1][0]
    y = result[1][1]
    board.board[y][x].team = 'blue'
    board.capture((x,y))
    min_score += board.board[y][x].value
    for neighbor in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if neighbor[0] < 5 and neighbor[0] >=0 and neighbor[1] <5 and neighbor[1] >=0:
            t = board.square_at(neighbor)
            if t.team == 'blue':       
                for neighbor in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                    if neighbor[0] < 5 and neighbor[0] >=0 and neighbor[1] <5 and neighbor[1] >=0:
                        temp = board.square_at(neighbor)
                        if temp.team == 'green':
                            temp.team = 'blue'
                            min_score += temp.value
                            max_score -= temp.value
                break
    print board

    
    
while False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    render_game(board)

    pygame.display.flip()
    clock.tick(30)
