import pygame as pg
from pygame import Vector2
import Global
from Global import WALL_COLLISION as hex_size

cell_pos = Vector2(0,0)
inner_pos = Vector2(0,0) # Where the mouse is within the cell
mode = 0 # 1 = floor, 2 = nwall, 3 = wwall, 4 = prop, -1 = Grab

override_mode = None

screen = None

previous_mode = None

def get_cursor_type():
    global mode

    if override_mode == -1: return override_mode

    near_nwall = False
    near_wwall = False
    offset = Vector2(0, 0)

    if override_mode is None or override_mode in [2,3]:
        # Check if cursor is in grid (with buffer for grid edges)
        if cell_pos.x >= Global.COLS + 1 or cell_pos.x < -1 \
        or cell_pos.y >= Global.ROWS + 1 or cell_pos.y < -1:
            return 0
        
        
        def check_near_wall(inner_pos_axis, offset_axis):
            if inner_pos_axis > Global.CELL_SIZE - Global.CURSOR_SIZE:
                if offset_axis == "x": offset.x = 1
                elif offset_axis == "y": offset.y = 1
                return True
            elif inner_pos_axis < Global.CURSOR_SIZE: return True
            else: return False    

        
        near_nwall = check_near_wall(inner_pos.y, "y")
        near_wwall = check_near_wall(inner_pos.x, "x")


        # If near both walls, prioritise last wall touched, otherwise prioritise north wall.
        # Prevents cursor "flickering" between both modes when moving it along a grid edge.
        if near_nwall and (not near_wwall or previous_mode == 2):
            cell_pos.y += offset.y

            if not (cell_pos.y >= Global.ROWS + 1 or cell_pos.y + offset.y < 0) \
            and not (cell_pos.x >= Global.COLS or cell_pos.x < 0):
                return 2
        
        if near_wwall and (not near_nwall or previous_mode == 3):
            cell_pos.x += offset.x

            if not (cell_pos.x >= Global.COLS + 1 or cell_pos.x + offset.x < 0) \
            and not (cell_pos.y >= Global.ROWS or cell_pos.y < 0):
                return 3
    
    # Check if cursor is within grid again but without the buffer zone
    if cell_pos.x >= Global.COLS or cell_pos.x < 0 \
    or cell_pos.y >= Global.ROWS or cell_pos.y < 0:
        return 0

    if override_mode is None or override_mode == 1:
        return 1


def move(mouse_pos):
    global cell_pos, inner_pos, mode, previous_mode
    cell_pos = Global.mouse_to_cell(mouse_pos)
    inner_pos = (mouse_pos - Global.camera_offset)
    inner_pos = Vector2(inner_pos.x % Global.CELL_SIZE, inner_pos.y % Global.CELL_SIZE)

    mode = get_cursor_type()

    previous_mode = mode


def draw():
    global screen
    screen = pg.Surface((Global.SCR_WDTH, Global.SCR_HGHT), pg.SRCALPHA)

    def rotate_points(point):
        return pg.math.Vector2(point).rotate(90)

    def hex_to_screen(vec):
        return tuple(vec + Global.cell_to_screen(cell_pos))
    
    if mode == 1:
        pg.draw.rect(screen, (255,255,255), (*tuple(Global.cell_to_screen(cell_pos)), *[Global.CELL_SIZE]*2), 1, border_radius=1)
    elif mode == 2:
        pg.draw.lines(screen, (255,255,255), True, list(map(hex_to_screen, Global.hexagon)))
    elif mode == 3:
        pg.draw.lines(screen, (255,255,255), True, list(map(hex_to_screen, map(rotate_points, Global.hexagon))))

    return screen