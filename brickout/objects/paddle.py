import pygame
from brickout.game_globals import screen_width, screen_height

# Paddle
class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('brickout/assets/paddle.png')
        self.rect = self.image.get_rect()

        # Paddle initial position (screen center)
        self.rect.midbottom = (screen_width / 2, screen_height -20)

        # Paddle speed
        self.speed= [0, 0]

    def update(self, event):
        # Player event handlers
        if event.key == pygame.K_LEFT and self.rect.left > 0:
            self.speed = [-5, 0]
        elif event.key == pygame.K_RIGHT  and self.rect.right < screen_width:
            self.speed = [5, 0]
        else:
            self.speed = [0, 0]
        
        # Move
        self.rect.move_ip(self.speed)