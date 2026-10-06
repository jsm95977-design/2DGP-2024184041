from pico2d import *

CANVAS_WIDTH, CANVAS_HEIGHT = 800, 600
FRAME_TIME = 0.1

open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

sonic = load_image('sonic-sprite.png')

# 대기 동작: bottom, height, 프레임별 (left, width)
IDLE_BOTTOM, IDLE_HEIGHT = 447, 39
IDLE_FRAMES = [(1, 29), (31, 26), (58, 29), (87, 29), (118, 30), (150, 30),
               (182, 30), (212, 28), (240, 29), (270, 24), (302, 29)]


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
    # 좌표 확인용: 대기 동작 11프레임을 한 줄로 나란히 그린다
    for i, (left, width) in enumerate(IDLE_FRAMES):
        sonic.clip_draw(left, IDLE_BOTTOM, width, IDLE_HEIGHT, 50 + i * 65, CANVAS_HEIGHT // 2)
    update_canvas()
    delay(FRAME_TIME)

close_canvas()
