import pygame
from pygame.sprite import Sprite
class Buding(Sprite):
    def __init__(self,ai_settings,screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('./images/被吃的布丁.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def check_edge(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        elif self.rect.left<=0:
            return True

    def update(self):
        self.x += (self.ai_settings.buding_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x


class Xcw(Sprite):
    def __init__(self,ai_settings,screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('D:/py/py代码/venv/images/xcw.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def check_edge(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        elif self.rect.left<=0:
            return True

    def update(self):
        self.x += (self.ai_settings.buding_speed_factor*self.ai_settings.fleet_direction)
        self.rect.x = self.x


class Yly(Sprite):
    def __init__(self,ai_settings,screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('D:/py/py代码/venv/images/yly.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def check_edge(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        elif self.rect.left<=0:
            return True

    def update(self):
        self.x += self.ai_settings.buding_speed_factor*self.ai_settings.fleet_direction
        self.rect.x = self.x

class Cat(Sprite):
    def __init__(self,ai_settings,screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('D:/py/py代码/venv/images/水黑.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def check_edge(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        elif self.rect.left<=0:
            return True

    def update(self):
        self.x += self.ai_settings.buding_speed_factor*self.ai_settings.fleet_direction
        self.rect.x = self.x
