from PIL import ImageDraw, Image
import random


class ArtElement:
    def __init__(self, attributes):
        self.attributes = attributes

    def update_attribute(self, key, value):
        self.key = key
        self.value = value


class Circle(ArtElement):
    def __init__(self, attributes):
        super().__init__(attributes)

    def draw(self, image: Image):
        x = self.attributes["x"]
        y = self.attributes["y"]
        radius = self.attributes["radius"]
        # color = self.attributes["color"]
        fill = self.attributes["fill"]
        if "outline_color" in self.attributes:
            outline_color = self.attributes["outline_color"]
        else:
            outline_color = None
        draw_context = ImageDraw.Draw(image)
        draw_context.ellipse(
            [
                (x - radius, y - radius),
                (x + radius, y + radius),
            ],
            fill=fill,
            outline=outline_color,
        )


class Rectangle(ArtElement):
    def __init__(self, attributes):
        super().__init__(attributes)

    def draw(self, image: Image):
        x = self.attributes["x"]
        y = self.attributes["y"]
        width = self.attributes["width"]
        height = self.attributes["height"]
        # color = self.attributes["color"]
        fill = self.attributes["fill"]
        if "outline_color" in self.attributes:
            outline_color = self.attributes["outline_color"]
        else:
            outline_color = None
        draw_context = ImageDraw.Draw(image)
        draw_context.rectangle(
            [
                (x, y),
                (x + width, y + height),
            ],
            fill=fill,
            outline=outline_color,
        )


class Line(ArtElement):
    def __init__(self, attributes):
        super().__init__(attributes)

    def draw(self, image: Image):
        x1 = self.attributes["x1"]
        y1 = self.attributes["y1"]
        x2 = self.attributes["x2"]
        y2 = self.attributes["y2"]
        width = self.attributes["width"]
        # color = self.attributes["color"]
        fill = self.attributes["fill"]
        draw_context = ImageDraw.Draw(image)
        draw_context.line(
            [
                (x1, y1),
                (x2, y2),
            ],
            width=width,
            fill=fill,
        )


class Polygon(ArtElement):
    def __init__(self, attributes):
        """
        example of attributes dictionary for a triangle
        that has a green fill and a blue outline:
        attributes = {
            "xy": [(100, 100), (200, 100), (200, 200)],
            "fill": (0, 255, 0),
            "outline_color": (0, 0, 255),
            "width": 1
        }
        """
        super().__init__(attributes)

    """
    draw.polygon(xy, fill, outline_color, width): 
    Draws a polygon. xy is a list of (x, y) coordinates for the vertices.
    """

    def draw(self, image: Image):
        # TODO: get variables from self.attributes
        # then remove the return statement
        return
        # xy = ?
        # fill = ?
        # width = ?
        if "outline_color" in self.attributes:
            outline_color = self.attributes["outline_color"]
        else:
            outline_color = None
        draw_context = ImageDraw.Draw(image)
        draw_context.polygon(xy, fill=fill, outline=outline_color, width=width)


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


def create_my_circles():
    my_circle1 = {"x": 200, "y": 200, "fill": (255, 0, 0), "radius": 100}
    my_circle2 = {"x": 800, "y": 800, "fill": (0, 255, 0), "radius": 50}
    my_circle3 = {"x": 500, "y": 500, "fill": (0, 0, 255), "radius": 75}
    circles = (my_circle1, my_circle2, my_circle3)
    return circles


def create_random_circles(n=10):
    circles = []
    for i in range(n):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        radius = random.randint(10, 100)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        circle = {"x": x, "y": y, "fill": color, "radius": radius}
        circles.append(circle)
    return circles


def create_my_rectangles():
    rectangle1 = {"x": 300, "y": 400, "width": 100, "height": 200, "fill": (255, 0, 0)}
    rectangle2 = {"x": 600, "y": 500, "width": 250, "height": 400, "fill": (0, 255, 0)}
    rectangle3 = {"x": 500, "y": 200, "width": 200, "height": 100, "fill": (0, 0, 255)}
    rectangle4 = {
        "x": 600,
        "y": 600,
        "width": 600,
        "height": 600,
        "fill": (200, 0, 200),
    }
    return rectangle1, rectangle2, rectangle3, rectangle4


def create_random_rectangles(n=10):
    rectangles = []
    for i in range(n):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        width = random.randint(10, 100)
        height = random.randint(10, 100)
        fill = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        rectangle = {"x": x, "y": y, "width": width, "height": height, "fill": fill}
        rectangles.append(rectangle)
    return rectangles


def create_random_lines(n=10):
    lines = []
    for i in range(n):
        x1 = random.randint(0, WIDTH)
        y1 = random.randint(0, HEIGHT)
        x2 = random.randint(0, WIDTH)
        y2 = random.randint(0, HEIGHT)
        width = random.randint(1, 10)
        fill = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        line = {"x1": x1, "y1": y1, "x2": x2, "y2": y2, "fill": fill, "width": width}
        lines.append(line)
    return lines


