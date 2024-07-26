import pygame as pg

ROWS = 10
COLS = 10
CELL_SIZE = 32
GRID_COLOUR = (255,255,255, 100)

surface = pg.Surface((ROWS * CELL_SIZE + 1, COLS * CELL_SIZE + 1), pg.SRCALPHA)

print(surface)

def draw():
    for c in range(COLS + 1):
        pg.draw.line(surface, GRID_COLOUR, (c * CELL_SIZE, 0), (c * CELL_SIZE, ROWS * CELL_SIZE))
        
    for c in range(ROWS + 1):
        pg.draw.line(surface, GRID_COLOUR, (0, c * CELL_SIZE), (COLS * CELL_SIZE, c * CELL_SIZE))

    return surface