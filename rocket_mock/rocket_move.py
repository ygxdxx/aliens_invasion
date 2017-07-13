import sys
import pygame


def rocket_move():
    # 初始化
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption('rocket_move')
    # 火箭对象
    rocket = Rocket(screen, settings)

    while True:
        # check_events(rocket)
        update_screen(rocket, settings, screen)
        # rocket.update_x()


def update_screen(rocket, settings, screen):
    screen.fill(settings.bg_color)
    pygame.display.flip()
    rocket.blit_rocket()


def check_events(rocket):
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event == pygame.KEYDOWN:
            check_key_down(event, rocket)
        elif event == pygame.KEYUP:
            check_key_up(event, rocket)


def check_key_down(event, rocket):
    """键盘落下"""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = True
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = True


def check_key_up(event, rocket):
    """键盘抬起"""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = False


class Settings:
    def __init__(self):
        self.screen_width = 800  # 屏幕长度
        self.screen_height = 600  # 屏幕高度
        self.bg_color = (240, 255, 255)  # 颜色
        self.rocket_speed = 1.5  # 飞船速度


class Rocket:
    def __init__(self, screen, settings):
        # 获取屏幕对象
        self.screen = screen
        self.settings = settings
        # 加载图片
        self.image = pygame.image.load_basic('../images/ship.bmp')
        # 模拟矩形
        self.image_rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        # 设置飞船初始位置 在屏幕正中央
        self.image_rect.centerx = self.screen_rect.centerx
        # self.image_rect.centery = self.screen_rect.centery
        self.image_rect.bottom = self.screen_rect.bottom
        # 获取初始位置
        self.center_x = float(self.image_rect.centerx)
        # self.center_y = float(self.image_rect.centery)

        # 左右移动标记
        self.moving_left = False
        self.moving_right = False

    def update_x(self):
        """x轴上的移动"""
        if self.moving_left and self.image_rect.left > 0:
            self.center_x -= self.settings.rocket_speed
        elif self.moving_right and self.image_rect.right < self.screen_rect.right:
            self.center_x += self.settings.rocket_speed
        # 修改位置
        self.image_rect.centerx = self.center_x

        # def update_y(self):
        #     """y轴"""
        #     if self.move_up and self.image_rect.top > 0:
        #         self.center_y -= self.settings.rocket_speed
        #     elif self.move_down and self.image_rect.bottom < self.screen_rect.bottom:
        #         self.center_y += self.settings.rocket_speed
        #     self.image_rect.centery = self.center_y

    def blit_rocket(self):
        """绘制图形"""
        self.screen.blit(self.image, self.image_rect)


if __name__ == '__main__':
    rocket_move()
