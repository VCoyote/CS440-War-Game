import sys, pygame
from math import floor

# initialize pygame
pygame.init()
screen = pygame.display.set_mode((570, 600))
clock = pygame.time.Clock()

# load assets
grass    = pygame.image.load('img/grass.png').convert_alpha()
team1 = pygame.image.load('img/princess.png').convert_alpha()
team2 = pygame.image.load('img/bug.png').convert_alpha()

font = pygame.font.SysFont('Arial', 28, bold=True)

# constants
square_rect  = pygame.Rect(20, -20, 100, 82)
square_offset = (20, 20)
board_offset =  (0,  80)

# globals
click_start    = None
preview_square = None

# render a square
def render_square(square):
    sr = square_rect
    col, row = square.loc

    # render background
    pos = sr.move(sr.w*col + board_offset[0], sr.h*row + board_offset[1])
    screen.blit(grass, pos)

    # render team
    if square.team == 'green':
        screen.blit(team1, pos)
    elif square.team == 'blue':
        screen.blit(team2, pos)

    # render move preview
    if square.loc == preview_square:
        screen.blit(team1, pos)

    # render points
    pos = pos.move(sr.w/2, sr.h)
    points = font.render(str(square.value), True, (10, 20, 0))
    screen.blit(points, pos)


# render function
def render_game(board):
    screen.fill((167, 219, 216))
    for square in board:
        render_square(square)

    # render player scores
    score_pos = pygame.Rect(20, 20, 0, 0)
    score = font.render('Queens: {}'.format(board.points['green']), True, (10, 60, 10))
    screen.blit(score, score_pos)

    score = font.render('Bugs: {}'.format(board.points['blue']), True, (10, 60, 10))
    screen.blit(score, score_pos.move(380, 0))
    

# mouse handling functions
def px_to_square(pos, board):
    sq = square_rect

    # translate pixels to game board cells
    x, y = pos
    x, y = x - square_offset[0] - board_offset[0], y - square_offset[1] - board_offset[1]
    col, row = int(floor(x / sq.w)), int(floor(y / sq.h))

    return board.square_at((col, row))

def mouse_down(pos, board):
    global click_start

    square = px_to_square(pos, board)

    # keep track of click start
    if square:
        click_start = square.loc


def mouse_move(pos, board):
    global preview_square

    square = px_to_square(pos, board)

    if not board.turn == 'green':
        return

    # only show preview on empty squares
    if square and not square.team:
        preview_square = square.loc
    else:
        preview_square = None


def mouse_up(pos, board):
    global preview_square, click_start

    square = px_to_square(pos, board)

    if not square:
        return

    # check if player wanted blitz or drop and then execute it
    cs_x, cs_y = click_start
    x,    y    = square.loc
    diff = (abs(cs_x - x), abs(cs_y - y))

    if not square.team and (diff == (0, 1) or diff == (1, 0)):
        board.blitz(square.loc, team='green')
    elif not square.team:
        board.drop(square.loc, team='green')
    else:
        return

    board.next_turn()
    preview_square, click_start = None, None
