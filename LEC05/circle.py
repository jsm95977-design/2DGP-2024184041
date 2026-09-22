from pico2d import *
import math

open_canvas(800, 600)

# 여기를 채우시오.
character = load_image('character.png')

r= 100  
PI = math.pi
angle = 0
count = 0
while count < 10:
    count +=1 
    while angle <2*PI:
        angle += 0.05
        clear_canvas()        
        character.draw(400 + r*math.cos(angle), 300 + r* math.sin(angle))
        update_canvas()
        delay(0.01)
    angle =0 

   

delay(2)

close_canvas()

