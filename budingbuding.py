import sys
import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from bullet import Spoon
from role import Buding,Yly,Xcw,Cat
from game_starts import GameStarts
from button import Button
from scoreboard import Scoreboard
import game_function as gf

def run_game():
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("布丁打布丁")
    play_button = Button(ai_settings,screen,"play")
    stats = GameStarts(ai_settings)
    ship = Ship(ai_settings,screen)
    bullets = Group()
    budings = Group()        
    sb = Scoreboard(ai_settings,screen,stats)

    gf.create_fleet(ai_settings,screen,budings,ship)

    while True:
        gf.check_events(ai_settings,screen,stats,play_button,ship,budings,bullets,sb)
        bullets.update()
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,ship,budings,bullets,stats,sb)
            gf.update_budings(ai_settings,stats,screen,ship,budings,bullets,sb)
        gf.update_screen(ai_settings,screen,ship,budings,bullets,play_button,stats,sb)
run_game()  