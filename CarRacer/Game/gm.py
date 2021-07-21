import keyboard
import pygame
import time

pygame.init()

win = pygame.display.set_mode((1080,517))
pygame.display.set_caption("Pixel car racer(For Windows)")



for i in range(pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
    joystick[-1].init()
run = False


while not run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True




        if event.type:
            print(event)
            
                    
                        
                

    
   
