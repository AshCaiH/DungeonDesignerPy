from pygame import Vector2

SCR_WDTH = 800
SCR_HGHT = 640

# Settings

ROWS = 10
COLS = 10
CELL_SIZE = 32
WALL_COLLISION = 3
GRID_COLOUR = (255,255,255, 100)

# Runtime values

camera_offset = Vector2(10,10)
camera_last_offset = camera_offset
camera_click_pos = Vector2(0,0)

# Functions
def mouse_to_world(mousepos):
    mousepos = Vector2(mousepos[0], mousepos[1])
    return mousepos - camera_offset

def mouse_to_cell(mousepos):
    world_pos = mouse_to_world(mousepos)
    cell_pos = Vector2(world_pos.x // CELL_SIZE, world_pos.y // CELL_SIZE)
    return cell_pos

def cell_to_screen(cell_coord: Vector2):
    return cell_coord * CELL_SIZE + camera_offset