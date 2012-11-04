import sys, pygame

# initialize pygame
pygame.init()
screen = pygame.display.set_mode((1024, 800))
clock = pygame.time.Clock()

# load assets
grass = pygame.image.load('img/grass.png')
font = pygame.font.SysFont('Arial', 26, bold=True)

# constants
square_rect = pygame.Rect(20, -20, 100, 82)

# render a square
def render_square(square):
    sr = square_rect
    col, row = square.loc

    # render background
    pos = sr.move(sr.w*col, sr.h*row)
    screen.blit(grass, pos)

    # render points
    pos = pos.move(sr.w/2, sr.h)
    points = font.render(str(square.value), True, (100, 100, 100))
    screen.blit(points, pos)


# render function
def render_game(board):
    screen.fill((0, 0, 0))
    for square in board:
        render_square(square)
