import sys
import pygame

def main():

# Game items
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
            if self.rect.bottom >= screen_height or self.rect.top <= 0:
                self.speed[1] = -self.speed[1]
            elif self.rect.right >= screen_width or self.rect.left <= 0:
                self.speed[0] = -self.speed[0]

            # Move
            self.rect.move_ip(self.speed)

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
            if event.key == pygame.K_LEFT:
                self.speed = [-5, 0]
            elif event.key == pygame.K_RIGHT:
                self.speed = [5, 0]
            else:
                self.speed = [0, 0]
            
            # Move
            self.rect.move_ip(self.speed)

# Game setup
    screen_width = 800
    screen_height = 600
    background = (0, 0, 64)

    screen = pygame.display.set_mode((screen_width, screen_height)) # screen size
    pygame.display.set_caption('Brickout') # window title
    clock = pygame.time.Clock() # game clock interval
    pygame.key.set_repeat(10) # adjust key repetition on press down

    ball = Ball()
    player = Paddle()

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

        # Paint elements in screen
        screen.fill(background)
        screen.blit(ball.image, ball.rect)
        screen.blit(player.image, player.rect)

        # Update screen items
        pygame.display.flip()


if __name__ == '__main__':
    main()