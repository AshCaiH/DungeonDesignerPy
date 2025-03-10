import pygame as pg
import Global, Grid, Loop, Cursor, Palette, Debug

pg.init()

clock = pg.time.Clock()

# Window settings

screen = pg.display.set_mode(( Global.SCR_WDTH, Global.SCR_HGHT ), pg.SRCALPHA)
pg.display.set_caption("Dungeon Designer")

bg_img = pg.image.load("assets/images/noisebg.png").convert_alpha()

Global.resize_cursor()

pg.font.init() # you have to call this at the start, 
                   # if you want to use this module.
my_font = pg.font.SysFont('Courier', 16)



running = True
while running:
    clock.tick(60)

    # Logic step
    running = Loop.tick()

    # Draw step    
    screen.fill((59,92,150))
    screen.blit(bg_img, (0,0))
    screen.blit(Grid.draw(), (0,0))
    screen.blit(Cursor.draw(), (0,0))
    screen.blit(Palette.draw(), (0,0))

    text_surface = my_font.render(
        f'{Global.mouse_to_cell()}/n \
        {Global.mouse_position}', 
        False, (255, 255, 255))    
    screen.blit(text_surface, (400,0))

    pg.display.update()