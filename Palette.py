import pygame as pg
import Global

screen : pg.Surface = None

element_types =     {"floor": 1,
                    "nwall": 1,
                    "wwall": 1,
                    "prop":  1}

colours = [None, (255,255,255), (180, 214, 205), (255, 218, 118), (255, 140, 158)]

def draw():
    global screen
    screen = pg.Surface((Global.SCR_WDTH, Global.SCR_HGHT), pg.SRCALPHA)

    draw_bg()

    return screen

def draw_bg():
    screen.fill((9, 158, 209, 120), Global.palette_rect)