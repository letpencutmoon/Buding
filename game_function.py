import sys
import pygame
import time
import threading
from bullet import Spoon
from role import Buding,Xcw,Cat
from time import sleep
from game_starts import GameStarts

def check_keydown_event(event,ai_sitting,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        new_buller = Spoon(ai_sitting,screen,ship)
        bullets.add(new_buller)

    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_event(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_SPACE:
        ship.bullet_up = False

def check_events(ai_sittings,screen,stats,play_button,ship,budings,bullets,sb):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event,ai_sittings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_sittings,screen,stats,play_button,ship,budings,bullets,mouse_x,mouse_y,sb)

def check_play_button(ai_settings,screen,stats,play_button,ship,budings,bullets,mouse_x,mouse_y,sb):
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        ai_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.game_active = True
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        budings.empty()
        bullets.empty()
        create_fleet(ai_settings,screen,budings,ship)
        ship.center_ship()

def update_screen(ai_sittings,screen,ship,budings,bullets,play_button,stats,sb):
    screen.fill(ai_sittings.bg_color)
    bullets.draw(screen)
    ship.blitme()
    budings.draw(screen)
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()

def update_bullets(ai_settings,screen,ship,budings,bullets,stats,sb):
    for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
    check_bullet_buding_collisions(ai_settings,screen,ship,budings,bullets,stats,sb)
    if len(budings) == 0:
        budings.empty()
        ai_settings.increase_speed()
        stats.level +=1
        sb.prep_score()
        create_fleet(ai_settings,screen,budings,ship)


def check_bullet_buding_collisions(ai_sittings,screen,ship,budings,bullets,stats,sb):
    collisions = pygame.sprite.groupcollide(bullets,budings,True,True)
    if collisions:
        for budings in collisions.values():
            stats.score +=ai_sittings.buding_point*len(budings)
            sb.prep_score()
        check_high_score(stats,sb)

def get_number_budings_x(ai_sittings,buding_width):
    available_space_x = ai_sittings.screen_width - 2*buding_width
    number_budings_x = int(available_space_x / (2*buding_width))
    return number_budings_x

def get_number_rows(ai_sittings,ship_height,buding_height):
    available_space_y = (ai_sittings.screen_height-(3*buding_height)-ship_height)
    number_rows = int(available_space_y/(2*buding_height))
    return number_rows

def create_buding(ai_sittings,screen,budings,buding_number,row_number):
    buding = Buding(ai_sittings,screen)
    buding_width = buding.rect.width
    buding.x = buding_width + 2*buding_width*buding_number
    buding.rect.x = buding.x
    buding.rect.y = buding.rect.height + 2*buding.rect.height*row_number
    budings.add(buding)

def create_fleet(ai_sittings,screen,budings,ship):
    buding = Buding(ai_sittings,screen)
    number_budings_x = get_number_budings_x(ai_sittings,buding.rect.width)
    number_rows = get_number_rows(ai_sittings,ship.rect.height,buding.rect.height)
    for row_number in range(number_rows):
        for buding_number in range(number_budings_x):
            create_buding(ai_sittings,screen,budings,buding_number,row_number)

def check_fleet_edges(ai_sittings,budings):
    for buding in budings.sprites():
        if buding.check_edge():
            change_fleet_direction(ai_sittings,budings)
            break
def change_fleet_direction(ai_sittings,budings):
    for buding in budings.sprites():
        buding.rect.y += ai_sittings.fleet_drop_speed
    ai_sittings.fleet_direction *=-1

def ship_hit(ai_sittings,stats,screen,ship,budings,bullets,sb):
    if stats.ships_left > 0:
        stats.ships_left -= 1
        sb.prep_ships()
        budings.empty()
        bullets.empty()
        create_fleet(ai_sittings,screen,budings,ship)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_budings_bottom(ai_sittings,stats,screen,ship,budings,bullets,sb):
    screen_rect = screen.get_rect()
    for buding in budings.sprites():
        if buding.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_sittings,stats,screen,ship,budings,bullets,sb)
            break

def update_budings(ai_settings,stats,screen,ship,budings,bullets,sb):
    check_fleet_edges(ai_settings,budings)
    budings.update()
    if pygame.sprite.spritecollideany(ship,budings):
        ship_hit(ai_settings,stats,screen,ship,budings,bullets,sb)
        print("ship hit!!!")
    check_budings_bottom(ai_settings,stats,screen,ship,budings,bullets,sb)

def check_high_score(stats,sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
