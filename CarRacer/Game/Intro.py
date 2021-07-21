import pygame
import os
import time
import sys
import keyboard

pygame.init()


win = pygame.display.set_mode((1080,517))
pygame.display.set_caption("Pixel car racer(For Windows)")
music = pygame.mixer.music.load('background.mp3')
pygame.mixer.music.play(-1)


back = pygame.image.load('back.png')
white = (255,255,255)
key = pygame.key.get_pressed()

run = False



while not run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True
    
       
        if keyboard.is_pressed('enter'):
            startsound = pygame.mixer.Sound('startsound.mp3')
            startsound.play()
            time.sleep(3)
            os.startfile('menu.py')
            sys.exit()
            break

        
            
        
    win.fill(white)
    win.blit(back, (0,0))
    pygame.display.update()

