from .GameSprit import GameSprit

class Player(GameSprit):
    def __init__(self, *groups):
        super().__init__(*groups)