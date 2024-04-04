import pygame
from brickout.game_globals import screen_width, screen_height

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('brickout/assets/ball.png')
        self.rect = self.image.get_rect()

        # Ball initial position (screen center)
        self.rect.centerx = screen_width / 2
        self.rect.centery = screen_height / 2

        # Ball speed
        self.speed= [3, 3]

    def update(self):
        # Boundaries collision detection
        # if self.rect.bottom >= screen_height or self.rect.top <= 0:
        if self.rect.top <= 0: # Check only top to allow player dead
            self.speed[1] = -self.speed[1]
        elif self.rect.right >= screen_width or self.rect.left <= 0:
            self.speed[0] = -self.speed[0]

        # Move
        self.rect.move_ip(self.speed)