import pygame
import os
import random
from sys import exit
pygame.init()
window = pygame.display.set_mode((800,800)) # create game screen
game_title = pygame.display.set_caption("Flappy Bird") # create game title
framerate = 60
run_time = pygame.time.Clock().tick(framerate)
running = True
color = (152,245,255)
Bird_x = 50
Bird_y = 400
Bird_vel = 0
Bird_gra = 0.1  
top_pipe1_x = 200
top_pipe2_x = 500
top_pipe3_x = 800
bot_pipe_y = 800
pipe_width = 50
pipe_moving_v = 1
ground_w = 800
ground_h = 50
top_pipe1_height = random.randint(100,550)
top_pipe2_height = random.randint(100,550)
top_pipe3_height = random.randint(100,550)
pipe_distance = 250
font1 = pygame.font.SysFont("Arial",20)
score = 0
pipe1_pass = False
pipe2_pass = False
pipe3_pass = False
music = pygame.mixer.Sound(
    os.path.join("bg_bird","no6.wav"))
# score_text = font1.render(f"Score: {score}", True, "BLACK")
# loading background image and transform
background_image = pygame.transform.scale(pygame.image.load(
    os.path.join("bg_bird", "bg.png")),(800,800))
# Loading and transform bottom ground
ground_image = pygame.transform.scale(pygame.image.load(
    os.path.join("bg_bird", "ground.png")),(ground_w,ground_h))
# Loading bird image and transform
Bird_image = pygame.transform.scale(
    pygame.image.load(os.path.join("bg_bird","bird.png")),(70,70))
# Loading and transform game over image
game_over = pygame.transform.scale(pygame.image.load(
    os.path.join("bg_bird","gameover.png")),(400,400))
#Top pipe images load and transform
Top_pipe1 = pygame.transform.scale(
    pygame.image.load(os.path.join("top_pipe","tube.png")),(pipe_width,top_pipe1_height))
Top_pipe2 = pygame.transform.scale(
    pygame.image.load(os.path.join("top_pipe","tube.png")),(pipe_width,top_pipe2_height))
Top_pipe3 = pygame.transform.scale(
    pygame.image.load(os.path.join("top_pipe","tube.png")),(pipe_width,top_pipe3_height))
#Bottom pipe images load and transform
Bot_pipe1 = pygame.transform.scale(
    pygame.image.load(os.path.join("bottom_pipe","red_bot.png")),(pipe_width,800-top_pipe1_height- pipe_distance + ground_h))
Bot_pipe2 = pygame.transform.scale(
    pygame.image.load(os.path.join("bottom_pipe","red_bot.png")),(pipe_width,800-top_pipe2_height- pipe_distance + ground_h))
Bot_pipe3 = pygame.transform.scale(
    pygame.image.load(os.path.join("bottom_pipe","red_bot.png")),(pipe_width,800-top_pipe3_height- pipe_distance +ground_h))
while running:
    pygame.mixer.Sound.play(music)
    run_time
    window.fill(color)
    window.blit(background_image,(0,0))
    # Draw top pipes
    Top_pipe1_draw = window.blit(Top_pipe1,(top_pipe1_x,0))
    Top_pipe2_draw = window.blit(Top_pipe2,(top_pipe2_x,0))
    Top_pipe3_draw = window.blit(Top_pipe3,(top_pipe3_x,0))
    # Draw bottom pipes
    Bot_pipe1_draw = window.blit(Bot_pipe1,(top_pipe1_x,top_pipe1_height + pipe_distance))
    Bot_pipe2_draw = window.blit(Bot_pipe2,(top_pipe2_x,top_pipe2_height + pipe_distance))
    Bot_pipe3_draw = window.blit(Bot_pipe3,(top_pipe3_x,top_pipe3_height + pipe_distance))
    # Draw bottom ground
    ground = window.blit(ground_image,(0,750))
    # Draw score
    score_text = font1.render(f"Score: {score}", True, "BLACK")
    window.blit(score_text,(30,30))
    # Draw pipe moving
    top_pipe1_x -= pipe_moving_v
    top_pipe2_x -= pipe_moving_v
    top_pipe3_x -= pipe_moving_v
    # Draw more pipes after moving 3 pipes completed
    if top_pipe1_x < - pipe_width:
        top_pipe1_x = 850
        pipe1_pass =False
    if top_pipe2_x < - pipe_width:
        top_pipe2_x = 850
        pipe1_pass =False
    if top_pipe3_x < - pipe_width:
        top_pipe3_x = 850
        pipe1_pass =False
    # Draw bird:
    Bird_draw = window.blit(Bird_image,(Bird_x,Bird_y))
    # Dropping Bird:
    Bird_y += Bird_vel
    Bird_vel += Bird_gra 
    # Check collide
    pipes = [Top_pipe1_draw,Top_pipe2_draw,Top_pipe3_draw,Bot_pipe1_draw,
    Bot_pipe2_draw,Bot_pipe3_draw, ground]
    for pipe in pipes:
        if Bird_draw.colliderect(pipe):
            pygame.mixer.pause()
            pipe_moving_v = 0
            Bird_vel = 0
            window.blit(game_over,(200,200))
    # Check Score
    if top_pipe1_x + pipe_width <= Bird_x and pipe1_pass == False:
        score += 1
        pipe1_pass = True
    if top_pipe2_x + pipe_width <= Bird_x and pipe2_pass == False:
        score += 1
        pipe2_pass = True
    if top_pipe3_x + pipe_width <= Bird_x and pipe3_pass == False:
        score += 1
        pipe3_pass = True
       
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit() 
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Bird_vel = 0
                Bird_vel -=4
    pygame.display.update() # (can use display.flip())update portions of the screen for game display   
  