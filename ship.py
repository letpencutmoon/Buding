import pygame
from pygame.sprite import Sprite

#飞船类
class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        super(Ship,self).__init__()
        self.screen = screen
        self.ai_settings =ai_settings
        
        #贴图，大小，场景设置
        self.image = pygame.image.load('./images/布丁-最终.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #初始位置
        self.rect.centerx =  self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)
        #默认未移动
        self.moving_right = False
        self.moving_left = False
    #移动
    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx
