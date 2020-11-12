import pygame
import time
import random
pygame.init()
white1=(255,255,255)
black=(0,0,0)
red=(200,0,0)
light_red=(255,0,0)
green=(0,225,0)
yellow=(240,240,0)
light_yellow=(255,255,0)
light_green=(0,255,0)
light_blue=(173,216,230)
display_width=800
display_height=600

gamedisplay=pygame.display.set_mode((display_width,display_height))

pygame.mixer.music.load("goat.mp3")
pygame.mixer.music.play(-1)



pygame.display.set_caption("TANKS")

icon=pygame.image.load("apple.png")
pygame.display.set_icon(icon)

pygame.display.update()
#img=pygame.image.load("snakehead.png")
#appleimg=pygame.image.load("apple.png")

#block_size=20
#apple_size=50
clock=pygame.time.Clock()
FPS=20
direction="right"
smallfont=pygame.font.SysFont("comicsansms",25)          
medfont=pygame.font.SysFont("comicsansms",50)
largefont=pygame.font.SysFont("arial",75)

 
tankwidth=40
tankheight=20

turretwidth=5
wheelwidth=5

ground_height=35
