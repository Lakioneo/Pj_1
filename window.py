from pygame import *
import os

FPS = 60
window_size = (700,500)

path = "image/tiles/"
grace = [path+"tile_0001.png",path+"tile_0002.png",path+"tile_0000.png"]
paving =path+"tile_0043.png"

game = True
level_run = True
clock = time.Clock()
window = display.set_mode(window_size)
