from scripts.functions import load_image
from scripts.sprite import Sprite


class Game():
    def __init__(self):
        #Загрузка изображений
        self.background= load_image('assets','images','background.png')
        self.player= Sprite((240,360),load_image('assets','images','player.png'))
    def render(self, surface):
        #Рендер бэкграунда
        surface.blit(self.background, (0,0))
        #Рендер экрана
        self.player.render(surface)