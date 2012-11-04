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
        self.playerpoints = [0, 0]
        
        x = 0
        temp = []
        # Parse the board by turning it into an array.
        for i in range(len(board)):
            for j in range(len(board[i])):
                # If the character given is a number
                if board[i][j] != '\t' and board[i][j] != '\n':
                    temp.append(board[i][j])        # Add the number to the list
                else:
                    points = int(''.join(temp))     # Turn the list into an integer
                    self.board[i][x] = Square((i,x), points)    # Then add the integer
                    self.open.append(points)
                    temp = []
                    x += 1
            x = 0
        
    def __str__(self):
        ret = ''
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                ret += str(self.board[i][j]) + '\t'
            ret += '\n'
        return ret

    def __iter__(self):
        for row in range(len(self.board[0])):
            for col in range(len(self.board)):
                yield self.square_at((col, row))
                
    
    def square_at(self, loc):
        x, y = loc

        if (x >= 0 and x < 5 and y >= 0 and y < 5):
            return self.board[x][y]
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
