import pygame
pygame.init()
pygame.mixer.music.load('exe021.mp3')
pygame.mixer.music.play()
from time import sleep
sleep(350)
pygame.event.wait()
