import pygame
pygame.mixer.init()
pygame.mixer.music.load('Ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()