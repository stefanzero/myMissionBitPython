from PIL import Image, ImageDraw
import os


def change_directory_to_script_directory():
    script_path = os.path.abspath(__file__)
    script_directory = os.path.dirname(script_path)
    os.chdir(script_directory)


class ArtElement:
    def __init__(self, attributes):
        self.attributes = attributes

    def update_attribute(self, key, value):
        self.attributes[key] = value

    def draw(self, draw_context):
        if (
            "position" in self.attributes
            and "size" in self.attributes
            and "color" in self.attributes
        ):
            position = self.attributes["position"]
            size = self.attributes["size"]
            color = self.attributes["color"]
            upper_left = (position[0] - size, position[1] - size)
            lower_right = (position[0] + size, position[1] + size)
            draw_context.ellipse([upper_left, lower_right], fill=color)


"""
Step 3: Creating the Canvas Class
Objective: Develop a container class for managing multiple art elements.
Actions:
Explain the structure of a digital canvas and its role in organizing art elements.
Assist students in creating a Canvas class that manages a collection of ArtElement objects and
facilitates rendering.
Example Code:
"""


class Canvas:
    def __init__(self, size, background_color="white"):
        self.image = Image.new("RGB", size, background_color)
        self.draw_context = ImageDraw.Draw(self.image)
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)

    def render(self):
        for element in self.elements:
            element.draw(self.draw_context)
        return self.image


"""
Step 4: Composing and Generating Artwork
Objective: Apply the classes to generate unique generative art.
Actions:
Guide students through writing a function to create and arrange multiple ArtElement instances
with random attributes.
Demonstrate how to use loops and randomization to generate diverse artworks.
Example Code:
"""
import random


def generate_artwork():
    canvas = Canvas((800, 600), "black")
    for _ in range(50):
        position = (random.randint(0, 800), random.randint(0, 600))
        size = random.randint(10, 50)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        circle_attributes = {"position": position, "size": size, "color": color}
        circle = ArtElement(circle_attributes)
        canvas.add_element(circle)
    final_art = canvas.render()
    final_art.show()
    final_art.save("my_generative_artwork.png")


if __name__ == "__main__":
    change_directory_to_script_directory()
    generate_artwork()
