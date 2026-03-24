import pygame
print('sente a vibe dessa musiquinha')
pygame.init()
pygame.mixer.music.load('lofiex0021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
