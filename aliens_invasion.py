import sys

import pygame

from settings import Settings
from ship import Ship


def run_game():
    # 初始化pygame
    pygame.init()
    # 创建设置对象
    ai_settings = Settings()
    # 设置一个1200x800的窗口
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # 设置标题
    pygame.display.set_caption('Aliens Invasion')
    # 创建飞船
    ship = Ship(screen)

    # 开启循环监控事件
    while True:
        # 监测鼠标和键盘事件
        for event in pygame.event.get():
            if event.type == 'QUIT':
                # 注销pygame库
                pygame.quit()
                # 退出程序
                sys.exit()
        # 设置屏幕背景颜色
        screen.fill(ai_settings.bg_color)
        # 把飞船添加到屏幕上
        ship.blitme()

        # 每次循环不断刷新屏幕
        pygame.display.flip()


run_game()
