from pico2d import *
import math

open_canvas(800, 600)
character = load_image("character.png")

degree = 0
theta = math.radians(degree)
x = 200 * math.cos(theta)   
y = 200 * math.sin(theta)

def draw_character(x,y):
    clear_canvas()
    character.draw(x,y)
    update_canvas()
    delay(0.01)

def move_circle():
    return
    global degree,theta, x, y
    
    for degree in range(360):
        degree += 1
        theta = math.radians(degree)
        x = 200 * math.cos(theta)   
        y = 200 * math.sin(theta)


        print("circle")
        draw_character(x+400, y+300)
    degree = 0

def move_bottom():
    print("1")
    for x in range(400, 700, 5):
        draw_character(x,y)
    pass

def move_right():
    print("2")
    draw_character(x,y)
    pass

def move_top():
    print("3")
    
    draw_character(x,y)
    pass

def move_left():
    print("4")
    draw_character(x,y)
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