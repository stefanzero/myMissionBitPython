from PIL import Image, ImageDraw
import os
import random
import math


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


def create_random_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )


def show_canvas(canvas):
    canvas.show()


def save_canvas(canvas, filename):
    canvas.save(filename)


def draw_random_circles(canvas, num_circles):
    for _ in range(num_circles):
        circle_position = (
            random.randint(0, canvas.width),
            random.randint(0, canvas.height),
        )
        circle_radius = random.randint(0, 100)
        circle_color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
        draw_circle(canvas, circle_position, circle_radius, circle_color)


def draw_random_rectangles(canvas, num_rectangles):
    for _ in range(num_rectangles):
        rectangle_position = (
            random.randint(0, canvas.width),
            random.randint(0, canvas.height),
        )
        rectangle_size = random.randint(0, 100)
        rectangle_color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
        draw_rectangle(canvas, rectangle_position, rectangle_size, rectangle_color)


def draw_circles_in_a_spiral(canvas, num_circles):
    angle = 0
    delta_angle = math.pi / 10
    radius = 50
    delta_radius = 10
    circle_radius = 60
    delta_circle_radius = 2

    for _ in range(num_circles):
        x = canvas.width / 2 + radius * math.cos(angle)
        y = canvas.height / 2 + radius * math.sin(angle)
        circle_radius += delta_circle_radius
        color = create_random_color()
        draw_circle(canvas, (x, y), circle_radius, color)
        angle += delta_angle
        radius += delta_radius


def main():
    change_directory_to_script_directory()
    WIDTH = 1000
    HEIGHT = 1000
    BACKGROUND_COLOR = (255, 255, 255)
    canvas = create_canvas((WIDTH, HEIGHT), BACKGROUND_COLOR)

    # draw_random_circles(canvas, 10)
    # draw_random_rectangles(canvas, 10)
    draw_circles_in_a_spiral(canvas, 100)
    show_canvas(canvas)
    file_name = "shapes.png"
    save_canvas(canvas, file_name)


if __name__ == "__main__":
    main()
