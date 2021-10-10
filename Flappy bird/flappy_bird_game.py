import pygame
from sys import *
import time
import random
from pygame import mixer

#defining FPS
def fps():
    fps = "FPS: " + str(int(clock.get_fps()))
    return fps

#score
score = 0

#initializing application
pygame.init()

flappy1 = pygame.image.load('assets/flappy1.png')
flappy2 = pygame.image.load('assets/flappy2.png')
flappy1_flip = pygame.image.load('assets/flappy1_flip.png')
flappy2_flip = pygame.image.load('assets/flappy2_flip.png')
flappy1_r = pygame.image.load('assets/flappy1_r.png')
flappy2_r = pygame.image.load('assets/flappy2_r.png')
flappy1_flip_r = pygame.image.load('assets/flappy1_flip_r.png')
flappy2_flip_r = pygame.image.load('assets/flappy2_flip_r.png')
bamboo_upper = pygame.image.load('assets/bamboo_upper.png')
bamboo_lower = pygame.image.load('assets/bamboo_lower.png')
background = pygame.image.load('assets/bg2.png')
tree_far = pygame.image.load('assets/tree.png')
tree_near = pygame.image.load('assets/tree2.png')
ground = pygame.image.load ('assets/land.png')
font = pygame.font.Font('assets/ariel.ttf', 15)
screen = pygame.display.set_mode((640, 360))

#scaling images
flappy1 = pygame.transform.scale(flappy1, (64, int(385/8)))
flappy2 = pygame.transform.scale(flappy2, (64, int(420/8)))
flappy1_flip = pygame.transform.scale(flappy1_flip, (64, int(385/8)))
flappy2_flip = pygame.transform.scale(flappy2_flip, (64, int(420/8)))


mixer.init()
mixer.music.load("assets/song.wav")
mixer.music.set_volume(0.7)

#final font
dir_font = font.render('Click on flappy to select your flappy', False, 'White')

#bird selection
flappy_selection = 0
flappy = [flappy1, flappy2, flappy1_flip, flappy2_flip]

#flappy bird selection window
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] >= 181 and pygame.mouse.get_pos()[0] < 245 and pygame.mouse.get_pos()[1] >= 193 and pygame.mouse.get_pos()[1] < 257:
                flappy_selection = flappy[0]
                mixer.music.play()
                break
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] >= 394 and pygame.mouse.get_pos()[0] < 458 and pygame.mouse.get_pos()[1] >= 193 and pygame.mouse.get_pos()[1] < 257:
                flappy_selection = flappy[1]
                mixer.music.play()
                break
    screen.blit(background, (0, 0))
    screen.blit(ground, (0, 335))
    screen.blit(dir_font, dir_font.get_rect(center=(640/2, 80)))
    screen.blit(flappy1, flappy1.get_rect(center=(640/3, 225)))
    screen.blit(flappy2, flappy2.get_rect(center=(1280/3, 225)))
    if (flappy_selection):
        break
    pygame.display.update()
mixer.music.load("assets/chirp.wav")

#flappy position
flappy_pos = [100, 180]

#fps update
font = pygame.font.Font('assets/ariel.ttf', 10)
clock = pygame.time.Clock()

#gravity
gravity = 0.05
try:
    gravity = 4/int(clock.get_fps())
except:
    gravity = 5/100
velocity = 0

#flappy texture update
background = pygame.image.load('assets/bg2.png')
flappy_new = [flappy1, flappy2, flappy1_flip, flappy2_flip]
flappy_new[0] = pygame.transform.scale(flappy1_r, (32, 24))
flappy_new[1] = pygame.transform.scale(flappy2_r, (32, 26))
flappy_new[2] = pygame.transform.scale(flappy1_flip_r, (32, 24))
flappy_new[3] = pygame.transform.scale(flappy2_flip_r, (32, 26))
mixer.music.play()

#bamboo position
def bamboo_pos():
    return -1*(random.randint(150, 200))
spawn_time = 0
bamboo_x = []
upper_bamboo_y = []
lower_bamboo_y = []

#flag
flag = 0

