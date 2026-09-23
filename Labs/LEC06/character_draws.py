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
    for r_x in range(400, 701, 5):
        draw_character(r_x,r_y)
    pass

def move_right():
    global r_x, r_y
    print("2")
    for r_y in range(300, 501, 5):
        draw_character(r_x,r_y)
    pass

def move_top():
    global r_x, r_y
    print("3")
    for r_x in range(700, 399, -5):
        draw_character(r_x,r_y)
    pass

def move_left():
    global r_x, r_y
    print("4")
    for r_y in range(500, 299, -5):
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

t_1 = (100,100)
t_2 = (700,100)
t_3 = (400,500)

def move_line(start, end):
    x1, y1 = start
    x2, y2 = end

    for i in range(0, 101, 2):      
        t = i / 100                   
        x = x1 + (x2 - x1) * t
        y = y1 + (y2 - y1) * t
        draw_character(x, y)

def move_triangle():
    print("triangle")
    move_line(t_1, t_2) 
    move_line(t_2, t_3)  
    move_line(t_3, t_1)   
    

while True:
    move_circle()
    move_rectangle()
    move_triangle()
    

close_canvas()