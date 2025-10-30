from PIL import ImageDraw, Image, ImageFont
import os


def change_directory_to_script_directory():
    script_path = os.path.abspath(__file__)
    script_directory = os.path.dirname(script_path)
    os.chdir(script_directory)


class ArtElement:
    def __init__(self, attributes):
        self.attributes = attributes

    def update_attribute(self, key, value):
        self.key = key
        self.value = value


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


WIDTH = 1000
HEIGHT = 1000
BACKGROUND_COLOR = (255, 255, 255)


def create_canvas(width=WIDTH, height=HEIGHT, background_color=BACKGROUND_COLOR):
    return Canvas(width, height, background_color)


"""
https://ttfonts.net/
"""


def draw_text(canvas, text, font_path, font_size, x, y, color):
    draw_context = ImageDraw.Draw(canvas.image)
    font = ImageFont.truetype(font_path, font_size)
    draw_context.text((x, y), text, font=font, fill=color)


def paste_image(canvas, image, position):
    canvas.image.paste(image, position)


def load_image(image_path):
    return Image.open(image_path)


def main():
    change_directory_to_script_directory()
    canvas = create_canvas()
    draw_text(canvas, "Hello, World!", "arial.ttf", 24, 50, 50, (0, 0, 0))
    image_path = "./grumpy-cat-blue-eyes.png"
    image = load_image(image_path)
    paste_image(canvas, image, (100, 100))
    canvas.show()


if __name__ == "__main__":
    main()