tree_far_x = [500, -220]
tree_near_x = [100, -230]

score_ = pygame.font.Font('assets/ariel.ttf', 17)
#starting main game
while 1:
    screen.blit(background, (0, 0))
    if (tree_far_x[0] <= 640):
        if (tree_far_x[0] < -640):
            tree_far_x[0] = random.randint(800, 1200)
        else:
            screen.blit(tree_far, tree_far_x)
    if (tree_near_x[0] <= 640):
        if (tree_near_x[0] < -640):
            tree_near_x[0] = random.randint(640, 1000)
        else:
            screen.blit(tree_near, tree_near_x)
    tree_far_x[0] -= 1
    tree_near_x[0] -= 1

    if (spawn_time == 0):
        y = bamboo_pos()
        upper_bamboo_y.append(y)
        bamboo_x.append(640)
        lower_bamboo_y.append(y+100+310)
        spawn_time = 300
    
    if len(bamboo_x) >= 1:
        bamboo_x[0]-=1 
        screen.blit(bamboo_upper, [bamboo_x[0], upper_bamboo_y[0]])
        screen.blit(bamboo_lower, [bamboo_x[0], lower_bamboo_y[0]])
        if bamboo_x[0] == -30:
            bamboo_x.pop(0)
            lower_bamboo_y.pop(0)
            upper_bamboo_y.pop(0)

    if len(bamboo_x) >= 2:
        bamboo_x[1]-=1 
        screen.blit(bamboo_upper, [bamboo_x[1], upper_bamboo_y[1]])
        screen.blit(bamboo_lower, [bamboo_x[1], lower_bamboo_y[1]])
        if bamboo_x[1] == -30:
            bamboo_x.pop(1)
            lower_bamboo_y.pop(1)
            upper_bamboo_y.pop(1)

    if len(bamboo_x) == 3:
        bamboo_x[2]-=1 
        screen.blit(bamboo_upper, [bamboo_x[2], upper_bamboo_y[2]])
        screen.blit(bamboo_lower, [bamboo_x[2], lower_bamboo_y[2]])
        if bamboo_x[2] == -30:
            bamboo_x.pop(2)
            lower_bamboo_y.pop(2)
            upper_bamboo_y.pop(2)


    if bamboo_x[0] == 100 and ((flappy_pos[1] >= upper_bamboo_y[0] and flappy_pos[1] < upper_bamboo_y[0]+310) or (flappy_pos[1] >= lower_bamboo_y[0] and flappy_pos[1] < lower_bamboo_y[0]+310)):
        break
    spawn_time-=1
    score_font = score_.render(str(int(score)), False, 'White')
    score += 0.01
    screen.blit(score_font, [0,0])
    #play background music
    if mixer.music.get_pos() >= 7990:
        mixer.music.play()
    
    #screening fps
    fps_update = font.render(fps(), False, 'Black')
    screen.blit(fps_update, (600,0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                flag = 1
            while flag:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    if event.key == pygame.K_SPACE:
                        flag = 0
                        break
            if event.key == pygame.K_SPACE and flappy_pos[1] != 0:
                velocity -= 4
    flappy_pos[1] += velocity
    velocity+=gravity

    #adding border to window
    if flappy_pos[1] <= 0:
        flappy_pos[1] = 0
    elif flappy_pos[1] > 320:
        flappy_pos[1] = 317

    #flapping wings
    if velocity < 0:
        if flappy_selection == flappy[0]:
            screen.blit(flappy_new[2], flappy_pos)
        else:
            screen.blit(flappy_new[3], flappy_pos)
    else:
        if flappy_selection == flappy[0]:
            screen.blit(flappy_new[0], flappy_pos)
        else:
            screen.blit(flappy_new[1], flappy_pos)
    screen.blit(ground, (0, 335))
    
    pygame.display.update()
    clock.tick(100)

font = pygame.font.Font('assets/ariel.ttf', 17)
dir_font = font.render('That little bird was flying to feed her chicks and you killed her. You evil', False, 'White')
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(dir_font, [30,100])
    pygame.display.update()
            

