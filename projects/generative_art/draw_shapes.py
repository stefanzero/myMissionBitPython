from calendar import c
from PIL import Image, ImageDraw
import os
import random


def change_directory_to_script_directory():
    script_path = os.path.abspath(__file__)
    script_directory = os.path.dirname(script_path)
    os.chdir(script_directory)


def create_canvas(size=(1200, 800), background_color=(255, 255, 255)):
    return Image.new("RGB", size, background_color)


def draw_rectangle(canvas, position, size, color):
    upper_left = (position[0] - size, position[1] - size)
    lower_right = (position[0] + size, position[1] + size)
    draw_context = ImageDraw.Draw(canvas)
    draw_context.rectangle([upper_left, lower_right], fill=color)


def draw_circle(canvas, position, radius, color):
    draw_context = ImageDraw.Draw(canvas)
    draw_context.ellipse(
        [
            (position[0] - radius, position[1] - radius),
            (position[0] + radius, position[1] + radius),
        ],
        fill=color,
    )


def show_canvas(canvas):
    canvas.show()


def save_canvas(canvas, filename):
    canvas.save(filename)


def main():
    change_directory_to_script_directory()
    canvas_width = 1200
    canvas_height = 800
    canvas_color = (255, 255, 255)
    canvas = create_canvas((canvas_width, canvas_height), canvas_color)
    # circle_position = (400, 400)
    # circle_radius = 100
    # circle_color = (255, 0, 0)
    # draw_circle(canvas, circle_position, circle_radius, circle_color)
    num_circles = 10
    for _ in range(num_circles):
        circle_position = (
            random.randint(0, canvas_width),
            random.randint(0, canvas_height),
        )
        circle_radius = random.randint(0, 100)
        circle_color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
        draw_circle(canvas, circle_position, circle_radius, circle_color)

    # rectangle_position = (200, 200)
    # rectangle_size = 100
    # rectangle_color = (0, 0, 255)
    # draw_rectangle(canvas, rectangle_position, rectangle_size, rectangle_color)

    num_rectangles = 10
    for _ in range(num_rectangles):
        rectangle_position = (
            random.randint(0, canvas_width),
            random.randint(0, canvas_height),
        )
        rectangle_size = random.randint(0, 100)
        rectangle_color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
        draw_rectangle(canvas, rectangle_position, rectangle_size, rectangle_color)
    show_canvas(canvas)
    file_name = "shapes.png"
    save_canvas(canvas, file_name)


if __name__ == "__main__":
    main()
