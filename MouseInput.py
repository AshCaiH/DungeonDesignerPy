from asyncio import Event
import pygame as pg
from pygame import Rect, Vector2
import Global, Grid, Cursor

pan_mode = False
previous_override = None

def mouse_event(event: Event):
    global pan_mode, previous_override
    Cursor.move(event.pos)

    if Global.palette_rect.collidepoint(event.pos):
        Cursor.override_mode = 0
    else:
        Cursor.override_mode = previous_override
        
        canvas_click(event)

        previous_override = Cursor.override_mode


    # Release pan mode regardless of cursor position
    if pan_mode:
        try: 
            Cursor.override_mode = -1
            Global.camera_offset = Vector2(*event.pos) - (Global.camera_click_pos - Global.camera_last_offset)
        except AttributeError: pass

    if event.type == pg.MOUSEBUTTONUP and event.button == 2:
        Global.camera_last_offset = Global.camera_offset
        Cursor.override_mode = None
        Cursor.move(event.pos)
        pan_mode = False

def palette_click(event: Event):
    pass

def canvas_click(event: Event):
    global pan_mode
    if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
        Global.set_cell_mode = Grid.set_cell(Cursor.cell_pos)
        Cursor.override_mode = Cursor.mode

    elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
        Global.set_cell_mode = 2
        Cursor.override_mode = None
        Cursor.move(event.pos)

    # Panning

    elif event.type == pg.MOUSEBUTTONDOWN and event.button == 2:
        try:
            Global.camera_click_pos = event.pos
            pan_mode = True
        except AttributeError: pass
    
    elif pg.mouse.get_pressed()[0]:
        Grid.set_cell(Cursor.cell_pos, Global.set_cell_mode)