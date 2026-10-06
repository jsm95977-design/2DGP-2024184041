from pico2d import *

CANVAS_WIDTH, CANVAS_HEIGHT = 800, 600
CENTER_X, CENTER_Y = CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2
SCALE = 4
FRAME_TIME = 0.1
REPEAT = 5
REST_TIME = 1.0
REST_FRAMES = round(REST_TIME / FRAME_TIME)

# (동작 이름, bottom, height, [(left, width), ...])
ACTIONS = [
    ('idle', 447, 39, [(1, 29), (31, 26), (58, 29), (87, 29), (118, 30), (150, 30),
                       (182, 30), (212, 28), (240, 29), (270, 24), (302, 29)]),
    ('walk', 407, 39, [(8, 26), (37, 27), (65, 31), (97, 37), (135, 32), (170, 32),
                       (206, 26), (238, 24), (263, 30), (295, 36), (334, 32), (370, 29)]),
    ('accel', 361, 43, [(1, 33), (39, 35), (89, 35), (130, 34), (181, 34), (228, 33)]),
    ('spin', 325, 33, [(1, 29), (35, 29), (67, 30), (98, 31), (131, 29), (162, 29),
                       (193, 30), (230, 31), (268, 30)]),
    ('ball', 292, 27, [(1, 30), (36, 29), (70, 29), (105, 29), (139, 29), (174, 29)]),
    ('run', 251, 36, [(1, 29), (36, 30), (74, 31), (111, 31), (149, 30), (186, 31)]),
    ('dash', 207, 35, [(1, 29), (36, 30), (72, 39), (123, 39), (172, 39), (218, 38)]),
    ('action_a', 154, 45, [(1, 24), (31, 29), (65, 20), (90, 25), (119, 25), (149, 20),
                           (184, 40), (232, 39)]),
    ('action_b', 108, 40, [(1, 27), (31, 31), (64, 31), (99, 33), (136, 32), (176, 33),
                           (217, 33), (254, 33)]),
    ('action_c', 56, 43, [(6, 34), (49, 34), (96, 23), (125, 23)]),
]

# 가장 큰 프레임이 화면 세로 중앙에 오도록 바닥선을 정한다
MAX_HEIGHT = max(height for _, _, height, _ in ACTIONS)
GROUND_Y = CENTER_Y - MAX_HEIGHT * SCALE / 2

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


def draw_frame(action_index, frame):
    name, bottom, height, frames = ACTIONS[action_index]
    left, width = frames[frame]
    # 높이가 달라도 발이 같은 바닥선에 오도록 아래쪽 기준으로 정렬
    y = GROUND_Y + height * SCALE / 2
    sonic.clip_draw(left, bottom, width, height,
                    CENTER_X, y, width * SCALE, height * SCALE)


def update():
    global action_index, frame, loop_count, rest_left

    # 휴식 중: 마지막 프레임을 그대로 두고 남은 휴식 시간만 줄인다
    if rest_left > 0:
        rest_left -= 1
        if rest_left == 0:
            action_index = (action_index + 1) % len(ACTIONS)
            frame = 0
        return

    if frame == len(ACTIONS[action_index][3]) - 1:
        loop_count += 1
        if loop_count == REPEAT:
            loop_count = 0
            rest_left = REST_FRAMES
            return
        frame = 0
    else:
        frame += 1


running = True
action_index = 0
frame = 0
loop_count = 0
rest_left = 0
while running:
    handle_events()
    clear_canvas()
    draw_frame(action_index, frame)
    update_canvas()
    update()
    delay(FRAME_TIME)

close_canvas()
