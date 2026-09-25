from pico2d import *
import math

open_canvas(800, 600)
char = load_image("character.png")

class Shape():
    def move():
        pass

class Circle(Shape):
    def __init__(self, start, radius):
        self.c1, self.c2 = start
        self.r = radius

    def move(self):
        for angle in range(0, 361, 2):
                theta = math.radians(angle)
                x = self.r * math.cos(theta)
                y = self.r * math.sin(theta)
                draw_char(self.c1 + x, self.c2 + y)

class Poly(Shape):
    def __init__(self, points):
        self.n = len(points)
        self.points = points

    def move(self):
        for i in range(self.n):
            self.move_line(self.points[i], self.points[(i+1)%self.n])

    def move_line(self, start, end):
        x1, y1 = start
        x2, y2 = end
        theta = math.atan2(y2-y1, x2-x1)
        dis = math.hypot(x2-x1,y2-y1 )
        
        for r in range(0, int(dis), 5):
            x = r * math.cos(theta)
            y = r * math.sin(theta)
            draw_char(x1 + x, y1 + y)
        

def draw_char(x,y):
    clear_canvas()

    char.draw(x, y)

    delay(0.01)
    update_canvas()

#main
shapes = [
    Circle((400, 300), 200),
    Poly([(100,100), (700,100), (700,500), (100,500)]),
    Poly([(100,100), (700,100), (400,300)])
]

for i in range(0, len(shapes), 1):
    for shape in shapes:
        shape.move()   

close_canvas()