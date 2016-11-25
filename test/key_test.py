background_image_filename = 'sushiplate.jpg'
 
import pygame
from pygame.locals import *
from sys import exit
 
pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
#background = pygame.image.load(background_image_filename).convert()
 
x, y = 0, 0
move_x, move_y = 0, 0
print "--init--" 

while True:
    for event in pygame.event.get():
	print "---key ---"
        if event.type == QUIT:
           exit()
        if event.type == KEYDOWN:
            print "--down--"
            if event.key == K_LEFT:
                print "--left--"
                move_x = -1
            elif event.key == K_RIGHT:
                print "--right--"
                move_x = 1
            elif event.key == K_UP:
                print "--up--" 
                move_y = -1
            elif event.key == K_DOWN:
                print "--down---"
                move_y = 1
        elif event.type == KEYUP:

            move_x = 0
            move_y = 0
 

        x+= move_x
        y+= move_y
 
        screen.fill((0,0,0))
        #screen.blit(background, (x,y))
 
        pygame.display.update()
