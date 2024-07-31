from asyncio import Event
from pygame import Vector2
import Grid, Cursor, Global, IO
import pygame as pg


def tick():
    
    event: Event
    for event in pg.event.get():
        if event.type == pg.QUIT:
            return False
        
        elif event.type == pg.MOUSEMOTION:
            Cursor.move(event.pos)
        
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            Grid.set_cell(Cursor.cell_pos)        

        elif event.type == pg.KEYDOWN:
            mods = pg.key.get_mods()

            if mods & pg.KMOD_CTRL and event.key == pg.K_s:
                IO.save_file()
            elif mods & pg.KMOD_CTRL and event.key == pg.K_l:
                IO.load_file()
        
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 2:
            try:
                Global.camera_click_pos = event.pos
                Cursor.override_mode = -1
            except AttributeError:
                pass

        elif event.type == pg.MOUSEBUTTONUP and event.button == 2:
            Global.camera_last_offset = Global.camera_offset
            Cursor.override_mode = None
            Cursor.move(event.pos)
        
        # Always check this
        if pg.mouse.get_pressed()[1]:
            try: 
                Global.camera_offset = Vector2(*event.pos) - (Global.camera_click_pos - Global.camera_last_offset)
            except AttributeError: pass
        
    return True

pg.quit()