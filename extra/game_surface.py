import sys
import pygame


def make_surface():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    screen.fill((240, 255, 255))
    pygame.display.set_caption('extra_surface')

    image = pygame.image.load_basic('../images/ship.bmp')
    image_rect = image.get_rect()
    screen_rect = screen.get_rect()

    image_rect.centerx = screen_rect.centerx
    image_rect.centery = screen_rect.centery

    screen.blit(image, image_rect)

    while True:
        pygame.display.flip()


make_surface()
