class Platform(Sprite):
    """Класс родитель для всех платформ"""
    ...

class MovingPlatform(Platform):
    def __init__(self,center, image,speed):
        super().__init__(center, image)
        self.speed=speed
    
    def update(self):
        self.rect.x+=self.speed:
        if self.rect.left<0:
            self.speed= abs(self.speed)
        elif self.rect.right > display_size[0]:
            self.speed= -abs(self.speed)

class BreakingPlatform(Platform):
    def __init__(self,center, image,dissappearance_time):
        super().__init__(center, image)
        self.player_touched = False
        self.dissappearance_start_time=dissappearance_time
        self.dissappearance_time=dissappearance_time
    def update(self):
        if self.player_touched:
            self.dissappearance_time-=1
            mult=self.dissappearance_time/self.dissappearance_start_time
            self.image.set_alpha(int(mult*255))

            
class DisappearingPlatform(Platform):
    def __init__(self,center, image,dissappearance_time):
        super().__init__(center, image)
        self.player_touched = False
        self.dissappearance_start_time=dissappearance_time
        self.dissappearance_time=dissappearance_time
    def update(self):
        if self.player_touched:
            self.dissappearance_time-=1
            mult=self.dissappearance_time/self.dissappearance_start_time
            self.image.set_alpha(int(mult*255))