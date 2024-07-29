from asyncio import Event
from pygame import Vector2
import Global
import pygame as pg


def tick():
    
    event: Event
    for event in pg.event.get():
        if event.type == pg.QUIT:
            return False
        
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            print(event.pos)
            print(event.pos, Global.mouse_to_cell(event.pos))

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 2:
            Global.camera_click_pos = event.pos

        if event.type == pg.MOUSEBUTTONUP and event.button == 2:
            Global.camera_last_offset = Global.camera_offset
        
        if pg.mouse.get_pressed()[1]:
            Global.camera_offset = Vector2(*event.pos) - (Global.camera_click_pos - Global.camera_last_offset)
        
    return True

pg.quit()