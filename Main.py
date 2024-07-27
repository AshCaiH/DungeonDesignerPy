import pygame as pg
import Grid
import Loop

pg.init()

clock = pg.time.Clock()

# Window settings
SCR_WDTH = 800
SCR_HGHT = 640

screen = pg.display.set_mode(( SCR_WDTH, SCR_HGHT ))
pg.display.set_caption("Dungeon Designer")

bg_img = pg.image.load("assets/images/noisebg.png").convert_alpha()

running = True
while running:
    clock.tick(60)
    
    screen.fill((59,92,150))
    screen.blit(bg_img, (0,0))

    Grid.draw(screen), (10,10)



    running = Loop.tick()

    pg.display.update()