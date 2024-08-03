from asyncio import Event
from pygame import Vector2
import IO, MouseInput, Grid
import pygame as pg
import json


def tick():    
    event: Event
    for event in pg.event.get():
        if event.type == pg.QUIT:
            return False    
        
        elif event.type in [pg.MOUSEMOTION, pg.MOUSEBUTTONDOWN, pg.MOUSEBUTTONUP]:
            MouseInput.mouse_event(event)

        elif event.type == pg.KEYDOWN:
            mods = pg.key.get_mods()

            if mods & pg.KMOD_CTRL and event.key == pg.K_s:
                IO.save_file()
            elif mods & pg.KMOD_CTRL and event.key == pg.K_l:
                IO.load_file()
            elif event.key == pg.K_p:
                print(json.dumps({str(key): value for key, value in Grid.cell_dict.items()}))

        
    return True

pg.quit()