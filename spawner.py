from metor import Metor
import random

class Spawner:
    def __init__(self, screen_width, screen_height):
        self.num_metors = None
        self.metors = []
        self.height = screen_height
        self.width = screen_width
        self.round_num  = 1
        self.num_metors = None

    def spawn_next_round(self, round_num):

        self.num_metors = round_num
        self.round_num = round_num

        return self.spawn_metors()

    def spawn_metors(self):
        i=0
        while i < self.num_metors:

            pos = self.determine_pos()

            metor = Metor(pos[0], pos[1], 1)
            self.metors.append(Metor(pos[0], pos[1], self.round_num))

            i += 1

        metors_clone = self.metors
        self.metors = []
        return metors_clone

    def determine_pos(self):
        quadrient = random.randint(1,5)
        x_pos = None
        y_pos = None
        if quadrient == 1:
            x_pos = self.width * .75 + random.randint(0,self.width * .25)
            y_pos = 0 + random.randint(0, self.width * .25)
        elif quadrient == 2:
            x_pos = 0 + random.randint(0,self.width * .25)
            y_pos = 0 + random.randint(0,self.height * .25)
        elif quadrient == 3:
            x_pos = 0 + random.randint(0, self.width * .25)
            y_pos = self.height * .75 + random.randint(0, self.height)
        else:
            x_pos = self.width * .75 + random.randint(0, self.width * .25)
            y_pos = self.height * .75 + random.randint(0, self.height * .25)

        pos = []
        pos.append(x_pos)
        pos.append(y_pos)
        return pos
