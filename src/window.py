import pygame
from config import WIDTH, HEIGHT, GAME_NAME, WIN

# red, orange, yellow, green, blue, indigo, violet
COLORS = [
    (255, 0, 0),
    (21, 255, 255),
    (42, 255, 255),
    (85, 255, 255),
    (170, 255, 255),
    (191, 255, 255),
    (213, 255, 255),
]


def gradient_window():
    """Creates the gradient window for the game"""

    white_to_black_size = (255, 255)
    white_to_color_size = (125, 255)

    # for color in COLORS:
    # specific_color = color
    color = (255, 0, 0)

    white_to_black = make_white_to_black(white_to_black_size)
    white_to_color = make_white_to_color(color, white_to_color_size)

    white_to_black.blit(white_to_color, (0, 0), special_flags=pygame.BLEND_RGB_MULT)

    WIN.blit(white_to_black, (75, 75))

    pygame.display.flip()
    pygame.event.get()


def make_white_to_black(size):
    """Creates the white_to_black gradient for the window"""

    white_to_black = pygame.Surface((1, 2))
    white_to_black.fill((255, 255, 255))
    white_to_black.set_at((0, 1), (0, 0, 0))
    white_to_black = pygame.transform.smoothscale(white_to_black, size)

    return white_to_black


def make_white_to_color(color, size):
    """Creates a white_to_color gradient window with specified color and size of
    the gradient"""

    white_to_color = pygame.Surface((2, 1))
    white_to_color.fill((255, 255, 255))
    white_to_color.set_at((1, 0), color)
    white_to_color = pygame.transform.smoothscale(white_to_color, size)
    return white_to_color
