from config import *
import pygame

class Planet:
    def __init__(self, x, y, radius, mass, surf=True):
        self.x = x
        self.y = y
        self.rad = radius
        self.surf = surf
        self.mass = mass
        self.dx = 0
        self.dy = 0

    def pull(self, pulled):
        for obj in pulled:
            pull = gravconst * self.mass * pulled.mass / sqrt((self.x - pulled.x) ** 2 + (self.y - pulled.y) ** 2)
            self.dx =