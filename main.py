import pygame
from time import sleep

pygame.init()
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# Load and play music
pygame.mixer.init()
pygame.mixer.music.load('tolling-bell_daniel-simion.mp3')
pygame.mixer.music.play()

sleep(2)  # blank screen for 3 seconds

pygame.mixer.music.load('No_mercy-Hipis.mp3')
pygame.mixer.music.play()

sleep(3)

image = pygame.image.load('evilscary.jpg')
window.blit(image, (4,3))
pygame.display.update()
sleep(3)
