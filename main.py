import pygame

WIDTH, HEIGHT = 255, 255
GAME_NAME = "COLOR'D"
WIN = pygame.display.set_mode((WIDTH, HEIGHT))


BUTTON_SCALE = (120, 120)
D_PLUS_IMG = pygame.image.load('./Assets/PLUSPLUS.png')
PLUS_IMG = pygame.image.load('./Assets/PLUS.png')
D_MIN_IMG = pygame.image.load('./Assets/MINMIN.png')
MIN_IMG = pygame.image.load('./Assets/MIN.png')


def main():
    run = True
    while run:
        
        pygame.time.Clock().tick(10)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                color_coord_x, color_coord_y = pygame.mouse.get_pos()
                print("The color chose: (", color_coord_x, ", ", (255-color_coord_y), ", ", (255-color_coord_y), ")")

        surf = pygame.Surface((1, 2))
        surf.fill((255, 255, 255))
        surf.set_at((0, 1), (0, 0, 0))
        surf = pygame.transform.smoothscale(surf, WIN.get_size())

        surf2 = pygame.Surface((2, 1))
        surf2.fill((255, 255, 255))
        surf2.set_at((1, 0), (255, 0, 0))
        surf2 = pygame.transform.smoothscale(surf2, WIN.get_size())
        surf.blit(surf2, (0, 0), special_flags=pygame.BLEND_MULT)

        WIN.blit(surf, (0, 0))

        pygame.display.flip()
        pygame.event.get()

        pygame.display.update()

    pygame.quit()


def window():
    '''window initialization'''
    WIN.fill((255, 255, 255))
    pygame.display.set_caption(GAME_NAME)





if __name__ == "__main__":
    main()
