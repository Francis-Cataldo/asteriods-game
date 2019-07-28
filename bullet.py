import pygame
import math
from object import Object

class Bullet(Object):
    def __init__(self, x_pos, y_pos, velocity):
        self.size = 5

        Object.__init__(self, x_pos, y_pos, self.size, self.size, velocity)
        self.type = "bullet"
        self.life_span = 25
