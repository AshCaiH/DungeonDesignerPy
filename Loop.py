from asyncio import Event
from pygame import Vector2
import States
import pygame as pg


def tick():
    
    event: Event
    for event in pg.event.get():
        if event.type == pg.QUIT:
            return False
        
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 2:
            States.camera_click_pos = event.pos

        if event.type == pg.MOUSEBUTTONUP and event.button == 2:
            States.camera_last_offset = States.camera_offset
        
        if pg.mouse.get_pressed()[1]:
            States.camera_offset = Vector2(*event.pos) - (States.camera_click_pos - States.camera_last_offset)
        
    return True

pg.quit()