import math
import random

import pygame


FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface, x, y):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """

        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = random.choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.x += self.vx
        if (self.y == 0 and self.vy <= 0.5):
            self.vy = 0
            return
        self.y -= self.vy
        self.vy -= 0.5
        if(self.x <= 0):
            self.x = 0
            self.vx = -self.vx / 4
        if(self.x >= 800):
            self.x = 800
            self.vx = -self.vx / 4
        if(self.y <= 0):
            self.y = 0
            self.vy = -self.vy / 4
        if(self.y >= 600):
            self.y = 600
            self.vy = -self.vy / 4
    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        dx = obj.x - self.x
        dy = obj.y - self.y
        return (abs(dx*dx + dy*dy) <= (obj.r + self.r) ** 2)

class Gun:
    def __init__(self, screen, x = 10):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.x = x 
        self.y = 500 
        self.v = 10

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen, self.x, self.y)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        pygame.draw.line(screen, self.color, (self.x + 20, self.y), (self.x + (20 + self.f2_power) * math.cos(self.an), self.y + (20 + self.f2_power) * (math.sin(self.an))), 5)
        pygame.draw.rect(self.screen,self.color, (self.x, self.y, 30, 30))
        pygame.draw.circle(self.screen, BLACK, (self.x + 30, self.y + 30), 10)
        pygame.draw.circle(self.screen, BLACK, (self.x, self.y + 30), 10)
    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY
    def move_L(self):
        print('1')
        self.x -= self.v
    def move_R(self):
        self.x += self.v


class Target:
    # self.points = 0
    # self.live = 1
    #don't work!!! How to call this functions when object is created?
    # self.new_target()

    def __init__(self):
        self.points = 0
        self.live = 1
        self.x=self.y=self.r=0
        self.color = RED
        self.new_target()
        self.vx = random.randint(5,10);
        self.vy = random.randint(5, 20)
        
    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = random.randint(600, 780)
        y = self.y = random.randint(300, 550)
        r = self.r = random.randint(20, 50)
        color = self.color = RED

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points
    def draw(self):
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.r, 0)    


    def move(self):
        """Переместить цель по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy,
        и стен по краям окна (размер окна 800х600).
        """
        self.y += self.vy
        if(self.y <= self.r):
            self.y = self.r
            self.vy = -self.vy
        if(self.y >= 700 - self.r):
            self.y = 700 - self.r
            self.vy = -self.vy
    def move_new(self): #same
        self.x += self.vx
        self.y += self.vy
        if(self.x <= 0):
            self.x = 0
            self.vx = -self.vx
        if(self.x >= 700):
            self.x = 700
            self.vx = -self.vx
        if(self.y <= 0):
            self.y = 0
            self.vy = -self.vy
        if(self.y >= 500):
            self.y = 500
            self.vy = -self.vy

F_D = F_A = 0
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
target_1 = Target()
target_2 = Target()
targets = [target_1, target_2]
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    target_1.draw()
    target_2.draw()
    for b in balls:
        b.draw()
    pygame.display.update()
    F = 0
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                F_D = 1
            if event.key == pygame.K_a:
                F_A = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                F_D = 0
            if event.key == pygame.K_a:
                F_A = 0 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
          
    if F_D == 1:
        gun.move_R()
    if F_A == 1:
        gun.move_L()
    for b in balls:
        b.move()
        if b.hittest(target_1) and target_1.live:
            target_1.live = 0
            target_1.hit()
            target_1.new_target()
            target_1.live = 1

        if b.hittest(target_2) and target_2.live:
            target_2.live = 0
            target_2.hit()
            target_2.new_target()
            target_2.live = 1
    target_1.move()
    target_2.move_new()
    gun.power_up()

pygame.quit()