from data import Enemy, Player, Block
from pygame import *
import window
import random


def create_level(path_level:str, width, height, speed) -> dict["Decor": sprite.Group,"Collision": sprite.Group]:
    """
    {
        "Decor": Group,
        "Collision": Group
    }
    """
    mapDecor = sprite.Group()
    mapCollision = sprite.Group()

    with open(path_level,"r") as file:
        y = 0
        for line in file:
            line = line.split(" ")
            x = 0
            for symbol in line:
                if symbol == ".":
                    random_number_image = random.randint(0,len(window.grace)-1)
                    block = Block(window.grace[random_number_image],
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
                    mapCollision.add(block)
                x += width
            y += height 

        return {
                "Decor":mapDecor,
                "Collision":mapCollision
                }

        


