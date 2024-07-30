import pygame as pg
from pygame import Vector2
import Global
from Global import WALL_COLLISION as hex_size

cell_pos = Vector2(0,0)
inner_pos = Vector2(0,0) # Where the mouse is within the cell
mode = 0 # 1 = floor, 2 = nwall, 3 = wwall, 4 = prop

screen = None

def move(mouse_pos):
    global cell_pos, inner_pos, mode
    cell_pos = Global.mouse_to_cell(mouse_pos)
    inner_pos = (mouse_pos - Global.camera_offset)
    inner_pos = Vector2(inner_pos.x % Global.CELL_SIZE, inner_pos.y % Global.CELL_SIZE)

    # TODO: Make sure to account for "invisible" cells needed for right and bottom edge walls.
    if cell_pos.x >= Global.COLS or cell_pos.y >= Global.ROWS \
        or cell_pos.x < 0 or cell_pos.y < 0:
        mode = 0
    elif inner_pos.y > Global.CELL_SIZE - Global.CURSOR_SIZE:
        mode = 2
        cell_pos.y += 1
    elif inner_pos.y < Global.CURSOR_SIZE:
        mode = 2
    elif inner_pos.x > Global.CELL_SIZE - Global.CURSOR_SIZE:
        mode = 3
        cell_pos.x += 1
    elif inner_pos.x < Global.CURSOR_SIZE:
        mode = 3
    else:
        mode = 1

def draw():
    global screen
    screen = pg.Surface((Global.SCR_WDTH, Global.SCR_HGHT), pg.SRCALPHA)

    # # Code for rotating the wall cursor
    def rotate_points(point):
        return pg.math.Vector2(point).rotate(90)

    # hexagon = list(map(rotate_points, Global.hexagon))

    def hex_to_screen(vec):
        return tuple(vec + Global.cell_to_screen(cell_pos))
    
    if mode == 1:
        pg.draw.rect(screen, (255,255,255), (*tuple(Global.cell_to_screen(cell_pos)), *[Global.CELL_SIZE]*2), 1, border_radius=1)
    elif mode == 2:
        pg.draw.lines(screen, (255,255,255), True, list(map(hex_to_screen, Global.hexagon)))
    elif mode == 3:
        pg.draw.lines(screen, (255,255,255), True, list(map(hex_to_screen, map(rotate_points, Global.hexagon))))

    return screen