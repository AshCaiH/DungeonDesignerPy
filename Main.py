import pygame as pg
import Global, Grid, Loop, Cursor

pg.init()

clock = pg.time.Clock()

# Window settings

screen = pg.display.set_mode(( Global.SCR_WDTH, Global.SCR_HGHT ), pg.SRCALPHA)
pg.display.set_caption("Dungeon Designer")

bg_img = pg.image.load("assets/images/noisebg.png").convert_alpha()

running = True
while running:
    clock.tick(60)
    
    screen.fill((59,92,150))
    screen.blit(bg_img, (0,0))

    screen.blit(Grid.draw(), (0,0))

    screen.blit(Cursor.draw(), (0,0))

    running = Loop.tick()

    pg.display.update()