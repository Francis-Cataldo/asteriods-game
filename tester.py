import pygame, sys
from object import Object
from metor import Metor
from bullet import Bullet
from player import Player


pygame.init()

game_running = True

mousex = 0
mousey = 0
move = False

def get_mouse_position():
    mousex, mousey = pygame.mouse.get_pos()

width = 800
height = 800
size = width, height

lives = 3

global screen
screen = pygame.display.set_mode(size)

o1 = Object(160, 160, 30, 30, [5,4])
o2 = Object(200, 200, 30, 30, [0,0])
m1 = Metor(500, 500, 3)
p = Player(400, 400)

objects = []
objects.append(o1)
objects.append(o2)
objects.append(m1)
objects.append(p)

print(o1.collide(o2))
m1.move(screen)

def game_over():
    sys.exit()

def respawn():
    p = Player(400, 400)
    objects.append(p)

while game_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            print(pygame.key.name(event.key))
            if (pygame.key.name(event.key) == 'space'):
                p.set_speed(5)
                move = True
            if (pygame.key.name(event.key) == 'w'):
                p.space_warp(width, height)


        elif event.type == pygame.KEYUP:
            if (pygame.key.name(event.key) == 'space'):
                if (p.get_speed() > 0):
                    p.set_speed(0)
        if (event.type == pygame.MOUSEBUTTONDOWN):
            bullet = p.fire()
            objects.append(bullet)


    if move:
        p.determine_velocity()

    screen.fill(0)
    for object in objects:
        if (object.is_player):
            pass
        else:
            object.move(screen)
    for object in objects:
        object.move(screen)

    i=0
    j=0
    while(i < len(objects)):
        while(j < len(objects)):
            if (not(objects[i] == objects[j])):
                if (objects[i].collide(objects[j])):
                    temp_object_1 = objects[i]
                    temp_object_2 = objects[j]
                    if (temp_object_1.type == "player"):
                        lives -= 1
                        print("die")
                        respawn()
                        if lives <= 0:
                            game_over()

                    if (temp_object_2.type == "player"):
                        lives -= 1
                        print("lives: " + str(lives))
                        respawn()
                        if lives <= 0:
                            print("done")
                            game_over()

                    for object in objects:
                        if object == temp_object_1 or object == temp_object_2:
                            objects.remove(object)


            j += 1
        i += 1




    pygame.display.flip()
