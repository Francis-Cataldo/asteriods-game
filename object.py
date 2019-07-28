import pygame
import random

class Object:
    def __init__(self, x_pos, y_pos, width, height, velocity):
        self.height = height
        self.width = width
        self.y_pos = y_pos
        self.x_pos = x_pos

        self.velocity = velocity
        self.type = "object"



    def collide(self, object):
        if (self.x_pos < object.x_pos + object.width and
            self.x_pos + self.width > object.x_pos and
            self.y_pos < object.y_pos + object.height and
            self.y_pos + self.height > object.y_pos):
            return True
        return False
    def move(self, screen):
        self.x_pos += self.velocity[0]
        self.y_pos += self.velocity[1]
        if (self.x_pos >= 800):
            self.x_pos = 10
        if (self.x_pos <= 0):
            self.x_pos = 790
        if (self.y_pos >= 800):
            self.y_pos = 10
        if (self.y_pos <= 0):
            self.y_pos = 790


        pygame.draw.rect(screen, (255, 255, 255), [self.x_pos, self.y_pos, self.width, self.height])
