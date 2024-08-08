from pygame import Vector2
import pygame as pg
import Global, Cursor, Palette

cell_dict : dict = {}

# Temporarily hard coded
elements_dict : dict = {
    "floors": {
        1: {"name": "ground", "tags": ["solid"]},
        2: {"name": "water", "tags": ["water"]},
        3: {"name": "stone", "tags": ["solid"]},
        4: {"name": "carpet", "tags": ["solid"]},
    },
    "walls": {
        1: {"name": "normal", "tags": ["solid"]},
        2: {"name": "window", "tags": ["solid"]},
        3: {"name": "archway", "tags": ["nonsolid"]},
        4: {"name": "door", "tags": ["solid"]}
    },
    "props": {}
}

def make_surface():
    return pg.Surface((Global.SCR_WDTH, Global.SCR_HGHT), pg.SRCALPHA)

def draw():
    surfaces = []
    screen = pg.Surface((Global.SCR_WDTH, Global.SCR_HGHT), pg.SRCALPHA)

    surfaces.append(draw_frame())
    if Global.layers["floors"]: surfaces.append(draw_floors())
    if Global.layers["props"]: surfaces.append(draw_props())
    if Global.layers["walls"]: surfaces.append(draw_walls())
    if Global.layers["grid"]: surfaces.append(draw_grid())

    for surface in surfaces: screen.blit(surface, (0,0))

    return screen


def draw_floors():
    surface = make_surface()
    for key in cell_dict.keys():
        if cell_dict[key].get("floor", 0) != 0:
            pg.draw.rect(surface, (*Palette.colours[cell_dict[key]["floor"]], 185),
                        pg.Rect(*Global.cell_to_screen(Vector2(*key)), Global.CELL_SIZE, Global.CELL_SIZE))
    return surface


def draw_props():
    surface = make_surface()
    return surface


def draw_walls():
    surface = make_surface()
    wall_width = max(1, int(Global.CELL_SIZE / 8 + (1 - Global.CELL_SIZE % 2)))

    for key in cell_dict.keys():
        startPoint = tuple(Global.cell_to_screen(Vector2(*key)))

        if cell_dict[key].get("nwall", 0) != 0:
            endPoint = tuple(Global.cell_to_screen(Vector2(*key) + Vector2(1, 0)))
            pg.draw.line(surface, Palette.colours[cell_dict[key]["nwall"]], startPoint, endPoint, wall_width)
            
        if cell_dict[key].get("wwall", 0) != 0:
            endPoint = tuple(Global.cell_to_screen(Vector2(*key) + Vector2(0, 1)))
            pg.draw.line(surface, Palette.colours[cell_dict[key]["wwall"]], startPoint, endPoint, wall_width)
    return surface


def draw_grid():
    global cell_dict
    surface = make_surface()
    # Remove unused cells from dict    

    for i in range(Global.COLS + 1):
        x = i * Global.CELL_SIZE + Global.camera_offset.x
        pg.draw.line(surface, Global.GRID_COLOUR, 
                     (x, Global.camera_offset.y), (x, Global.ROWS * Global.CELL_SIZE + Global.camera_offset.y))
        
    for i in range(Global.ROWS + 1):
        y = i * Global.CELL_SIZE + Global.camera_offset.y
        pg.draw.line(surface, Global.GRID_COLOUR, 
                     (Global.camera_offset.x, y), (Global.COLS * Global.CELL_SIZE + Global.camera_offset.x, y))
    return surface


def draw_frame():
    surface = make_surface()
    pg.draw.rect(surface, Global.GRID_COLOUR, 
                 pg.Rect(*Global.camera_offset, Global.CELL_SIZE * Global.COLS, Global.CELL_SIZE * Global.ROWS), 3)
    return surface


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
    cell_dict.setdefault((int(cell_coord.x), int(cell_coord.y)), {})

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