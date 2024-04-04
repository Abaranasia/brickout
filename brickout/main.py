import sys
import time
import pygame

# Game items
screen_width = 800
screen_height = 600
background = (0, 0, 64)
text_color = (255, 255, 255)
initial_FPS = 125
start_level = 1

available_fonts = pygame.font.get_fonts()

def main():
    director = Director('BrickOut', (screen_width, screen_height))
    director.select_scene('level1')
    director.execute('level1')

class Director: 
    def __init__(self, title = "", res = (screen_width, screen_height)):
        pygame.init()

        # Screen initialization
        pygame.display.set_caption(title) # window title
        self.screen = pygame.display.set_mode(res) # screen size
        self.clock = pygame.time.Clock() # game clock interval
        self.current_level = start_level
        self.scene = None
        self.scenes = {}

    def execute(self, initial_scene, fps = initial_FPS):
        self.scene = self.scenes[initial_scene]
        playing = True

        while playing:
            self.clock.tick(fps) # Set FPS
            events = pygame.event.get() #Capture events

            # Check events
            for event in events:
                if event.type == pygame.QUIT:
                    playing = False
                    sys.exit()

            self.scene.event_handlers(events)
            self.scene.update()
            self.scene.display(self.screen)
            self.select_scene(self.scene.next_scene)

            if playing:
                playing = self.scene.playing

            pygame.display.flip()

        time.sleep(3)

    def select_scene(self, next_scene):
        if next_scene:
            if next_scene not in self.scenes:
                self.add_scene(next_scene)
            self.scene = self.scenes[next_scene]

    def add_scene(self, scene):
        scene_class = 'Scene_'+scene
        sceneObj = globals()[scene_class]
        self.scenes[scene] = sceneObj()

class Scene:
    def __init__(self):
        self.next_scene = False
        self.playing = True

    def event_handlers(self, events):
        pass

    def update(self):
        pass

    def display(self, screen):
        pass

    def screen_switch(self, scene):
        self.next_scene = scene

    def increase_level(self, current_level):
        return str(current_level + 1)
        
class Scene_level1(Scene):
    def __init__(self):
        Scene.__init__(self)

        self.bricks_counter = 20
        # Game element instances
        self.ball = Ball()
        self.player = Paddle()
        self.wall = Wall_easy(self.bricks_counter)
        self.current_level = 1


        self.player_score = 0
        self.player_lives = 3
        self.waiting_player = True

        pygame.key.set_repeat(10) # adjust key repetition on press down
    
    def event_handlers(self, events):
        # Check keypress events
        for event in events: 
            if event.type == pygame.KEYDOWN:
                self.player.update(event)
                if self.waiting_player == True and event.key == pygame.K_SPACE:
                    self.waiting_player = False
                    if self.ball.rect.centerx < screen_width / 2:
                        self.ball.speed = [3 ,-3]
                    else:
                        self.ball.speed = [-3 , -3]

    def update(self):
    # Update screen items

        # Update ball position
        if self.waiting_player == False: 
            self.ball.update()
        else: 
            self.ball.rect.midbottom = self.player.rect.midtop

        # Collision management
        if pygame.sprite.collide_rect(self.ball, self.player): # ball vs player
            self.ball.speed[1] = - self.ball.speed[1]
        
        collided_brick_list= pygame.sprite.spritecollide(self.ball, self.wall, False)
        if collided_brick_list: 
            collided_brick = collided_brick_list[0]
            cx = self.ball.rect.centerx
            if cx < collided_brick.rect.left or cx > collided_brick.rect.right:
                self.ball.speed[0] = - self.ball.speed[0]
            else: 
                self.ball.speed[1] = - self.ball.speed[1]
            self.wall.remove(collided_brick)  # Remove a sprite from a group
            self.player_score += 10
            self.bricks_counter -= 1
            print("bricks_counter", self.bricks_counter)
        
        # Check if ball rebase bottom boudary 
        if self.ball.rect.top > screen_height:
            self.player_lives -= 1
            self.waiting_player = True
        
        if self.bricks_counter <= 0:
            self.screen_switch('level_complete')
            time.sleep(2)
            next_level= 'level' + self.increase_level(self.current_level)
            self.screen_switch(next_level)

        if self.player_lives <= 0: 
            # game_over() 
            # self.playing = False
            self.screen_switch('game_over')
    
    def display(self, screen):
        # Paint elements in screen
        screen.fill(background)

        display_player_score(screen, self.player_score)
        display_player_lives(screen, self.player_lives)
        
        screen.blit(self.ball.image, self.ball.rect)
        screen.blit(self.player.image, self.player.rect)
        self.wall.draw(screen)

