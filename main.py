import pygame

WIDTH, HEIGHT = 600, 500
GAME_NAME = "Color'd"
WIN = pygame.display.set_mode((WIDTH, HEIGHT))


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        window()

    pygame.quit()


def window():
    '''initializes window'''
    WIN.fill((255, 255, 255))
    pygame.display.set_caption(GAME_NAME)
    pygame.display.update()


if __name__ == "__main__":
    main()
