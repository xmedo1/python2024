import sys
import pygame

# Consts
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SIZE = (800, 600)
WIN_SCORE = 11

# Init
pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Ping pong game')

# Clock
FPS=60
clock = pygame.time.Clock()

