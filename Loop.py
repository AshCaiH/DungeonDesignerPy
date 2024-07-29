from asyncio import Event
from pygame import Vector2
import Grid, Cursor, Global
import pygame as pg


def tick():
    
    event: Event
    for event in pg.event.get():
        if event.type == pg.QUIT:
            return False
        
        if event.type == pg.MOUSEMOTION:
            Cursor.move(event.pos)
        
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            Grid.add_floor(Global.mouse_to_cell(event.pos))

        # FOR TESTING ONLY, REMOVE WHEN NO LONGER NEEDED
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 3:
            print(Cursor.inner_pos)
        # ###

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 2:
            try:
                Global.camera_click_pos = event.pos
            except AttributeError:
                pass

        if event.type == pg.MOUSEBUTTONUP and event.button == 2:
            Global.camera_last_offset = Global.camera_offset
        
        if pg.mouse.get_pressed()[1]:
            try:
                Global.camera_offset = Vector2(*event.pos) - (Global.camera_click_pos - Global.camera_last_offset)
            except AttributeError:
                pass
        
    return True

pg.quit()