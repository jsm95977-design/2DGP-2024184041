from pico2d import *
import math

open_canvas(800, 600)
character = load_image("character.png")

degree = 0
theta = math.radians(degree)
x = 200 * math.cos(theta)   
y = 200 * math.sin(theta)


def move_circle():
    return
    global degree,theta, x, y
    
    for degree in range(360):
        degree += 1
        theta = math.radians(degree)
        x = 200 * math.cos(theta)   
        y = 200 * math.sin(theta)


        print("circle")
        clear_canvas()
        character.draw(400 + x, 300 + y)
        update_canvas()
        delay(0.01)
    degree = 0

def move_bottom():
    print("1")
    pass

def move_right():
    print("2")
    pass

def move_top():
    print("3")
    pass

def move_left():
    print("4")
    pass

def  move_rectangle():
    print("rectangle")
    move_bottom()
    move_right()
    move_top()
    move_left()
    delay(3)
    pass

def move_triangle():
    print("triangle")
    pass

while True:
    move_circle()
    move_rectangle()
    move_triangle()
    

close_canvas()