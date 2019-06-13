from constants import MAX_Y, MAX_X
from random import randint

class Food:

    #initilizing
    def __init__(self, window):
        self.window = window
        self.x = randint(1, MAX_X)
        self.y = randint(1, MAX_Y)
        self.fruit = '@'

    #rendering fruit
    def render(self):
        self.window.addstr(self.y, self.x, self.fruit)

    #Updating food loctaion
    def update(self):
        self.x = randint(1, MAX_X)
        self.y = randint(1, MAX_Y)
