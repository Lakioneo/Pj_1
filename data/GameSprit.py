from pygame import *
import window


class GameSprit(sprite.Sprite):
    def __init__(self, img, x, y, width, height, speed, *groups):
        super().__init__(*groups)
        self.image = transform.scale(image.load(img),(width, height))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed = speed

    def show(self):
        window.window.blit(self.image,(self.rect.x,self.rect.y))
