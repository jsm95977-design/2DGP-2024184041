from pico2d import *

CANVAS_WIDTH, CANVAS_HEIGHT = 800, 600
SCALE = 6  # 원본 프레임(약 50px)을 6배 확대 -> 화면 높이의 절반 이상
GROUND_Y = 150  # 캐릭터 발이 닿는 바닥 높이

# 프레임 좌표 (left, top, width, height) - 이미지 편집기 기준 (위쪽이 y=0)
IDLE_FRAMES = [
    (2, 2, 37, 52), (41, 2, 37, 51), (80, 2, 37, 50), (119, 2, 37, 50),
    (158, 2, 37, 49), (197, 2, 37, 50), (236, 2, 37, 51), (275, 2, 37, 52),
]
WALK_FRAMES = [
    (2, 56, 46, 47), (50, 56, 46, 47), (98, 56, 46, 47), (146, 56, 46, 48),
    (194, 56, 46, 48), (242, 56, 46, 47), (290, 56, 46, 48), (338, 56, 46, 48),
]
# 공격 모션은 6프레임이고, 베기 이펙트가 있는 뒤 2프레임은 크기가 107x69 로 훨씬 크다
ATTACK_FRAMES = [
    (2, 106, 41, 53), (45, 106, 43, 53), (90, 106, 41, 53), (133, 106, 41, 53),
    (176, 106, 107, 69), (285, 106, 107, 69),
]
HIT_FRAMES = [
    (2, 177, 48, 53), (52, 177, 48, 56),
]


def to_pico2d(frame, sheet_height):
    # 위쪽 기준 좌표를 pico2d 의 아래쪽 기준 좌표 (left, bottom, width, height) 로 변환
    left, top, width, height = frame
    return left, sheet_height - top - height, width, height


def handle_events():
    global running
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def draw_frame(frame):
    left, bottom, width, height = frame
    # 프레임마다 높이가 달라서 중심이 아니라 발(아래쪽)을 GROUND_Y 에 맞춘다
    draw_w, draw_h = width * SCALE, height * SCALE
    clear_canvas()
    sheet.clip_draw(left, bottom, width, height,
                    CANVAS_WIDTH // 2, GROUND_Y + draw_h // 2, draw_w, draw_h)
    update_canvas()


open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

sheet = load_image('ani_sheet.png')
idle = [to_pico2d(frame, sheet.h) for frame in IDLE_FRAMES]
walk = [to_pico2d(frame, sheet.h) for frame in WALK_FRAMES]
attack = [to_pico2d(frame, sheet.h) for frame in ATTACK_FRAMES]
hit = [to_pico2d(frame, sheet.h) for frame in HIT_FRAMES]

running = True
while running:
    for frame in idle + walk + attack + hit:
        handle_events()
        if not running:
            break
        draw_frame(frame)
        delay(0.1)

close_canvas()
