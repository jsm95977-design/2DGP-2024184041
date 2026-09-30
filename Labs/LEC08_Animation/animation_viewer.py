from pico2d import *

CANVAS_WIDTH, CANVAS_HEIGHT = 800, 600

# 프레임 좌표 (left, top, width, height) - 이미지 편집기 기준 (위쪽이 y=0)
IDLE_FRAMES = [
    (2, 2, 37, 52), (41, 2, 37, 51), (80, 2, 37, 50), (119, 2, 37, 50),
    (158, 2, 37, 49), (197, 2, 37, 50), (236, 2, 37, 51), (275, 2, 37, 52),
]

open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

sheet = load_image('ani_sheet.png')

left, top, width, height = IDLE_FRAMES[0]
clear_canvas()
sheet.clip_draw(left, sheet.h - top - height, width, height, CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
update_canvas()

delay(2)

close_canvas()
