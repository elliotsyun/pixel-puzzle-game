import pygame

WIDTH, HEIGHT = 400, 400
GAME_NAME = "COLOR'D"
WIN = pygame.display.set_mode((WIDTH, HEIGHT))


BUTTON_SCALE = (120, 120)
D_PLUS_IMG = pygame.image.load("./Assets/PLUSPLUS.png")
PLUS_IMG = pygame.image.load("./Assets/PLUS.png")
D_MIN_IMG = pygame.image.load("./Assets/MINMIN.png")
MIN_IMG = pygame.image.load("./Assets/MIN.png")


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

        pygame.display.update()

    pygame.quit()


def window():
    """window initialization"""
    WIN.fill((255, 255, 255))
    pygame.display.set_caption(GAME_NAME)


if __name__ == "__main__":
    main()
