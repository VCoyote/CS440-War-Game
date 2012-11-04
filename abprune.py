#  Assumptions:
# Grid contains a 5 by 5 array of Squares, each of which has a value, a team, and a location (and pointers to adjacent Squares?)
# Grid has the function square_at((int,int), which returns a reference to the Square a that location in the grid
from copy import deepcopy
prune = None
#prune must be reset to None before ab pruning commences
#   calculate_abprune(string,string,Grid,int,int,int,Square) returns the heuristic value and location of the best choice
#   for the next move of the game
def calculate_abprune(curr_team, evil_team, board , depth, curr_value, evil_value, loc):
    # define constants
    global prune
    max_depth = 2
    max_team = 'green'
    best_square = None
    # make deep copy of the board to work with, so earlier paths dont alter new paths
    grid = deepcopy(board)

    # root search node hasn't altered anything yet
    if depth == 0:
            prune = None
            return max(calculate_abprune(curr_team, evil_team, grid, depth+1, curr_value, evil_value, next) for next in grid.open)
    # loc refers to the square in board, but we want to equivalent square in grid to alter
    square = grid.square_at(loc)
    # Mark the location as captured
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
                    curr_value += evil.value
                    evil_value -= evil.value
                    evil.team = curr_team
        break
    # we just took this square, mark it as current players and add its value to their score
    curr_value += square.value
    square.team = curr_team
    if depth >= max_depth or len(grid.open) == 0:
        # return [heuristic value, square used]
        # max_team wants (max_value - min_value) to be as large as possible, min_team wants it to be as small as possible
            return [curr_value - evil_value, square.loc, curr_value, evil_value]
    else:
        if curr_team == max_team:
            #search through each possible next move 
            for next in grid.open:
                retval = calculate_abprune(evil_team, curr_team, grid, depth+1, evil_value, curr_value, next)
                if not retval:
                    continue
                #if the value is above prune (and if prune has been set yet)
                #then min will never pick this route, throw it out
                if prune:
                    if retval[0] > prune:
                        return None
                if not best_square:
                    best_square = retval
                #if the result is higher than our previous max, make it the new max
                if retval[0] > best_square[0]:
                    best_square = retval
            #our new best choice is where we prune from
            if best_square:
                prune = best_square[0]
            return best_square
        else:            
            for next in grid.open:
                retval = calculate_abprune(evil_team, curr_team, grid, depth+1, evil_value, curr_value, next)
                if not retval:
                    continue
                #if the value is below prune, max will never pick it, so throw it out
                if prune:
                    if retval[0] > prune:
                        return None
                if not best_square:
                    best_square = retval
                #if the result is lower than our previous min, make it the new min
                if retval[0] > best_square[0]:
                    best_square = retval
            #our selection is the new prune
            if best_square:
                prune = best_square[0]
            return best_square