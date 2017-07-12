import pygame
import game_functions as gf
from settings import Settings
from ship import Ship


def run_game():
    # 初始化pygame
    pygame.init()
    # 创建设置对象
    settings = Settings()
    # 设置一个1200x800的窗口
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    # 设置标题
    pygame.display.set_caption('Aliens Invasion')

    # 创建飞船对象
    ship = Ship(screen, settings)

    # 开启循环监控事件
    while True:
        # 监测鼠标和键盘事件
        gf.check_events(ship)
        ship.update()
        # 刷新屏幕
        gf.update_screen(screen, ship, settings)


run_game()
