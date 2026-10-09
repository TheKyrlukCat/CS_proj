from config import *
import pygame
from math import *


def grav_compute(stage_masses):
    #this assumes the player has already set its movement deltas for this tick
    #also the player is a type of mass, so it falls into the input list, at [0]
    for mass in stage_masses:
        for mass2 in stage_masses:
            if mass != mass2: #prevent masses from pulling themselves and crashing
                mass.pull(mass2)

class Planet:
    def __init__(self, x, y, radius, mass, surf=True):
        self.x = x
        self.y = y
        self.rad = radius
        self.surf = surf
        self.mass = mass
        self.dx = 0
        self.dy = 0
        pygame.sprite.Sprite.__init__(self)
        self.tex = pygame.image.load("kenney_planets/Planets/planet00.png").convert_alpha()

    def pull(self, pulled):
        pass
        '''
        for obj in pulled:
            angle = atan2(pulled.y - self.y, pulled.x - self.x)
            pull = gravconst * self.mass * pulled.mass / sqrt((self.x - pulled.x) ** 2 + (self.y - pulled.y) ** 2)
            pulled.dx = cos(angle)*pull
            pulled.dy = sin(angle)*pull'''