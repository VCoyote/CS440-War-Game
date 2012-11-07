'''
Created on Oct 29, 2012

@author: Dan Pang
'''

'''
#    Board class
#        board: A 2D array of tuples, where the first number is the point value
#                and the second number is the player that holds the space.
#        open:  A list of open spaces, implemented as a dictionary
#        taken: A list of taken spaces, implemented as a dictionary
#
#    Constructor:
#        @param fileName: Name of the maze file
#
#        Constructs the board using the file provided.
#
#    operator str() overload:
#        Returns the current state of the board as a string
'''
class Board:
    turn = 'green'

    # initializer
    def __init__(self, fileName):
        #Initialize all the variables.
        board = open(fileName, 'r').readlines()
        self.board = [[0]*5 for i in range(5)]
        self.open = []
        self.points = {'green': 0, 'blue': 0}
        
        # Parse the board by turning it into an array.
        y = 0
        for line in board:
            x = 0
            for value in line.split():
                self.board[y][x] = Square((x, y), int(value))
                self.open.append((x,y))
                x += 1

            y += 1
        
    def __str__(self):
        ret = ''
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                ret += str(self.board[i][j]) + '\t'
            ret += '\n'
        return ret

    def __iter__(self):
        for row in self.board:
            for square in row:
                yield square
    
    def square_at(self, loc):
        x, y = loc

        if 0 <= x < 5 and 0 <= y < 5:
            return self.board[y][x]

        return None
    


    def capture(self, loc, team = None):
        try:
            self.open.remove(loc)
        except ValueError:
            pass

        square = self.square_at(loc)

        # take over enemies square
        if square.team and square.team != team:
            self.points[square.team] -= square.value
            self.points[team]        += square.value

        # take over empty square
        elif not square.team:
            self.points[team] += square.value



    def drop(self, loc, team = None):
        square = self.square_at(loc)

        # can only land in empty spots
        if not square.team:
            self.capture(loc, team)



    def blitz(self, src, dst, team = None):
        src, dst = self.square_at(src), self.square_at(dst)

        # Requirements to blitz:
        #   1. squares exist
        if not self.square_at(src) or not self.square_at(dst):
            raise Error('Non-existing blitzing squares')

        #   2. squares are adjacent
        col_diff = abs(dst.loc[0] - src.loc[0])
        row_diff = abs(dst.loc[1] - src.loc[1])
        if col_diff != 1 or row_diff != 1:
            raise Error('Blitzing too far')

        #   3. destination square is not occupied
        if dst.team:
            raise Error('Blitzing destination occupied')

        # do the blitz
        self.capture(dst, team=team)

        # capture surrounding squares
        for dir in (0, 1), (1, 0), (-1, 0), (0, -1):
            adj = self.square_at((dst.loc[0]+dir[0], dst.loc[1]+dir[1]))

            if adj and adj.team:
                self.capture(adj.loc, team)

    def next_turn(self):
        if self.turn == 'green':
            self.turn = 'blue'
        else:
            self.turn = 'green'

class Square:
    def __init__(self, loc, value):
        x, y = loc
        self.loc = loc
        self.value = value
        self.team = None
        
    def __str__(self):
        return str((self.value, self.team))


# Testing
if __name__ == '__main__':
    test = Board('Game boards/Punxsutawney.txt')
    print(test)
    print(test.square_at((0,4)))
    print(test.square_at((5,1)))
