from pico2d import *
import math

open_canvas(800, 600)
character = load_image("character.png")

degree = 0
theta = math.radians(degree)
x = 200 * math.cos(theta)   
y = 200 * math.sin(theta)


def move_circle():
    
    global degree,theta, x, y
    

    degree += 1
    theta = math.radians(degree)
    x = 200 * math.cos(theta)   
    y = 200 * math.sin(theta)


    print("circle")
    clear_canvas()
    character.draw(400 + x, 300 + y)
    update_canvas()
    pass

def  move_rectangle():
    print("rectangle")
    pass

def move_triangle():
    print("triangle")
    pass

while True:
    move_circle()
    move_rectangle()
    move_triangle()
    

close_canvas()