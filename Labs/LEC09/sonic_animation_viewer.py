from pico2d import *

CANVAS_WIDTH, CANVAS_HEIGHT = 800, 600

open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

sonic = load_image('sonic-sprite.png')
print(sonic.w, sonic.h)

close_canvas()
