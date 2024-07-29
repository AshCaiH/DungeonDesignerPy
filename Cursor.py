import pygame as pg
from pygame import Vector2
import Global
from Global import WALL_COLLISION as hex_size

cell_pos = Vector2(0,0)
inner_pos = Vector2(0,0) # Where the mouse is within the cell
mode = 0 # 1 = floor, 2 = nwall, 3 = wwall, 4 = prop

screen = None

def move(mouse_pos):
    global cell_pos, inner_pos
    cell_pos = Global.mouse_to_cell(mouse_pos)
    inner_pos = (mouse_pos - Global.camera_offset)
    inner_pos = Vector2(inner_pos.x % Global.CELL_SIZE, inner_pos.y % Global.CELL_SIZE)

def draw():
    global screen
    screen = pg.Surface((Global.SCR_WDTH, Global.SCR_HGHT), pg.SRCALPHA)

    # TODO: Make sure to account for "invisible" cells needed for right and bottom edge walls.
    if cell_pos.x >= Global.COLS or cell_pos.y >= Global.ROWS \
        or cell_pos.x < 0 or cell_pos.y < 0:
        mode = 0
    else: mode = 2

    hexagon = [
        Vector2(0,0),
        Vector2(hex_size, hex_size),
        Vector2(Global.CELL_SIZE-hex_size, hex_size),
        Vector2(Global.CELL_SIZE, 0),
        Vector2(Global.CELL_SIZE-hex_size, -hex_size),
        Vector2(hex_size, -hex_size),
    ]

    def hex_to_screen(vec):
        return tuple(vec + Global.cell_to_screen(cell_pos))
    
    if mode == 2:
        pg.draw.polygon(screen, (255,255,255), list(map(hex_to_screen, hexagon)))

    return screen