import pygame as pg


def tick():
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            return False
        
    return True

pg.quit()