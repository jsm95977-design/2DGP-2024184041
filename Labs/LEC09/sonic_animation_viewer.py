from pico2d import *

CANVAS_WIDTH, CANVAS_HEIGHT = 800, 600

open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

sonic = load_image('sonic-sprite.png')
print(sonic.w, sonic.h)

# 시트 로드 확인용: 시트 전체를 화면 중앙에 그린다
clear_canvas()
sonic.draw(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
update_canvas()
delay(2)

close_canvas()
