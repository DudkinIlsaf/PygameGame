import pygame
import sys
import random
import time


class Game():
    def __init__(self):
        self.screen_width = 720
        self.screen_height = 460

        self.red = pygame.Color(255, 0, 0)
        self.green = pygame.Color(0, 255, 0)
        self.black = pygame.Color(0, 0, 0)
        self.white = pygame.Color(255, 255, 255)
        self.brown = pygame.Color(165, 42, 42)

        self.fps_controller = pygame.time.Clock()

        self.score = 0