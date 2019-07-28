import pygame
import random
from object import Object
import math

class Metor(Object):
    def __init__(self, x_pos, y_pos, size):
        if (size == 1):
            self.width = 75
            self.height = 75
        elif (size == 2):
            self.width = 50
            self.height = 50
        else:
            self.width = 25
            self.height = 25

        self.velocity = []
        self.velocity.append(random.randint(-10, 11))
        self.velocity.append(random.randint(-10, 11))
        # self.velocity.append(0)
        # self.velocity.append(0)
        self.x_pos = x_pos
        self.y_pos = y_pos
        Object.__init__(self, self.x_pos, self.y_pos, self.width, self.height, self.velocity)
        self.type = "metor"
