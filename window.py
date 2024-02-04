import pygame as pg
from numpy import zeros, ndarray
from prac.prac1 import drawLineDDA

W, H = 100, 80
PIXEL = 10
W_SCREEN, H_SCREEN = W*PIXEL, H*PIXEL

PIXEL_BUFFER : ndarray[ndarray]  = zeros((H, W), dtype=int)

# initialize
pg.init()
screen : pg.Surface = pg.display.set_mode((W_SCREEN, H_SCREEN))


def draw_grid(surface : pg.Surface, color : pg.Color) -> None:
    # vertical lines
    [pg.draw.line(surface, color, (x, 0), (x, H_SCREEN)) for x in range(0, W_SCREEN, PIXEL)] 
    # horizaontal lines
    [pg.draw.line(surface, color, (0, y), (W_SCREEN, y)) for y in range(0, H_SCREEN, PIXEL)]

def draw_pixel(buffer : ndarray[ndarray], surface : pg.Surface, color : pg.Color) -> None:
    [[pg.draw.rect(surface, color, pg.Rect(x*PIXEL, y*PIXEL, PIXEL, PIXEL)) for x, pixel in enumerate(row) if pixel] for y, row in enumerate(buffer)]


running : bool= True

if __name__ == '__main__':
    screen.fill((0,0,0))
    draw_grid(screen, (20, 20, 20))

    # draw line
    drawLineDDA(PIXEL_BUFFER, (10, 10), (10, 50))
    drawLineDDA(PIXEL_BUFFER, (10, 50), (50, 50))
    drawLineDDA(PIXEL_BUFFER, (10, 10), (50, 10))
    drawLineDDA(PIXEL_BUFFER, (50, 10), (50, 50))

    # draw pixels
    draw_pixel(PIXEL_BUFFER, screen, (50, 50, 50))
    pg.display.flip()

    # run the loop for checking closing of window
    while running:
        [exit() for e in pg.event.get() if e.type == pg.QUIT]