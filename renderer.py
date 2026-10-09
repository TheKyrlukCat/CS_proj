import pygame
import main
from config import *

def render(obj, screen):
    pygame.Surface.blit(obj, screen)

def render_everything(screen):
    for obj in main.masses:
        pygame.Surface.blit(obj, screen)
