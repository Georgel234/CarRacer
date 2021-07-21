import pygame
import keyboard
import sys
import time
import webbrowser
import os
import json


pygame.init()


win = pygame.display.set_mode((1080,517))
pygame.display.set_caption("Pixel car racer(For Windows)")
pygame.mixer.music.load('menumusic.mp3')
pygame.mixer.music.play(-1)
joysticks = []





def menu():
    
    
    if keyboard.is_pressed('d'):
        webbrowser.open('https://www.paypal.com/paypalme/GeorgeNexus')
        
    if keyboard.is_pressed('p'):
        os.startfile('gm.py')
        
    if keyboard.is_pressed('s'):
        os.startfile('settings.py')
        
        
        


    
run = False



while not run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True

        menu()
