import pygame
import math
import sys
from player import Player
from spawner import Spawner
from object import Object
from bullet import Bullet
from metor import Metor
import pickle

pygame.init()

objects = []
mousex = 0
mousey = 0
width = 800
height = 800
size = width, height
lives = 3
font = pygame.font.Font('freesansbold.ttf', 32)
screen = pygame.display.set_mode(size)
game_running = True
move1 = False
s = Spawner(width, height)
round_num = 1
fire_cooldown = 0
score = 0


pygame.display.set_caption('Asteriods')

def game_over():
    if score > get_high_score():
        with open('score.bat', 'wb') as file:
            pickle.dump(score,file)
            print("New High Score!")
    else:
        print("All time high score is " + str(get_high_score()))



    sys.exit()

def respawn():
    global p
    p = Player(width/2, height/2)
    objects.append(p)

def display_score():
    text = font.render((str(score) + " " + str(lives) + " " + str(round_num )), True, (255, 255, 255))
    screen.blit(text, text.get_rect())


def collision():
    for object1 in objects:
        for object2 in objects:
            col = True
            if object1 == object2:
                col = True
            elif object1.collide(object2):

                if object1.type == "player" or object2.type == "player":

                    if object1.type == "bullet" or object2.type == "bullet":
                        col = False
                    else:
                        global lives
                        lives -= 1
                        respawn()
                        if lives <= 0:
                            game_over()
                elif object1.type == "metor" and object2.type == "metor":
                    col = False
                if col:
                    if object1.type == "metor" or object2.type == "metor":
                        global score
                        score += 100
                    objects.remove(object1)
                    objects.remove(object2)

def get_high_score():
    with open("score.bat", "rb") as file:
        high_score = pickle.load(file)
        return high_score
move1 = True
p = Player(width/2, height/2)
objects.append(p)
r = s.spawn_next_round(round_num)
for object in r:
    objects.append(object)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if pygame.key.name(event.key) == 'space':
                p.speed = 5
                move1 = True
            else:
                pass
            if pygame.key.name(event.key) == 'w':
                p.space_warp(width, height)

        elif event.type == pygame.KEYUP:
            if pygame.key.name(event.key) == 'space':
                if (p.speed > 0):
                    p.speed = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            if fire_cooldown <= 0:
                bullet = p.fire()
                objects.append(bullet)
                fire_cooldown = 15

    if move1:
        p.determine_velocity()



    screen.fill(0)
    num_metors = 0
    for object in objects:
        if object.type == "bullet":
            if object.life_span <= 0:
                objects.remove(object)
            else:
                object.life_span -= 1
        if object.type == "metor":
            num_metors += 1

        object.move(screen)

    collision()
    display_score()


    if num_metors == 0:
        round_num += 1
        for object_ in s.spawn_next_round(round_num):
            objects.append(object_)
    fire_cooldown -= 1

    pygame.display.flip()
