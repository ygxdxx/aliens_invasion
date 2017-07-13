import sys
import pygame
from bullet import Bullet


def check_events(ship, settings, screen, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, screen, settings, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(screen, ship, settings, bullets):
    # 绘制所有的子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 显示飞船
    ship.blitme()
    # 刷新屏幕
    pygame.display.flip()
    # 设置屏幕颜色
    screen.fill(settings.bg_color)


def check_keydown_events(event, ship, screen, settings, bullets):
    """检测键盘摁下事件"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(settings, screen, ship)
        # 添加到编组
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """检测键盘抬起事件"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
