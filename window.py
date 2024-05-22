import pygame
from config import WIDTH, HEIGHT, GAME_NAME, WIN


def gradient_window():
    """Creates the gradient window for the game"""

    white_to_black = pygame.Surface((1, 2))
    white_to_black.fill((255, 255, 255))
    white_to_black.set_at((0, 1), (0, 0, 0))
    white_to_black = pygame.transform.smoothscale(white_to_black, (255, 255))

    white_to_color = pygame.Surface((2, 1))
    white_to_color.fill((255, 255, 255))

    changing_color = (255, 0, 0)
    # below code is changing the color, to red which is (255, 0, 0)
    white_to_color.set_at((1, 0), changing_color)
    white_to_color = pygame.transform.smoothscale(white_to_color, (255, 255))
    white_to_black.blit(white_to_color, (0, 0), special_flags=pygame.BLEND_MULT)

    WIN.blit(white_to_black, (75, 75))

    pygame.display.flip()
    pygame.event.get()
