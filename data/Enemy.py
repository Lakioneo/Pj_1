from .GameSprit import GameSprit



class Enemy(GameSprit):
    def __init__(self, *groups):
        super().__init__(*groups)