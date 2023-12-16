import os
import pygame
def load_image(*paths):
    #Загружаем картинку
    path = os.path.join(*paths)
    image = pygame.image.load(path)
    image = pygame.image.load(path).convert()
    image.set_colorkey((0,0,0))
    return image
