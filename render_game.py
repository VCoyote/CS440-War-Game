import sys, pygame
from math import floor

# initialize pygame
pygame.init()
screen = pygame.display.set_mode((1024, 800))
clock = pygame.time.Clock()

# load assets
grass    = pygame.image.load('img/grass.png')
team1 = pygame.image.load('img/princess.png')
team2 = pygame.image.load('img/bug.png')

font = pygame.font.SysFont('Arial', 28, bold=True)

# constants
square_rect  = pygame.Rect(20, -20, 100, 82)
board_offset = (20, 20)

# render a square
def render_square(square):
    sr = square_rect
    col, row = square.loc

    # render background
    pos = sr.move(sr.w*col, sr.h*row)
    screen.blit(grass, pos)

    # render team
    if square.team == 'green':
        screen.blit(team1, pos)
    elif square.team == 'blue':
        screen.blit(team2, pos)

    # render points
    pos = pos.move(sr.w/2, sr.h)
    points = font.render(str(square.value), True, (30, 80, 0))
    screen.blit(points, pos)


# render function
def render_game(board):
    screen.fill((0, 0, 0))
    for square in board:
        render_square(square)

# register click
def click(pos, board):
    sq = square_rect

    # translate pixels to game board cells
    x, y = pos
    x, y = x - board_offset[0], y - board_offset[1] 
    col, row = int(floor(x / sq.w)), int(floor(y / sq.h))

    square = board.square_at((col, row))

    # if player can make a move and does, do it
    if square and board.turn == 'green':
        board.drop((col, row), team='green')
        board.next_turn()
