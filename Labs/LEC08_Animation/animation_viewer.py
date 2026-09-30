from pico2d import *

CANVAS_WIDTH, CANVAS_HEIGHT = 800, 600

# 프레임 좌표 (left, top, width, height) - 이미지 편집기 기준 (위쪽이 y=0)
IDLE_FRAMES = [
    (2, 2, 37, 52), (41, 2, 37, 51), (80, 2, 37, 50), (119, 2, 37, 50),
    (158, 2, 37, 49), (197, 2, 37, 50), (236, 2, 37, 51), (275, 2, 37, 52),
]


def to_pico2d(frame, sheet_height):
    # 위쪽 기준 좌표를 pico2d 의 아래쪽 기준 좌표 (left, bottom, width, height) 로 변환
    left, top, width, height = frame
    return left, sheet_height - top - height, width, height


def draw_frame(frame):
    left, bottom, width, height = frame
    clear_canvas()
    sheet.clip_draw(left, bottom, width, height, CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
    update_canvas()


open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

sheet = load_image('ani_sheet.png')
idle = [to_pico2d(frame, sheet.h) for frame in IDLE_FRAMES]

for frame in idle:
    draw_frame(frame)
    delay(0.1)

close_canvas()
