import pygame


class Ship:
    def __init__(self, screen):
        """初始化飞船的位置"""
        self.screen = screen
        # 加载图片
        self.image = pygame.image.load_basic('images/ship.bmp')
        # 模拟成矩形
        self.image_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 设定飞船出现的位置 把屏幕的坐标赋值给图片矩形
        self.image_rect.centerx = self.screen_rect.centerx
        self.image_rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.image_rect)
