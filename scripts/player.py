from scripts.sprite import Sprite
import pygame
class Player(Sprite): #Класс игрока
    def __init__(self, center, image, jump_power, gravity, speed):
        super().__init__(center, image)
        self.original_image = image.copy()
        self.gravity=gravity
        self.speed=speed
        self.jump_power=jump_power
        self.is_walking_right=False
        self.is_walking_left=False
        self.velosity_y=0
        self.on_platform=False

    def update(self):
        """Обновляем данные игрока"""
        if self.on_platform:
            self.velocity_y= - self.jump_power

        self.velocity_y = min(self.velocity_y+self.gravity, 15)
        self.rect.y += self.velocity_y
        #Логика перса
        if self.is_walking_right!= self.is_walking_left:
            if self.is_walking_right:
                self.rect.x += self.speed
                self.image= self.original_image.copy()
            else:
                self.rect.x -= self.speed
                self.image = pygame.transform.flip(self.original_image, True, False)
        self.on_platform=False
        
    def reset(self,center): #Возврат к началу
        super().__init__(center, self.original_image)
        self.velocity_y=0
        self.is_walking_right= False
        self.is_walking_left = False
        self.on_platform= False

