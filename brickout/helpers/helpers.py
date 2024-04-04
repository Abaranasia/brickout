import pygame
from brickout.game_globals import *

available_fonts = pygame.font.get_fonts()

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