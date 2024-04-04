import pygame

# Brick
class Brick(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('brickout/assets/brick.png')
        self.rect = self.image.get_rect()

        # Brick initial position
        self.rect.topleft = position