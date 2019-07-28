import pygame
import random
import math
from object import Object
from bullet import Bullet

class Player(Object):
    def __init__(self, x_pos, y_pos):
        self.width = 5
        self.height = 15
        self.velocity = []
        self.speed = 5
        self.thrusters = False
        self.velocity.append(0)
        self.velocity.append(0)

        Object.__init__(self, x_pos, y_pos, self.width, self.height, self.velocity)
        self.type = "player"


    def determine_velocity(self):

        mouse_position = pygame.mouse.get_pos()
        mousex = mouse_position[0]
        mousey = mouse_position[1]

        dx = mousex - self.x_pos
        dy = mousey - self.y_pos

        angle = math.atan2(dy, dx)

        self.velocity[0] = self.speed * math.cos(angle)
        self.velocity[1] = self.speed * math.sin(angle)

        return self.velocity

    def fire(self):
        bullet_speed = 30
        mouse_position = pygame.mouse.get_pos()
        mousex = mouse_position[0]
        mousey = mouse_position[1]

        dx = mousex - self.x_pos
        dy = mousey - self.y_pos

        angle = math.atan2(dy, dx)

        velocity = []
        velocity.append(bullet_speed * math.cos(angle))
        velocity.append(bullet_speed * math.sin(angle))


        return Bullet(self.x_pos, self.y_pos, velocity)
