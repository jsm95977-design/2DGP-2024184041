from pico2d import *

CANVAS_WIDTH, CANVAS_HEIGHT = 800, 600
FRAME_TIME = 0.1

open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

sonic = load_image('sonic-sprite.png')


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


running = True
while running:
    handle_events()
    clear_canvas()
    # 대기 동작의 첫 프레임: left=1, bottom=447, width=29, height=39
    sonic.clip_draw(1, 447, 29, 39, CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
    update_canvas()
    delay(FRAME_TIME)

close_canvas()
