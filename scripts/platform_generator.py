from scripts.functions import load_image
from random import randint
from scripts.constance import display_size, CreatePlatformEvent
from scripts.platform import Platform, BreakingPlatform, DisappearingPlatform, MovingPlatform
import pygame
class PlatformGenerator():
    def __init__ (self,step):
        self.step=step #Расстояние между платформами
        #Загрузка картинок
        self.platform_images= [
            load_image('assets','images','platform.png'),
            load_image('assets','images','breaking-platform.png'),
            load_image('assets','images','platform.png'),
            load_image('assets','images','moving-platform.png'),]

            self.create_start_configuration()

    def create_start_configuration(self):
        'Начальная платформа'
        platform=Platform((display_size[0]//2),(display_size[1]-50), self.platform_images[0])
        event = pygame.Event(CreatePlatformEvent, {'platform': platform})
        pygame.event.post(event)

        for y in range(int(display_size[1]/self.step),-1,-1):
            self.create_platform(y*self.step)

    def create_platform(self, center_y):
        "Создаёт платформу"
        number=randint(0,3)
        image=self.platform_images[number]
        min_x= image.get_width()//2
        max=display_size[0]-image.get_width()//2
        center = (randint(min_x,max_x), center_y)

        if number == 0:
            info = {'platform': Platform(center, image)}
        elif number == 1:
            info = {'platform': BreakingPlatform(center, image)}
        elif number==2:
            info={'platform': DisappearingPlatform(center, image, 150+randint(0,60))}
        else:
            {'platform': MovingPlatform(center, image, randint(100,300) /100 )}
        
        event = pygame.Event(CreatePlatformEvent, info)
        pygame.event.post(event)

    def update(self, offset_y, platfoms):
        "Обновляем данные"
        #Если верхняя платформа слишком низко опустилась
        if platforms[-1].rect.centery - offset_y >= self.step:
            self.create_platform(offset_y)
            platfoms.remove(platform[0])



    