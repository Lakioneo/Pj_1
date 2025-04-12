from .GameSprit import GameSprit

class Block(GameSprit):
    def __init__(self, img, x, y, width, height, speed, *groups):
        super().__init__(img, x, y, width, height, speed, *groups)

    def update(self, *args, **kwargs):
        if kwargs["moveX"] > 0 and kwargs["moveX"] < 0: 
            self.rect.x -= kwargs["moveX"]
        if kwargs["moveY"] > 0 and kwargs["moveY"] < 0: 
            self.rect.x -= kwargs["moveY"]
        return super().update(*args, **kwargs)
        