class Scene_level2(Scene):
    def __init__(self):
        Scene.__init__(self)

        self.bricks_counter = 60
        # Game element instances
        self.ball = Ball()
        self.player = Paddle()
        self.wall = Wall_middle(self.bricks_counter)


        self.player_score = 0
        self.player_lives = 3
        self.waiting_player = True

        pygame.key.set_repeat(10) # adjust key repetition on press down
    
    def event_handlers(self, events):
        # Check keypress events
        for event in events: 
            if event.type == pygame.KEYDOWN:
                self.player.update(event)
                if self.waiting_player == True and event.key == pygame.K_SPACE:
                    self.waiting_player = False
                    if self.ball.rect.centerx < screen_width / 2:
                        self.ball.speed = [3 ,-3]
                    else:
                        self.ball.speed = [-3 , -3]

    def update(self):
    # Update screen items

        # Update ball position
        if self.waiting_player == False: 
            self.ball.update()
        else: 
            self.ball.rect.midbottom = self.player.rect.midtop

        # Collision management
        if pygame.sprite.collide_rect(self.ball, self.player): # ball vs player
            self.ball.speed[1] = - self.ball.speed[1]
        
        collided_brick_list= pygame.sprite.spritecollide(self.ball, self.wall, False)
        if collided_brick_list: 
            collided_brick = collided_brick_list[0]
            cx = self.ball.rect.centerx
            if cx < collided_brick.rect.left or cx > collided_brick.rect.right:
                self.ball.speed[0] = - self.ball.speed[0]
            else: 
                self.ball.speed[1] = - self.ball.speed[1]
            self.wall.remove(collided_brick)  # Remove a sprite from a group
            self.player_score += 10
            self.bricks_counter -= 1
            print("bricks_counter", self.bricks_counter)
        
        # Check if ball rebase bottom boudary 
        if self.ball.rect.top > screen_height:
            self.player_lives -= 1
            self.waiting_player = True
        
        if self.bricks_counter <= 0:
            self.screen_switch('level_complete')

        if self.player_lives <= 0: 
            # game_over() 
            # self.playing = False
            self.screen_switch('game_over')
    
    def display(self, screen):
        # Paint elements in screen
        screen.fill(background)

        display_player_score(screen, self.player_score)
        display_player_lives(screen, self.player_lives)
        
        screen.blit(self.ball.image, self.ball.rect)
        screen.blit(self.player.image, self.player.rect)
        self.wall.draw(screen)

class Scene_level_complete(Scene):
    def update(self):
        self.playing = False    

    def display(self, screen):
        self.message_font = pygame.font.SysFont(available_fonts[0], 72)
        self.message = self.message_font.render('Level completed! ', True, text_color)
        self.message_rect = self.message.get_rect()
        self.message_rect.center = [screen_width / 2, screen_height / 2]
        screen.blit(self.message, self.message_rect)

class Scene_game_over(Scene):
    def update(self):
        self.playing = False

    def display(self, screen):
        self.message_font = pygame.font.SysFont(available_fonts[0], 72)
        self.message = self.message_font.render('Game over :/ ', True, text_color)
        self.message_rect = self.message.get_rect()
        self.message_rect.center = [screen_width / 2, screen_height / 2]
        screen.blit(self.message, self.message_rect)

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
class Wall_easy(pygame.sprite.Group):
    def __init__(self, brick_quantity ):
        pygame.sprite.Group.__init__(self)

        pos_x = 0
        pos_y = 125
        for i in range(brick_quantity):
            brick = Brick((pos_x,pos_y))
            self.add(brick)
            pos_x += brick.rect.width

            if pos_x >= screen_width:
                pos_x = 0
                pos_y += brick.rect.height

class Wall_middle(pygame.sprite.Group):
    def __init__(self, brick_quantity ):
        pygame.sprite.Group.__init__(self)

        pos_x = 0
        pos_y = 25
        for i in range(brick_quantity):
            brick = Brick((pos_x,pos_y))
            self.add(brick)
            pos_x += brick.rect.width

            if pos_x >= screen_width:
                pos_x = 0
                pos_y += brick.rect.height

# Player score logic
def display_player_score(screen, player_score):
    score_font = pygame.font.SysFont(available_fonts[2], 20)
    score_text = "Score: " + str(player_score).zfill(5)
    score = score_font.render(score_text, True, text_color)
    score_rect = score.get_rect()
    score_rect.topleft =  [0, 0]
    screen.blit(score, score_rect)

# Player lives logic
def display_player_lives(screen, player_lives):
    lives_font = pygame.font.SysFont(available_fonts[2], 20)
    lives_text = "Lives: " + str(player_lives).zfill(2)
    lives = lives_font.render(lives_text, True, text_color)
    lives_rect = lives.get_rect()
    lives_rect.topright =  [screen_width, 0]
    screen.blit(lives, lives_rect)
    
if __name__ == '__main__':
    main()