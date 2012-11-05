#  Assumptions:
# Grid contains a 5 by 5 array of Squares, each of which has a value, a team, and a location (and pointers to adjacent Squares?)
# Grid has the function square_at((int,int), which returns a reference to the Square a that location in the grid

from copy import deepcopy
#   calculate_minimax(string,string,Grid,int,int,int,Square) returns the heuristic value and location of the best choice
#   for the next move of the game
def calculate_minimax(curr_team, evil_team, board , depth, loc):
    # define constants
    max_depth = 1
    max_team = 'green'
    # make deep copy of the board to work with, so earlier paths don't alter new paths
    grid = deepcopy(board)
    # root search node hasn't altered anything yet
    if depth == 0:
        if curr_team == max_team:
            return max(calculate_minimax(curr_team, evil_team, grid, depth+1, next) for next in grid.open)
        else:
            return min(calculate_minimax(curr_team, evil_team, grid, depth+1, next) for next in grid.open)
    # Mark the location as captured
    # loc refers to the square in board, but we want to equivalent square in grid to alter
    square = grid.square_at(loc)
    grid.capture(loc)
    # we treat each square as a Para-Drop, then we check to see if it has any neighbors that belong
    # to the current team...it is more advantageous to Death Blitz whenever possible
    x = loc[0]
    y = loc[1]
    all_neighbors = [grid.square_at((x+1, y)), grid.square_at((x-1,y)), grid.square_at((x,y+1)), grid.square_at((x,y-1))]
    for neighbor in all_neighbors:
        # check for wall
        if not neighbor:
            continue
        # check if we have a neighbor on our side (we only need one neighbor)
        if neighbor.team == curr_team:
            # check the neighbors for ones on the enemy team
            for evil in all_neighbors:
                if not evil:
                    continue
                if evil.team == evil_team:
                    # we have conquered an enemy square, add its value to the current player's score,
                    # subtract the value from the evil player's score, and mark the square as belonging to
                    # the current team
                    if curr_team == max_team:
                        grid.greenpoints += evil.value
                        grid.bluepoints -= evil.value
                    else:
                        grid.greenpoints -= evil.value
                        grid.bluepoints += evil.value
                    evil.team = curr_team
            break
    # we just took this square, mark it as current players and add its value to their score
    if curr_team == max_team:
        grid.greenpoints += square.value
    else:
        grid.bluepoints += square.value
    square.team = curr_team
    if depth >= max_depth or len(grid.open) == 0:
        # return [heuristic value, square used,max_team value, min_team value]
        # max_team wants (max_value - min_value) to be as large as possible, min_team wants it to be as small as possible
        return [grid.greenpoints - grid.bluepoints, square.loc]
    else:
        if curr_team == max_team:
            retval = max(calculate_minimax(evil_team, curr_team, grid, depth+1, next) for next in grid.open)
            return retval
        else:
            retval = min(calculate_minimax(evil_team, curr_team, grid, depth+1, next) for next in grid.open)
            return retval

