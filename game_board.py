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
    # initializer
    def __init__(self, fileName):
        #Initialize all the variables.
        board = open(fileName, 'r').readlines()
        self.board = [[0]*5 for i in range(5)]
        self.open = []
        self.greenpoints = 0
        self.bluepoints = 0
        
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

        if (x >= 0 and x < 5 and y >= 0 and y < 5):
            return self.board[y][x]
        else:
            return None
    
    def capture(self, loc):
        self.open.remove(loc)

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
