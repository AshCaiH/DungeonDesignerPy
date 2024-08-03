from asyncio import Event
import IO, MouseInput, Grid, Palette
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
            elif event.key == pg.K_1:
                for key in Palette.element_types.keys(): Palette.element_types[key] = 1
            elif event.key == pg.K_2:
                for key in Palette.element_types.keys(): Palette.element_types[key] = 2
            elif event.key == pg.K_3:
                for key in Palette.element_types.keys(): Palette.element_types[key] = 3
            elif event.key == pg.K_4:
                for key in Palette.element_types.keys(): Palette.element_types[key] = 4

        
    return True

pg.quit()