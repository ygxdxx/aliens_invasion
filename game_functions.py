import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_events(ship, settings, screen, bullets):
    """监控键盘事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()
        elif event.type == pygame.K_q:
            quit_game()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, screen, settings, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def quit_game():
    pygame.quit()
    sys.exit(0)


def fire_bullet(settings, screen, ship, bullets):
    """开火"""
    if len(bullets) < settings.bullet_allowed:
        new_bullet = Bullet(settings, screen, ship)
        # 添加到编组
        bullets.add(new_bullet)


def remove_bullets(bullets):
    """删除消失的子弹"""
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def get_number_aliens_x(settings, alien_width):
    """计算每行可以容纳外星人的数量"""
    available_space_x = settings.screen_width - 2 * alien_width
    number_alienx_x = int(available_space_x / (2 * alien_width))
    return number_alienx_x


def create_alien(settings, screen, aliens, alien_number):
    """创建一个外星人并放置在当前行"""
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)


def create_fleet(settings, screen, aliens):
    """创建一排外星人"""
    alien = Alien(screen, settings)
    number_aliens_x = get_number_aliens_x(settings, alien.rect.width)

    for alien_number in range(number_aliens_x):
        create_alien(settings, screen, aliens, alien_number)


def update_screen(screen, ship, settings, bullets, aliens):
    """绘制图像"""
    # 绘制所有的子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 显示飞船
    ship.blitme()
    # 显示外星人
    aliens.draw(screen)
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
        fire_bullet(settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    """检测键盘抬起事件"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
