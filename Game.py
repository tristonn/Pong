import pygame as pg

from Sprites import *
from Settings import *

class Game:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.font = pg.font.SysFont(None, SCORE_SIZE)
        self.playing = True
        self.running = True

    def new(self):
        self.player = Player()
        self.computer = Computer()
        self.ball = Ball()

        self.players = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()

        self.all_sprites.add(self.player)
        self.players.add(self.player)
        self.all_sprites.add(self.computer)
        self.players.add(self.computer)
        self.all_sprites.add(self.ball)

        self.run()

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def update(self):
        self.all_sprites.update()
        if pg.sprite.spritecollide(self.ball, self.players, False):
            self.ball.dir *= -1
        if self.ball.pos.x >= WIDTH - BALL_WIDTH:
            self.player.score += 1
            self.ball.pos = pg.math.Vector2(WIDTH/2, HEIGHT/2)
        if self.ball.pos.x <= BALL_WIDTH:
            self.computer.score += 1
            self.ball.pos = pg.math.Vector2(WIDTH/2, HEIGHT/2)

    def draw(self):
        self.window.fill(BLACK)
        pg.draw.line(self.window, WHITE, (WIDTH/2, 0), (WIDTH/2, HEIGHT), 5)
        self.player_text = self.font.render(str(self.player.score), True, WHITE)
        self.computer_text = self.font.render(str(self.computer.score), True, WHITE)
        self.all_sprites.draw(self.window)
        self.window.blit(self.player_text, (WIDTH/2 - SCORE_SIZE, SCORE_SIZE))
        self.window.blit(self.computer_text, (WIDTH/2 + (SCORE_SIZE/1.5), SCORE_SIZE))
        pg.display.flip()

def main():
    g = Game()
    while g.running:
        g.new()
    pg.quit()

if __name__ == "__main__":
    main()
