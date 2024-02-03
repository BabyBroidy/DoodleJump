from scripts.functions import load_image
from scripts.sprite import Sprite
from scripts.player import Player
from scripts.platform_generator import PlatformGenerator

class Game():
    def __init__(self):
        #Загрузка изображений
        self.background= load_image('assets','images','background.png')
        self.platform_generator = PlatformGenerator(200)
        self.player= Sprite((240,360),load_image('assets','images','player.png'),5,20,0.65)
        self.platforms=list()

    def handle_key_down_event(self,key):
        if key ==pygame.K_a:
            self.player.is_walking_left=True
        elif key == pygame.K_d:
            self.player.is_walking_right=True

    def handle_key_down_event(self,key):
        if key ==pygame.K_a:
            self.player.is_walking_left=False
        elif key == pygame.K_d:
            self.player.is_walking_right=False
    
    def handle_create_platform_event(self,platform):
        """Добавляем платформу в список"""
        self.platforms.append(platform)


    def update(self):
        """Обновляем данные игры"""
        self.player.update()
        self.platform_generator.update(self.offset_y,self.platforms)

    def render(self, surface):
        #Рендер бэкграунда
        surface.blit(self.background, (0,0))
        #Рендер экрана
        self.player.render(surface)
    
