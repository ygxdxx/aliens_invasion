import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group


def run_game():
    """初始化屏幕相关参数"""
    # 获取设置对象
    settings = Settings()
    # 初始化pygame对象
    pygame.init()
    # 设置一个1200x800的窗口
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    # 设置标题
    pygame.display.set_caption('Aliens Invasion')

    # 创建飞船对象
    ship = Ship(screen, settings)
    # 编组
    bullets = Group()

    # 开启循环监控事件
    while True:
        # 监测鼠标和键盘事件
        gf.check_events(ship, settings, screen, bullets)
        ship.update()
        bullets.update()
        gf.update_bullets(bullets)
        # 刷新屏幕
        gf.update_screen(screen, ship, settings, bullets)


if __name__ == '__main__':
    run_game()
