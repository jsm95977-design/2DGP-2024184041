from pico2d import *

CANVAS_WIDTH, CANVAS_HEIGHT = 800, 600
FRAME_TIME = 0.1

open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

sonic = load_image('sonic-sprite.png')

running = True
while running:
    clear_canvas()
    # 시트 로드 확인용: 시트 전체를 화면 중앙에 그린다
    sonic.draw(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
    update_canvas()
    delay(FRAME_TIME)

close_canvas()
