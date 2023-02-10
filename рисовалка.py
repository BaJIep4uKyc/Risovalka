import random

import pygame as pg

WHITE = [225]*3
YELLOW = [0, 225, 225]
RED = [225, 0, 0]
GREEN = [0, 225, 0]
BLUE = [0, 0, 225]
color_list = [YELLOW, RED, GREEN, BLUE]
W, H = 500, 500
pg.init()
win = pg.display.set_mode((W, H))
pg.display.set_caption('Paintilka')

flag = 1
size = 30
object_to_draw = 'circle'

class Circle:
    def __init__(self, x, y, rad, color):
        self.x = x
        self.y = y
        self.rad = rad
        self.color = color
        self.flag = flag

    def clean(self):
        win.fill(WHITE)

win.fill(WHITE)
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    pos = pg.mouse.get_pos()
    key = pg.key.get_pressed()
    if key[pg.K_SPACE]:
        win.fill(WHITE)
    elif key[pg.K_w]:
        object_to_draw = 'rect'
    elif key[pg.K_q]:
        object_to_draw = 'circle'

    pg.display.update()
    size += flag
    if size > 200:
        flag = -1
    if size < 50:
        flag = 1
    if object_to_draw == 'circle':
        pg.draw.circle(win, random.choices(range(0, 256), k=3), \
                       pg.mouse.get_pos(), size // 2)
    elif object_to_draw == 'rect':
        x, y = pg.mouse.get_pos()
        pg.draw.rect(win, random.choices(range(0, 256), k=3), \
                     (x - size // 2, y - size // 2, size, size))
    pg.time.delay(10)
