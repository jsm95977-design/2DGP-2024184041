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
    # 시트 로드 확인용: 시트 전체를 화면 중앙에 그린다
    sonic.draw(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
    update_canvas()
    delay(FRAME_TIME)

close_canvas()
