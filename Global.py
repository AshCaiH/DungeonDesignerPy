from pygame import Vector2, Rect

SCR_WDTH = 800
SCR_HGHT = 640

# Settings

ROWS = 10
COLS = 10
CELL_SIZE = 32
WALL_COLLISION = 3
GRID_COLOUR = (0,0,0, 100)
CURSOR_SIZE = 5
PALETTE_HEIGHT = 100

# Runtime values

camera_offset = Vector2(10,10)
camera_last_offset = camera_offset
camera_click_pos = Vector2(0,0)

layers = {"grid": True, "floors": True, "walls": True, "props": True}

palette_rect = Rect(0,SCR_HGHT-PALETTE_HEIGHT,SCR_WDTH, PALETTE_HEIGHT)

set_cell_mode = None

# Static hidden values

hexagon = []

# Functions
def mouse_to_world(mousepos):
    mousepos = Vector2(mousepos[0], mousepos[1])
    return mousepos - camera_offset

def world_to_mouse(worldpos):
    return worldpos + camera_offset

def mouse_to_cell(mousepos):
    world_pos = mouse_to_world(mousepos)
    cell_pos = Vector2(world_pos.x // CELL_SIZE, world_pos.y // CELL_SIZE)
    return cell_pos

def cell_to_screen(cell_coord: Vector2):
    return cell_coord * CELL_SIZE + camera_offset

def resize_cursor():
    global hexagon, CURSOR_SIZE
    hexagon = [
        Vector2(0,0),
        Vector2(CURSOR_SIZE, CURSOR_SIZE),
        Vector2(CELL_SIZE-CURSOR_SIZE, CURSOR_SIZE),
        Vector2(CELL_SIZE, 0),
        Vector2(CELL_SIZE-CURSOR_SIZE, -CURSOR_SIZE),
        Vector2(CURSOR_SIZE, -CURSOR_SIZE)
    ]

    CURSOR_SIZE = CELL_SIZE / 8
    CURSOR_SIZE += 1 - (CURSOR_SIZE % 2)