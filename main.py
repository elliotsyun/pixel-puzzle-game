import pygame
import window

WIDTH, HEIGHT = 600, 500
GAME_NAME = "COLOR'D"
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BUTTON_SCALE = (120, 120)
D_PLUS_IMG = pygame.image.load("./Assets/PLUSPLUS.png")
PLUS_IMG = pygame.image.load("./Assets/PLUS.png")
D_MIN_IMG = pygame.image.load("./Assets/MINMIN.png")
MIN_IMG = pygame.image.load("./Assets/MIN.png")


def main():
    run = True
    fps = pygame.time.Clock().tick(60) / 1000
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        window.window()
        button()
        pygame.display.update()

    pygame.quit()


def button():
    """button scaling, sizing and placement on the window"""
    d_plus_img_s = pygame.transform.scale(D_PLUS_IMG, BUTTON_SCALE)
    plus_img_s = pygame.transform.scale(PLUS_IMG, BUTTON_SCALE)
    d_min_img_s = pygame.transform.scale(D_MIN_IMG, BUTTON_SCALE)
    min_img_s = pygame.transform.scale(MIN_IMG, BUTTON_SCALE)
    WIN.blit(d_plus_img_s, (450, 300))
    WIN.blit(plus_img_s, (315, 300))
    WIN.blit(d_min_img_s, (25, 300))
    WIN.blit(min_img_s, (165, 300))


if __name__ == "__main__":
    main()
