from .GameSprit import GameSprit
from pygame import *
class Block(GameSprit):
    def __init__(self, img, x, y, width, height, speed, *groups):
        super().__init__(img, x, y, width, height, speed, *groups)

    def update(self, *args, **kwargs):
        keyList = key.get_pressed()
        if keyList[K_RIGHT]:
            self.rect.x -= self.speed
        elif keyList[K_LEFT]:
            self.rect.x += self.speed
        
        if keyList[K_UP]:
            self.rect.y += self.speed
        elif keyList[K_DOWN]:
            self.rect.y -= self.speed
        return super().update(*args, **kwargs)
        
