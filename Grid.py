from pygame import Vector2
import pygame as pg
import Global

ROWS = 10
COLS = 10
CELL_SIZE = 64
GRID_COLOUR = (255,255,255, 100)

def draw(screen):
    for i in range(COLS + 1):
        x = i * CELL_SIZE + Global.camera_offset.x
        pg.draw.line(screen, GRID_COLOUR, (x, Global.camera_offset.y), (x, ROWS * CELL_SIZE + Global.camera_offset.y))
        
    for i in range(ROWS + 1):
        y = i * CELL_SIZE + Global.camera_offset.y
        pg.draw.line(screen, GRID_COLOUR, (0 + Global.camera_offset.x, y), (COLS * CELL_SIZE + Global.camera_offset.x, y))