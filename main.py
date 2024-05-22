import pygame
from config import WIDTH, HEIGHT, GAME_NAME, WIN


def main():
    run = True
    while run:

        pygame.time.Clock().tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                coord = pygame.mouse.get_pos()
                color = WIN.get_at(coord)
                print("Color: ", color)

        pygame.display.update()

    pygame.quit()


def initialize_window():
    """window initialization"""
    WIN.fill((255, 255, 255))
    pygame.display.set_caption(GAME_NAME)


if __name__ == "__main__":
    main()
