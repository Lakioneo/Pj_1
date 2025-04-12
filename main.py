import time as t
import random
from pygame import *
from window import *
from data import Enemy, Player


font.init()
mixer.init()



while game:
    for ev in event.get():
        if ev.type == QUIT:
            game = False


    if level_run:
        pass

    clock.tick(FPS)
    display.update()












