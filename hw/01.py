import pygame
import pygame.draw
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 500))

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
pygame.draw.circle(screen, YELLOW, (250, 250), 100, 0)
rect(screen, BLACK, (200, 300, 100, 20), 0)

pygame.draw.circle(screen, RED, (200, 250), 30, 0)
pygame.draw.circle(screen, BLACK, (200, 250), 10, 0)
pygame.draw.circle(screen, RED, (300, 250), 30, 0)
pygame.draw.circle(screen, BLACK, (300, 250), 10, 0)
polygon(screen, BLACK, [(200, 200), (250, 250), (240, 250), (190,200)], 0)
polygon(screen, BLACK, [(300, 200), (250, 250), (260, 250), (310,200)], 0)
# polygon(screen, BLACK, [(256,206), (270,220), (305,195), (291,171)], 0)
# polygon(screen, BLACK, [(244,206), (230,220), (195,195), (209,171)], 0)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
