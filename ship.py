import pygame


class Ship:
    def __init__(self, screen, settings):
        """初始化飞船的位置"""
        self.settings = settings
        # 加载图片
        self.image = pygame.image.load_basic('images/ship.bmp')
        self.screen = screen

        # 分别模拟成矩形
        self.image_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 设定飞船出现的位置 把屏幕的坐标赋值给图片矩形
        self.image_rect.centerx = self.screen_rect.centerx
        self.image_rect.bottom = self.screen_rect.bottom

        self.center = float(self.image_rect.centerx)

        # 移动标记
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """刷新飞船位置"""
        self.screen.blit(self.image, self.image_rect)

    def update(self):
        """改变飞船在x轴上的位置"""
        if self.moving_right and self.image_rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_factor
        if self.moving_left and self.image_rect.left > 0:
            self.center -= self.settings.ship_speed_factor
        # 调整所在位置
        self.image_rect.centerx = self.center
