import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, settings, screen, ship):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)  # 先创建一个矩形，并设置其位置
        self.rect.centerx = ship.image_rect.centerx
        self.rect.top = ship.image_rect.top  # 子弹的位置设置与飞船相同
        self.y = float(self.rect.y)  # 将子弹的位置转换为小数

        self.color = settings.bullet_color  # 子弹颜色
        self.speed_factor = settings.bullet_speed_factor  # 子弹速度

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
