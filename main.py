import time as t
import random
from pygame import *
from window import *
from data import Enemy, Player
from map import create

font.init()
mixer.init()

background = create.create_level("map/level/1.txt",
                                window_size[0]//10,
                                window_size[1]//8,
                                5)



while game:
    for ev in event.get():
        if ev.type == QUIT:
            game = False


    if level_run:

        background["Decor"].update()
        background["Decor"].draw(window)
        background["Collision"].update()
        background["Collision"].draw(window)
            
            


        
    clock.tick(FPS)
    display.update()












