import sys
import pygame


def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 注销pygame库
            pygame.quit()
            # 退出程序
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            # 左右移动
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False


def update_screen(screen, ship, settings):
    # 设置屏幕颜色
    screen.fill(settings.bg_color)
    # 显示飞船
    ship.blitme()
    # 刷新屏幕
    pygame.display.flip()
