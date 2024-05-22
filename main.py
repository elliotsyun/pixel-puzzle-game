import pygame
import hexgenerator as hg

WIDTH, HEIGHT = 600, 500
GAME_NAME = "COLOR'D"
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BUTTON_SCALE = (120, 120)
COLOR_SCALE = (120, 120)
D_PLUS_IMG = pygame.image.load('./Assets/PLUSPLUS.png')
PLUS_IMG = pygame.image.load('./Assets/PLUS.png')
D_MIN_IMG = pygame.image.load('./Assets/MINMIN.png')
MIN_IMG = pygame.image.load('./Assets/MIN.png')
WHITE = (255, 255, 255)


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        window()
        button()
        color_circ()
        pygame.display.update()

    pygame.quit()


def window():
    '''window initialization'''
    WIN.fill((255, 255, 255))
    pygame.display.set_caption(GAME_NAME)


def button():
    '''button scaling, sizing and placement on the window'''
    d_plus_img_s = pygame.transform.scale(D_PLUS_IMG, BUTTON_SCALE)
    plus_img_s = pygame.transform.scale(PLUS_IMG, BUTTON_SCALE)
    d_min_img_s = pygame.transform.scale(D_MIN_IMG, BUTTON_SCALE)
    min_img_s = pygame.transform.scale(MIN_IMG, BUTTON_SCALE)
    new = min_img_s.fill((255, 0, 0, 100))
    WIN.blit(d_plus_img_s, (450, 300))
    WIN.blit(plus_img_s, (315, 300))
    WIN.blit(d_min_img_s, (25, 300))
    WIN.blit(min_img_s, (165, 300))


def color_circ():
    '''creates the randomized color circles'''
    rand_color = (0, 255, 0)
    user_color = (0, 0, 255)

    circ_radius = 10
    surf = pygame.Surface((100, 100))


    CIRCLE1 = pygame.Surface((100, 100))
    CIRCLE1.fill((255, 0, 0))
    pygame.draw.rect(CIRCLE1, rand_color, ((10, 10), (150, 150)), width=0)

    CIRCLE1 = pygame.Surface((100, 100))
    CIRCLE1.fill(WHITE)
    pygame.draw.circle(CIRCLE1, rand_color, (50, 50), 20, width=0)
    WIN.blit(CIRCLE1, (200, 200))


    CIRCLE2 = pygame.Surface((100, 100))
    CIRCLE2.fill(WHITE)
    pygame.draw.circle(CIRCLE2, user_color, (150, 150), 10, width=0)
    WIN.blit(CIRCLE2, (100, 100))


if __name__ == "__main__":
    main()
