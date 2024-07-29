from pygame import Vector2
import pygame as pg
import Global

screen = pg.Surface((Global.SCR_WDTH, Global.SCR_HGHT), pg.SRCALPHA)

grid_dict = {}

def draw():
    global screen
    screen = pg.Surface((Global.SCR_WDTH, Global.SCR_HGHT), pg.SRCALPHA)

    draw_floors()
    draw_props()
    draw_walls()

    draw_grid()

    return screen

def draw_floors():
    for key in grid_dict.keys():
        if grid_dict[key].get("floor", 0) != 0:
            pg.draw.rect(screen, (255,255,255, 150),
                        pg.Rect(*Global.cell_to_position(Vector2(*key)), Global.CELL_SIZE, Global.CELL_SIZE))


def draw_props():
    pass


def draw_walls():
    pass


def draw_grid():
    for i in range(Global.COLS + 1):
        x = i * Global.CELL_SIZE + Global.camera_offset.x
        pg.draw.line(screen, Global.GRID_COLOUR, 
                     (x, Global.camera_offset.y), (x, Global.ROWS * Global.CELL_SIZE + Global.camera_offset.y))
        
    for i in range(Global.ROWS + 1):
        y = i * Global.CELL_SIZE + Global.camera_offset.y
        pg.draw.line(screen, Global.GRID_COLOUR, 
                     (0 + Global.camera_offset.x, y), (Global.COLS * Global.CELL_SIZE + Global.camera_offset.x, y))
        
def add_floor(cell_coord):
    grid_dict.setdefault((cell_coord.x, cell_coord.y), {})
    grid_dict[(cell_coord.x, cell_coord.y)]["floor"] = 1