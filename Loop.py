from asyncio import Event
import IO, MouseInput, Grid, Palette, Global
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

        elif event.type == pg.MOUSEWHEEL:
            old_scale = Global.CELL_SIZE

            new_cell_size = Global.CELL_SIZE + (event.y * Global.CELL_SIZE // 8 + (1 - Global.CELL_SIZE % 2))
            Global.CELL_SIZE = max(min(new_cell_size, 128), 8)
            Global.resize_cursor()

            # Credit to this post for inspiration https://stackoverflow.com/a/38302057
            Global.camera_offset = pg.mouse.get_pos() - (Global.CELL_SIZE / old_scale) * (pg.mouse.get_pos() - Global.camera_offset)

        
    return True

pg.quit()