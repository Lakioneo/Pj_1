from pygame import *
import os

FPS = 60
window_size = (700,500)


path = os.path.join(os.getcwd(),"image","tiles")
grace = [   os.path.join(path,"tile_0001.png"),
            os.path.join(path,"tile_0002.png"),
            os.path.join(path,"tile_0000.png")]
paving = os.path.join(path,"tile_0043.png")

game = True
level_run = True
clock = time.Clock()
window = display.set_mode(window_size)
