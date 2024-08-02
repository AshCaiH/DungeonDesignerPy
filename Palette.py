import pygame as pg
import Global

screen : pg.Surface = None

def draw():
    global screen
    screen = pg.Surface((Global.SCR_WDTH, Global.SCR_HGHT), pg.SRCALPHA)

    draw_bg()

    return screen

def draw_bg():
    screen.fill((9, 158, 209, 120), Global.palette_rect)