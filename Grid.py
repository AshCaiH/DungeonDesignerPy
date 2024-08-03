from pygame import Vector2
import pygame as pg
import Global, Cursor, Palette

screen = None

cell_dict : dict = {}


def draw():
    global screen
    screen = pg.Surface((Global.SCR_WDTH, Global.SCR_HGHT), pg.SRCALPHA)

    draw_floors()
    draw_props()
    draw_grid()
    draw_walls()

    return screen


def draw_floors():
    for key in cell_dict.keys():
        if cell_dict[key].get("floor", 0) != 0:
            pg.draw.rect(screen, (*Palette.colours[cell_dict[key]["floor"]], 140),
                        pg.Rect(*Global.cell_to_screen(Vector2(*key)), Global.CELL_SIZE, Global.CELL_SIZE))


def draw_props():
    pass


def draw_walls():
    wall_width = int(Global.CELL_SIZE / 8 + (1 - Global.CELL_SIZE % 2))

    for key in cell_dict.keys():
        startPoint = tuple(Global.cell_to_screen(Vector2(*key)))

        if cell_dict[key].get("nwall", 0) != 0:
            endPoint = tuple(Global.cell_to_screen(Vector2(*key) + Vector2(1, 0)))
            pg.draw.line(screen, Palette.colours[cell_dict[key]["nwall"]], startPoint, endPoint, wall_width)
            
        if cell_dict[key].get("wwall", 0) != 0:
            endPoint = tuple(Global.cell_to_screen(Vector2(*key) + Vector2(0, 1)))
            pg.draw.line(screen, Palette.colours[cell_dict[key]["wwall"]], startPoint, endPoint, wall_width)


def draw_grid():
    global cell_dict
    # Remove unused cells from dict    

    for i in range(Global.COLS + 1):
        x = i * Global.CELL_SIZE + Global.camera_offset.x
        pg.draw.line(screen, Global.GRID_COLOUR, 
                     (x, Global.camera_offset.y), (x, Global.ROWS * Global.CELL_SIZE + Global.camera_offset.y))
        
    for i in range(Global.ROWS + 1):
        y = i * Global.CELL_SIZE + Global.camera_offset.y
        pg.draw.line(screen, Global.GRID_COLOUR, 
                     (0 + Global.camera_offset.x, y), (Global.COLS * Global.CELL_SIZE + Global.camera_offset.x, y))


def add_floor(cell_coord):
    cell_dict.setdefault((cell_coord.x, cell_coord.y), {})
    cell_dict[(cell_coord.x, cell_coord.y)]["floor"] = 1


# Remove empty cells from dictionary.
def clean_cells():
    global cell_dict
    def nonzero_value(item): return item[1] != 0

    for key in cell_dict.keys():
        for key2 in cell_dict[key].keys():
            cell_dict[key] = dict(filter(nonzero_value, cell_dict[key].items()))

    def contains_keys(cells : dict): return len(cells[1].keys()) > 0
    
    cell_dict = dict(filter(contains_keys, cell_dict.items()))


# Modes: 0 = off, 1 = on, 2 = toggle
def set_cell(cell_coord, mode = 2):
    global cell_dict
    cell_dict.setdefault((cell_coord.x, cell_coord.y), {})

    element = None
    return_state = None

    match Cursor.mode:
        case 1: element = "floor" 
        case 2: element = "nwall" 
        case 3: element = "wwall" 
        case 4: element = "prop" 
        case _: return

    try:
        cell_property = cell_dict[(cell_coord.x, cell_coord.y)][element]
    except KeyError:
        cell_property = None
    
    if mode == 0: 
        cell_dict[(cell_coord.x, cell_coord.y)][element] = 0
        return_state = 0
    elif mode == 1: cell_dict[(cell_coord.x, cell_coord.y)][element] = Palette.element_types[element]
    elif mode == 2:
        if cell_property is None or cell_property != Palette.element_types[element]:
            cell_dict[(cell_coord.x, cell_coord.y)][element] = Palette.element_types[element]
            return_state = 1
        else:
            cell_dict[(cell_coord.x, cell_coord.y)][element] = 0
            return_state = 0
    else:
        cell_dict[(cell_coord.x, cell_coord.y)][element] = Palette.element_types[element]

    clean_cells()

    return return_state