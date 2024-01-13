class Sprite:
    def __init__(self,center,image):
        #Объект
        self.image = image.copy()
        self.rect = self.image.get_frect()
        self.rect.center=center

    def render(self,surface):
        #Отоброжение картинки
        surface.blit(self.image, self.rect)

    def collide_sprite(self, other):
        #Контроль столкновения
        return self.rect.colliderect(other.rect)