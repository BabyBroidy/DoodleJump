from scripts.functions import load_image
from scripts.sprite import Sprite
from scripts.player import Player
from scripts.platform import Platform
from scripts.platform_generator import PlatformGenerator
import os
class Game():
    def __init__(self):
        #Загрузка изображений
        self.background= load_image('assets','images','background.png')
        self.platform_generator = PlatformGenerator(200)
        self.player= Sprite((240,360),load_image('assets','images','player.png'),5,20,0.65)
        self.platforms=list()
        self.losed = False
        self.font=pygame.Font(os.path.join('assets','fonts','pixel.ttf'), 32)
    
    def restart(self):
        """Перезапуск игры"""
        self.losed=False
        self.offset_y=0
        self.platforms=list()
        self.platform_generator.create_configuration()

    def collide_sprite(self, other):

    def handle_key_down_event(self,key):
        if self.losed:
            self.restart()
        if key == pygame.K_a: #Нажатие
            self.player.is_walking_left=True
        elif key == pygame.K_d:
            self.player.is_walking_right=True

    def handle_key_up_event(self,key): #Отпускание
        if key ==pygame.K_a:
            self.player.is_walking_left=False
        elif key == pygame.K_d:
            self.player.is_walking_right=False
    
    def handle_create_platform_event(self,platform):
        """Добавляем платформу в список"""
        self.platforms.append(platform)

    def update(self):
        """Обновляем данные игры"""
        self.losed=self.player.rect.top - self.offset_y >= display_size[1]
        self.player.update()
        for platform in self.platforms:
            if self.player.collide_sprite(platform):
                self.player.on_platform = True

        self.platform_generator.update(self.offset_y,self.platforms)
        if self.losed:
            return
        if self.platforms:
            self.platform_generator.update(self.offset_y,self.platforms)

    def render(self, surface):
        #Рендер бэкграунда
        surface.blit(self.background, (0,0))
        for platform in self.platforms:
            platform.render(surface)
        self.player.render(surface)
        #Рендер экрана
        self.player.render(surface)


        score = round(- self.offset_y/10)
        if self.losed:
            score_text = self.font.render(f'Ваш рекорд: {score}.', True, (1,1,1))
            hint_text = self.font.render('Нажмите на любую клавишу:', True, (1,1,1))
            score_rect = score.text.get.rect(centerx=display_size[0]/2, centery=display_size[1]/2-25)
            hint.rect= hint_text.get_rect(centerx=display_size[0]/2, centery=display_size[1]/2+25)
            surface.blit(score_text, score_rect)
            surface,blit(hint_text, hint_rect)
        else:
            text = self.font.render(str(score), True, (255,0,0))
            rect = text.get_rect(midtop=(display_size[0]/2,10))
            surface.blit(text,rect)

        
    
