from scripts.sprite import Sprite

class Player(Sprite): #Класс игрока
    def __init__(self, center, image, jump_power, gravity, speed):
        super().__init__(center, image)
        self.gravity=gravity
        self.speed=speed
        self.jump_power=jump_power
        self.is_walking_right=False
        self.is_walking_left=False
        self.velosity_y=0
        self.on_platform=False
    def update(self):
        self.velocity_y = min(self.velocity_y+self.gravity, 15)
        self,recty.y += self.velocity_y