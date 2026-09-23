from pico2d import *
import math

open_canvas(800, 600)
character = load_image("character.png")

degree = 0
theta = math.radians(degree)
x = 200 * math.cos(theta)   
y = 200 * math.sin(theta)
r_x = 400
r_y = 300

def draw_character(x,y):
    clear_canvas()
    character.draw(x,y)
    update_canvas()
    delay(0.01)

def move_circle():
    return
    global degree,theta, x, y
    
    for degree in range(360):
        theta = math.radians(degree)
        x = 200 * math.cos(theta)   
        y = 200 * math.sin(theta)


        print("circle")
        draw_character(x+400, y+300)
    degree = 0

def move_bottom():
    global r_x, r_y
    print("1")
    for r_x in range(400, 700, 5):
        draw_character(r_x,r_y)
    pass

def move_right():
    global r_x, r_y
    print("2")
    for r_y in range(300, 500, 5):
        draw_character(r_x,r_y)
    pass

def move_top():
    global r_x, r_y
    print("3")
    for r_x in range(700, 400, -5):
        draw_character(r_x,r_y)
    pass

def move_left():
    global r_x, r_y
    print("4")
    for r_y in range(500, 300, -5):
        draw_character(r_x,r_y)
    pass

def  move_rectangle():
    print("rectangle")
    r_x=400
    r_y=300
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