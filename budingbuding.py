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
    # 初始化pygame库
    pygame.init()
    # 导入游戏设置
    ai_settings = Settings()

    # 设置游戏区域，即长和宽
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))

    #设置标题和开始按钮
    pygame.display.set_caption("布丁打布丁")
    play_button = Button(ai_settings,screen,"play")

    #开始游戏
    stats = GameStarts(ai_settings)
    ship = Ship(ai_settings,screen)
    bullets = Group()
    budings = Group()        
    sb = Scoreboard(ai_settings,screen,stats)
    #初始化敌人
    gf.create_fleet(ai_settings,screen,budings,ship)

    while True:
        #事件监测
        gf.check_events(ai_settings,screen,stats,play_button,ship,budings,bullets,sb)
        bullets.update()
        #如果游戏还在进行
        if stats.game_active:
            #更新飞船，子弹，敌人
            ship.update()
            gf.update_bullets(ai_settings,screen,ship,budings,bullets,stats,sb)
            gf.update_budings(ai_settings,stats,screen,ship,budings,bullets,sb)
        gf.update_screen(ai_settings,screen,ship,budings,bullets,play_button,stats,sb)
run_game() 