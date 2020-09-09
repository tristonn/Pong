import pygame as pg

from Settings import *

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (PLAYER_WIDTH, HEIGHT/2)
        self.pos = pg.math.Vector2(PLAYER_WIDTH, HEIGHT/2)
        self.vel = pg.math.Vector2(0, 0)
        self.score = 0

    def update(self):
        self.vel = pg.math.Vector2(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            self.vel.y = -PLAYER_VEL
        if keys[pg.K_DOWN]:
            self.vel.y = PLAYER_VEL
        self.pos += self.vel
        self.rect.center = self.pos

class Computer(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((COMPUTER_WIDTH, COMPUTER_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH - COMPUTER_WIDTH, HEIGHT/2)
        self.pos = pg.math.Vector2(WIDTH - COMPUTER_WIDTH, HEIGHT/2)
        self.vel = pg.math.Vector2(0, 0)
        self.score = 0

    def update(self):
        pass

class Ball(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((BALL_WIDTH, BALL_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = pg.math.Vector2(WIDTH/2, HEIGHT/2)
        self.vel = pg.math.Vector2(0, 0)
        self.acc = pg.math.Vector2(0, 0)
        self.dir = 1

    def update(self):
        self.vel.x = BALL_VEL * self.dir
        self.pos += self.vel
        self.rect.center = self.pos
