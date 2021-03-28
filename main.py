import pygame
import random
import time


FRAMERATE = 60
DELAY_TIME = 100 #delay between swaps in ms

WIDTH = 1000 # width in pixels 100 10px wide rectangles
HEIGHT = 700 # 500px for rectangles and 200px for buttons

RECT_HEIGHTS = []

pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))





running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    SCREEN.fill((255,255,255))
    pygame.display.flip()
    time.sleep(1/FRAMERATE)
