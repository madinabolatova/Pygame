import pygame as pg
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500


class Ball:
    BALL_SIZE = 25

    def get_random_change(self):
        change = random.randint(-2, 3)
        while change == 0:
            change = random.randint(-2, 3)
        return change

    def __init__(self):
        self.x = random.randint(self.BALL_SIZE, SCREEN_WIDTH - self.BALL_SIZE )
        self.y = random.randint(self.BALL_SIZE, SCREEN_HEIGHT - self.BALL_SIZE)
        self.change_x = self.get_random_change()
        self.change_y = self.get_random_change()
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def move(self):
        self.x += self.change_x
        self.y += self.change_y

        if self.x > SCREEN_WIDTH - self.BALL_SIZE or self.x < self.BALL_SIZE:
            self.change_x *= -1
        if self.y > SCREEN_HEIGHT - self.BALL_SIZE or self.y < self.BALL_SIZE:
            self.change_y *= -1


def main():
    pg.init()
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pg.display.set_mode(size)
    pg.display.set_caption("Ball Game")
    done = False
    clock = pg.time.Clock()
    ball_list = []
    ball = Ball()
    ball_list.append(ball)

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                ball_list.append(Ball())
        for ball in ball_list:
            ball.move()
        screen.fill(BLACK)
        for ball in ball_list:
            pg.draw.circle(screen, ball.color, [ball.x, ball.y], ball.BALL_SIZE)

        clock.tick(60)
        pg.display.flip()
    pg.quit()


main()