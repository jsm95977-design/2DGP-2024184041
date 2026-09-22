from pico2d import *


open_canvas(800, 600)

# 여기를 채우시오.
character = load_image('character.png')

x = 0
y = 90
count = 0

while count < 3:
    count+=1
    while x< 400:
        x+=2
        clear_canvas()
        character.draw(x, y)
        update_canvas()
    
        delay(0.01)

    while y< 140:
        y+=2
        clear_canvas()
        character.draw(x, y)
        update_canvas()
    
        delay(0.01)

    while x > 0:
        x-=2
        clear_canvas()
        character.draw(x, y)
        update_canvas()
    
        delay(0.01)

    while y > 90:
        y-=2
        clear_canvas()
        character.draw(x, y)
        update_canvas()
    
        delay(0.01)


delay(2)

close_canvas()

