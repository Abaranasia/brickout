import pygame
from brickout.game_globals import screen_width, screen_height
from brickout.objects.brick import Brick

# Wall
class Wall(pygame.sprite.Group):
    def __init__(self, brick_quantity, pos_x, pos_y ):
        pygame.sprite.Group.__init__(self)

        for i in range(brick_quantity):
            brick = Brick((pos_x,pos_y))
            self.add(brick)
            pos_x += brick.rect.width

            if pos_x >= screen_width:
                pos_x = 0
                pos_y += brick.rect.height