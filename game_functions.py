import sys
import pygame


def check_events():
    for event in pygame.event.get():
        if event.type == 'QUIT':
            # 注销pygame库
            pygame.quit()
            # 退出程序
            sys.exit(0)


def update_screen(screen, ship, settings):
    # 设置屏幕颜色
    screen.fill(settings.bg_color)
    # 显示飞船
    ship.blitme()
    # 刷新屏幕
    pygame.display.flip()
