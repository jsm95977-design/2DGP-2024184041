from pico2d import *
import math

open_canvas(800, 600)
character = load_image("character.png")

CENTER = (400, 300)
RADIUS = 200

RECT_POINTS = [(400, 300), (700, 300), (700, 500), (400, 500)]
TRIANGLE_POINTS = [(100, 100), (700, 100), (400, 500)]


def draw_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.01)


def move_circle():
    cx, cy = CENTER
    for degree in range(360):
        theta = math.radians(degree)
        draw_character(cx + RADIUS * math.cos(theta), cy + RADIUS * math.sin(theta))


def move_line(start, end, step=2):
    x1, y1 = start
    x2, y2 = end
    for i in range(0, 101, step):
        t = i / 100
        draw_character(x1 + (x2 - x1) * t, y1 + (y2 - y1) * t)


def move_along_path(points, step=2):
    for start, end in zip(points, points[1:] + points[:1]):
        move_line(start, end, step)


def move_rectangle():
    move_along_path(RECT_POINTS)


def move_triangle():
    move_along_path(TRIANGLE_POINTS)


while True:
    move_circle()
    move_rectangle()
    move_triangle()

close_canvas()
