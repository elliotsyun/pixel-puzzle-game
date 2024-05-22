import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BUTTON_SCALE = (120, 120)
D_PLUS_IMG = pygame.image.load('./Assets/PLUSPLUS.png')
PLUS_IMG = pygame.image.load('./Assets/PLUS.png')
D_MIN_IMG = pygame.image.load('./Assets/MINMIN.png')
MIN_IMG = pygame.image.load('./Assets/MIN.png')


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()
