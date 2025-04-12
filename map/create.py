from data import Enemy, Player, Block
from pygame import *
import window
import random




def create_level(path_level:str, width, height, speed):
    mapDecor = sprite.Group()
    mapCollision = sprite.Group()

    with open(path_level,"r") as file:
        y = 0
        for line in file:
            line = line.split(" ")
            x = 0
            for symbol in line:
                if symbol == ".":
                    block = Block(window.grace[random.randint(len(window.grace)-1)],
                                    x,
                                    y,
                                    width,
                                    height, 
                                    speed)
                    mapDecor.add(block)

                if symbol == "#":
                    block = Block(window.paving,
                                    x,
                                    y,
                                    width,
                                    height, 
                                    speed)
                    mapCollision.add()

                x += width

            y += height 

        return {
                "Decor":mapDecor,
                "Collision":mapCollision
                }

        


