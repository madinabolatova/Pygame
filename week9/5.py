import pygame as pg

pg.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

size = (700, 500)

display = pg.display.set_mode(size)

pg.display.set_caption("Pygame example")

clock = pg.time.Clock()

colors = [WHITE, BLUE, GREEN, RED]

color = WHITE

x = 100
y = 100
dx = 1
dy = 0

done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        if event.type == pg.KEYDOWN and event.key == pg.K_UP:
            dx = 0
            dy = -1
        if event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
            dx = 0
            dy = 1
        if event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
            dx = 1
            dy = 0
        if event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
            dx = -1
            dy = 0
    display.fill(BLACK)
    x += dx
    y += dy

    if x > 700:
        x = 0
    if x < 0:
        x = 700
    if y > 500:
        y = 0
    if y < 0:
        y = 500
    pg.draw.ellipse(display, color, [x, y, 20, 20])
    clock.tick(60)
    pg.display.update()

pg.quit()