def test_circles():
    circles = create_my_circles()
    # circles = create_random_circles(10)
    my_canvas = create_canvas()
    for circle in circles:
        my_canvas.add_element(Circle(circle))
    my_canvas.render()
    my_canvas.show()
    # my_canvas.save("canvas.png")


def test_rectangles():
    # rectangles = create_my_rectangles()
    rectangles = create_random_rectangles(10)
    my_canvas = create_canvas()
    for rectangle in rectangles:
        my_canvas.add_element(Rectangle(rectangle))
    my_canvas.render()
    my_canvas.show()
    # my_canvas.save("canvas.png")


def test_lines():
    lines = create_random_lines(10)
    my_canvas = create_canvas()
    for line in lines:
        my_canvas.add_element(Line(line))
    my_canvas.render()
    my_canvas.show()
    # my_canvas.save("canvas.png")


def create_background(canvas):
    """
    assume the canvas is 1000x1000
    draw the sky as a rectangle with corner at (0, 0) and
    width = 1000
    height = 600
    fill = sky_blue = (135, 206, 235)
    sky_rectangle = {
        "x": ?,
        "y": ?,
        "width": ?,
        "height": ?,
        "fill": ?
    }
    """
    # create the rectangle dictionary
    sky_rectangle = {}
    # create the rectangle ArtElement
    # sky = Rectangle(sky_rectangle)
    # add the sky to the canvas
    # canvas.add_element(sky)

    """
    draw the ground as a rectangle with corner at (0, 600)
    width = 1000
    height = 600
    fill = forest_green = (34, 139, 34)
    ground_rectangle = {
        "x": ?,
        "y": ?,
        "width": ?,
        "height": ?,
        "fill": ?  
    }
    """
    # create the rectangle dictionary
    ground_rectangle = {}
    # create the rectangle ArtElement
    # ground = Rectangle(ground_rectangle)
    # add the ground to the canvas
    # canvas.add_element(ground)

    """
    draw the sun as a circle with center (800, 100) and radius 50
    and fill = yellow = (255, 255, 0)
    sun_circle = {
        "x": ?,
        "y": ?,
        "fill": ?,
        "radius": ?
    }
    """
    # create the circle dictionary
    sun_circle = {}
    # create the circle ArtElement
    # sun = Circle(sun_circle)
    # add the sun to the canvas
    # canvas.add_element(sun)


def create_house(canvas):
    """
    draw the house as a rectangle with corner at (200, 500)
    width = 500
    height = 300
    fill = goldenrod = (255, 185, 15),
    outline_color = black = (0, 0, 0)
    house_rectangle = {
        "x": ?,
        "y": ?,
        "width": ?,
        "height": ?,
        "fill": ?,
        "outline_color": ?
    }
    """
    # create the rectangle dictionary
    house_rectangle = {}
    # create the rectangle ArtElement
    # house = Rectangle(house_rectangle)
    # add the house to the canvas
    # canvas.add_element(house)

    """
    draw the door as a rectangle with corner at (300, 600)
    width = 100
    height = 200
    fill = red = (255, 0, 0)
    outline_color = black = (0, 0, 0)
    door_rectangle = {
        "x": ?,
        "y": ?,
        "width": ?,
        "height": ?,
        "fill": ?,
        "outline_color": ?,
    }
    """
    # create the rectangle dictionary
    door_rectangle = {}
    # create the rectangle ArtElement
    # door = Rectangle(door_rectangle)
    # add the door to the canvas
    # canvas.add_element(door)

    # draw the window as a rectangle with corner at (500, 600)
    # width = 100
    # height = 100
    # fill = white = (255, 255, 255)
    # outline_color = black = (0, 0, 0)
    # create the rectangle dictionary
    window_rectangle = {}
    # create the rectangle ArtElement
    # window = Rectangle(window_rectangle)
    # add the window to the canvas
    # canvas.add_element(window)


def create_roof(canvas):
    # draw the roof as a triangle with xy corners at
    # [(200, 500), (700, 500), (450, 300)]
    # fill = burlywood =  (139, 115, 85)
    # outline_color = black = (0, 0, 0)
    # create the triangle dictionary
    roof_triangle = {}
    # create the triangle ArtElement
    # roof = Polygon(roof_triangle)
    # add the roof to the canvas
    # canvas.add_element(roof)


# Make a drawing of background and a house
def draw_landscape():
    # create the canvas
    WIDTH = 1000
    HEIGHT = 1000
    BACKGROUND_COLOR = (255, 255, 255)
    """
    canvas_dictionary = {
        "width": ?,
        "height": ?,
        "background_color": ?
    }
    """
    canvas_dictionary = {
        "width": WIDTH,
        "height": HEIGHT,
        "background_color": BACKGROUND_COLOR,
    }
    my_canvas = Canvas(*canvas_dictionary.values())

    # create the background
    create_background(my_canvas)

    # create the house
    create_house(my_canvas)

    # create the roof
    create_roof(my_canvas)

    # render the canvas
    my_canvas.render()

    # show the canvas
    my_canvas.show()

    pass


if __name__ == "__main__":
    # test_circles()
    # test_rectangles()
    # test_lines()
    draw_landscape()
