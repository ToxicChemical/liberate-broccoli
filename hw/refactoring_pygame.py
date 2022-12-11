import pygame.draw
from pygame.draw import *
import numpy as np

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 500))

DARK_GREEN = (1, 50, 32)
LIGHT_GREEN = (0, 128, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
LIGHT_BLUE = (66, 170, 255)
BROWN = (150, 75, 0)

def home(xh, yh, h):  
    '''
    Draws house
    xh, yh - left right corner coordinates
    h - 'size' coefficient
    '''
    rect(screen, (150, 75, 0), (xh, yh, 150 * h, 100 * h), 0)  # house
    polygon(screen, (255, 0, 0), [(xh + 150 * h / 2, yh - 100 * h / 2), (xh, yh), (xh + 150 * h, yh)], 0)  # roof
    rect(screen, (0, 191, 255), (xh + 50 * h, yh + 30 * h, 50 * h, 30 * h), 0)  # window


def tree(xt, yt, t):
    '''
    Draws tree
    xt, yt - left right corner coordinates
    t - 'size' coefficient
    '''
    rect(screen, BROWN, (xt, yt, 15 * t, 60 * t), 0)  # log
    circle(screen, DARK_GREEN, (xt + 15 * t / 2, yt - 30 * t), 30 * t)  # leaves
    circle(screen, (DARK_GREEN), (xt + 15 * t / 2 + 30 * t, yt - 30 * t + 15 * t), 30 * t)
    circle(screen, (DARK_GREEN), (xt + 15 * t / 2 - 30 * t, yt - 30 * t + 15 * t), 30 * t)
    circle(screen, (DARK_GREEN), (xt + 15 * t / 2 + 30 * t, yt - 30 * t - 20 * t), 30 * t)
    circle(screen, (DARK_GREEN), (xt + 15 * t / 2 - 30 * t, yt - 30 * t - 20 * t), 30 * t)
    circle(screen, (DARK_GREEN), (xt + 15 * t / 2, yt - 30 * t - 50 * t), 30 * t)


def cloud(xc, yc, c):
    '''
    Draws cloud

    xt, yt - left right cloud cofficient
    t - 'size' coefficient
    '''
    circle(screen, WHITE, (xc, yc), 30 * c, 0)
    circle(screen, (WHITE), (xc + 30 * c, yc + 30 * c), 30 * c, 0)
    circle(screen, (WHITE), (xc + 30 * c, yc - 30 * c), 30 * c, 0)
    circle(screen, (WHITE), (xc + 60 * c, yc), 30 * c, 0)
    circle(screen, (WHITE), (xc + 90 * c, yc + 30 * c), 30 * c, 0)
    circle(screen, (WHITE), (xc + 90 * c, yc - 30 * c), 30 * c, 0)
    circle(screen, (WHITE), (xc + 120 * c, yc), 30 * c, 0)


def sun(xs, ys, s):
    '''
    draws sun
    xs, ys - coordinates of sun center
    s - 'size' of sun
    '''
    circle(screen, YELLOW, (xs, ys), 30 * s)  # sun body

def draw_sky(color = LIGHT_BLUE):
    '''
    draws the shy. 
    by default color is blue-ish
    '''
    rect(screen, color, (0, 0, 500, 250), 0)  # sky

def draw_grass(color = LIGHT_GREEN):
    '''
    draws the grass. 
    by default color is green
    '''
    rect(screen, color, (0, 250, 500, 250), 0)  # grass

draw_sky()
draw_grass()
home(50, 270, 1.25)
home(300, 200, 0.75)
tree(300, 350, 1)
tree(450, 230, 0.75)
cloud(50, 50, 1)
cloud(230, 80, 0.5)
sun(450, 50, 1)
cloud(400, 80, 0.5)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
