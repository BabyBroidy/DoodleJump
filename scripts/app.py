import pygame
import os
from scripts.game import Game
from scripts.functions import load_image
class App():
    def __init__ (self):
        self.maxfps= 60
        self.display_size=(480,720)
        self.running= True
        self.display= pygame.display.set_mode(self.display_size)
        self.clock=pygame.time.Clock()
        self.game = Game()
        pygame.display.set_caption('Doodle Jump')
        pygame.display.set_icon(load_image('assets','icons','icon.ico'))
    def handle_events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.running = False
    def update(self):
        ...
    def render(self):
        self.display.fill((0,0,0)) #Закрашиваем окно
        self.game.render(self.display)
        pygame.display.update() #Обновляем окно
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()

