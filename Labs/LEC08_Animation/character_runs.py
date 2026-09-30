from pico2d import *

open_canvas(800,600)

grass = load_image('grass.png')
character = load_image('animation_sheet.png')


# fill here
frame = 0
action = 0
while True: 
    
    for x in range(0, 800, 5):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(
            frame * 100, action * 100,
            100, 100,
            x, 90,
            100, 100
        )
        update_canvas()

        frame = (frame + 1) % 8
        delay(0.05)

    action = (action + 1) % 4

close_canvas()

