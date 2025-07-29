import re
from PIL import Image, ImageDraw
import random


class ArtElement:
    def __init__(self, attributes: dict, items: list):
        self.attributes = attributes
        self.items = items

    def draw(self, image: Image):
        for item in self.items:
            item.draw(image)
        pass


class Circle(ArtElement):
    def __init__(self, x, y, radius, color):
        super().__init__({}, [])
        self.attributes = {"x": x, "y": y, "radius": radius, "color": color}
        # self.x = x
        # self.y = y
        # self.radius = radius
        # self.color = color

    def draw(self, image: Image):
        pass
        # draw = ImageDraw.Draw(image)
        # draw.ellipse(
        #     [
        #         (self.x - self.radius, self.y - self.radius),
        #         (self.x + self.radius, self.y + self.radius),
        #     ],
        #     fill=self.color,
        # )


class Canvas:
    def __init__(self, width, height, background_color):
        self.width = width
        self.height = height
        self.background_color = background_color
        self.elements = []
        self.image = Image.new("RGB", (width, height), background_color)

    def add_element(self, element: ArtElement):
        self.elements.append(element)

    def render(self):
        for element in self.elements:
            element.draw(self.image)
        return self.image

    def show(self):
        self.image.show()

    def save(self, filename):
        self.image.save(filename)


def generate_random_circles(num_circles=10):
    circles = []
    for _ in range(num_circles):
        x = random.randint(0, 1000)
        y = random.randint(0, 1000)
        radius = random.randint(0, 100)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        circle = Circle(x, y, radius, color)
        circles.append(circle)
    return circles


def create_canvas(width=1000, height=1000, background_color=(255, 255, 255)):
    return Canvas(width, height, background_color)


def draw_circles(canvas: Canvas = create_canvas(), circles: list[Circle] = []):
    for circle in circles:
        canvas.add_element(circle)
    canvas.render()
    canvas.show()
    canvas.save("canvas.png")
    return canvas


if __name__ == "__main__":
    canvas = create_canvas()
    circles = generate_random_circles(10)
    draw_circles(canvas, circles)
