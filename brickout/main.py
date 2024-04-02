import sys
import time
import pygame

def main():
    
# Game items
    screen_width = 800
    screen_height = 600
    background = (0, 0, 64)
    
    pygame.init()
    
# Ball
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

# Brick
    class Brick(pygame.sprite.Sprite):
        def __init__(self, position):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('brickout/assets/brick.png')
            self.rect = self.image.get_rect()

            # Brick initial position
            self.rect.topleft = position

# Wall
    class Wall(pygame.sprite.Group):
        def __init__(self, brick_quantity ):
            pygame.sprite.Group.__init__(self)

            pos_x = 0
            pos_y = 20
            for i in range(brick_quantity):
                brick = Brick((pos_x,pos_y))
                self.add(brick)
                pos_x += brick.rect.width

                if pos_x >= screen_width:
                    pos_x = 0
                    pos_y += brick.rect.height

# Game over logic
    def game_over():
        available_fonts= pygame.font.get_fonts()
        message_font = pygame.font.SysFont(available_fonts[0], 72)
        message = message_font.render('Game over :/ ', True, (255, 255, 255))
        message_rect = message.get_rect()
        message_rect.center = [screen_width / 2, screen_height / 2]
        screen.blit(message, message_rect)
        pygame.display.flip()
        time.sleep(3)
        sys.exit()

# Game setup
    screen = pygame.display.set_mode((screen_width, screen_height)) # screen size
    pygame.display.set_caption('Brickout') # window title
    clock = pygame.time.Clock() # game clock interval
    pygame.key.set_repeat(10) # adjust key repetition on press down

    # Game element instances
    ball = Ball()
    player = Paddle()
    wall = Wall(120)

# Game logic
    while True:
        # Set FPS
        clock.tick(60)

        # Check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                player.update(event)
        
        # Update ball position
        ball.update()

        # Collision management
        if pygame.sprite.collide_rect(ball, player): # ball vs player
            ball.speed[1] = - ball.speed[1]
        
        collided_brick_list= pygame.sprite.spritecollide(ball, wall, False)
        if collided_brick_list: 
            collided_brick = collided_brick_list[0]
            cx = ball.rect.centerx
            if cx < collided_brick.rect.left or cx > collided_brick.rect.right:
                ball.speed[0] = - ball.speed[0]
            else: 
                ball.speed[1] = - ball.speed[1]
            wall.remove(collided_brick)  # Remove a sprite from a group 
        
        # Check if ball rebase bottom boudary 
        if ball.rect.top > screen_height:
            game_over()

        # Paint elements in screen
        screen.fill(background)
        screen.blit(ball.image, ball.rect)
        screen.blit(player.image, player.rect)
        wall.draw(screen)
        
        # Update screen items
        pygame.display.flip()


if __name__ == '__main__':
    main()