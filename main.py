import sys
import pygame

# Basic setup
width = 800
heigth = 600
screen = pygame.display.set_mode((width, heigth))
pygame.display.set_caption('Brickout')

while True:
    # Check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()
