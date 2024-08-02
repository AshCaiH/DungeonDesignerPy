from asyncio import Event
from pygame import Vector2
import IO, MouseInput
import pygame as pg


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

        
    return True

pg.quit()