from pico2d import *

CANVAS_WIDTH, CANVAS_HEIGHT = 800, 600

open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

sheet = load_image('ani_sheet.png')

clear_canvas()
sheet.draw(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
update_canvas()

delay(2)

close_canvas()
