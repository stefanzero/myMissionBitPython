import asyncio
import pygame
import sys
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Initialize Pygame
pygame.init()
# The top row is for clickable squares
NUM_ROWS = 7
NUM_COLS = 7

# 1.83
BROWSER_ASPECT_RATIO = 1980 / 1080
WIDTH, HEIGHT = 1200, 1200
# HEIGHT = 1200
# WIDTH = int(HEIGHT * BROWSER_ASPECT_RATIO)
CAPTION = "Connect 4"
TITLE_WIDTH = WIDTH
TITLE_HEIGHT = 100
TITLE_FONT_SIZE = 50
TITLE_COLOR = (255, 255, 255)
FOOTER_HEIGHT = TITLE_HEIGHT
BUTTON_HEIGHT = 50
BUTTON_WIDTH = 200
BODY_HEIGHT = HEIGHT - TITLE_HEIGHT - FOOTER_HEIGHT

LINE_WIDTH = 10
LINE_WIDTH_2 = 5
WIN_LINE_WIDTH = 15
SQUARE_SIZE = 100
BOARD_WIDTH = NUM_COLS * SQUARE_SIZE + (NUM_COLS + 1) * LINE_WIDTH
BOARD_HEIGHT = NUM_ROWS * SQUARE_SIZE + (NUM_ROWS + 1) * LINE_WIDTH
BOARD_LEFT_MARGIN = (WIDTH - BOARD_WIDTH) // 2
BOARD_TOP_MARGIN = TITLE_HEIGHT + (BODY_HEIGHT - BOARD_HEIGHT) // 2
BOARD_ROWS = NUM_ROWS
BOARD_COLS = NUM_COLS
# CIRCLE_RADIUS = 30
CIRCLE_RADIUS = SQUARE_SIZE // 3
# CIRCLE_WIDTH = 15
CIRCLE_WIDTH = CIRCLE_RADIUS
# CROSS_WIDTH = 25
# SPACE = 55

FOOTER_TOP_MARGIN = HEIGHT - FOOTER_HEIGHT

RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
KHAKI = (240, 230, 140)
BG_COLOR = (107, 230, 224)
SELECTABLE_COLOR = KHAKI
BUTTON_BG_COLOR = pygame.Color(0, 0, 0)
BUTTON_BG_COLOR.hsla = (177, 71, 50, 1)
BUTTON_HOVER_BG_COLOR = pygame.Color(0, 0, 0)
BUTTON_HOVER_BG_COLOR.hsla = (177, 71, 70, 1)
BUTTON_BORDER_RADIUS = 10
TITLE_BG_COLOR = (95, 30, 174)
FOOTER_BG_COLOR = TITLE_BG_COLOR
TITLE_COLOR = WHITE
BOARD_COLOR = (113, 125, 141)
LINE_COLOR = (255, 255, 255)

# arial_30 = pygame.font.Font("arial.ttf", size=30)
TITLE_FONT_FAMILY = "arial"
TITLE_FONT_SIZE = 50
TITLE_FONT = pygame.font.SysFont(TITLE_FONT_FAMILY, TITLE_FONT_SIZE, bold=True)
BUTTON_FONT_FAMILY = "arial"
BUTTON_FONT_SIZE = 20
BUTTON_FONT = pygame.font.SysFont(BUTTON_FONT_FAMILY, size=BUTTON_FONT_SIZE)


def create_screen():
    """
    Creates the game screen.

    Returns
    -------
    screen : pygame.Surface
        The created game screen.
    """
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(CAPTION)
    screen.fill(BG_COLOR)
    return screen


def draw_title(screen):
    """
    Draws the title of the game on the screen.

    Parameters
    ----------
    screen : pygame.Surface
        The screen to draw the title on.

    """
    title_text = TITLE_FONT.render(CAPTION, True, TITLE_COLOR)
    title_rect = title_text.get_rect(center=(TITLE_WIDTH // 2, TITLE_HEIGHT // 2))
    pygame.draw.rect(screen, TITLE_BG_COLOR, (0, 0, TITLE_WIDTH, TITLE_HEIGHT))
    screen.blit(title_text, title_rect)


def create_button(action=None):
    """
    Creates a button with the specified action.

    Args:
        action (function): The function to be called when the button is clicked.

    Returns:
        Button: The created button.
    """
    left = (WIDTH - BUTTON_WIDTH) // 2
    top = FOOTER_TOP_MARGIN + (FOOTER_HEIGHT - BUTTON_HEIGHT) // 2
    button = Button(
        text="Reset Game",
        left=left,
        top=top,
        width=BUTTON_WIDTH,
        height=BUTTON_HEIGHT,
        font=BUTTON_FONT,
        text_color=WHITE,
        button_color=BUTTON_BG_COLOR,
        button_hover_color=BUTTON_HOVER_BG_COLOR,
        border_radius=BUTTON_BORDER_RADIUS,
        action=action,
    )
    return button


def draw_footer(screen, button=None):
    """
    Draw the footer of the game window.

    The footer is drawn with a background color of FOOTER_BG_COLOR
    and a height of FOOTER_HEIGHT. If a button is provided, it is
    drawn on top of the footer.

    Parameters
    ----------
    screen : pygame.Surface
        The surface to draw the footer on
    button : Button, optional
        The button to draw on top of the footer
    """
    pygame.draw.rect(
        screen,
        FOOTER_BG_COLOR,
        (0, FOOTER_TOP_MARGIN, WIDTH, FOOTER_HEIGHT),
    )
    if button:
        button.draw(screen)


class Button:
    def __init__(
        self,
        top,
        left,
        width,
        height,
        text,
        font=None,
        text_color=BLACK,
        button_color=BUTTON_BG_COLOR,
        button_hover_color=BUTTON_HOVER_BG_COLOR,
        border_radius=BUTTON_BORDER_RADIUS,
        action=None,
    ):
        """
        Initialize a Button object.

        Parameters:
        top (int): y-coordinate of the button
        left (int): x-coordinate of the button
        width (int): width of the button
        height (int): height of the button
        text (str): text of the button
        font (pygame.font.Font): font of the button, defaults to Arial 30
        text_color (tuple): color of the button text, defaults to BLACK
        button_color (tuple): color of the button, defaults to BUTTON_BG_COLOR
        button_hover_color (tuple): color of the button when hovered, defaults to BUTTON_HOVER_BG_COLOR
        border_radius (int): border radius of the button, defaults to BUTTON_BORDER_RADIUS
        action (function): action to take when the button is clicked, defaults to None
        """
        self.rect = pygame.Rect(
            left,
            top,
            width,
            height,
        )
        self.text = text
        if font:
            self.font = font
        else:
            self.font = pygame.font.SysFont("arial", 30, bold=True)
        self.text_color = text_color
        self.button_color = button_color
        self.button_hover_color = button_hover_color
        self.border_radius = border_radius
        self.action = action
        self.color = button_color
        self.hover_color = button_hover_color
        self.is_hovered = False

    def set_action(self, action):
        """
        Sets the action to be performed when the button is clicked.

        Parameters
        ----------
        action : callable
            The action to be performed when the button is clicked.
        """
        self.action = action

    def draw(self, surface):
        """
        Draws the button on the given surface.

        Parameters
        ----------
        surface : pygame.Surface
            The surface to draw the button on.

        Returns
        -------
        bool
            True if the hover state changed or the button was clicked.
        """
        current_color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(
            surface, current_color, self.rect, border_radius=self.border_radius
        )

        text_surface = self.font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    # return True if the hover state changes or button was clicked
    def update(self, event, screen):
        """
        Update the button state based on the given event.

        If the event is a MOUSEBUTTONDOWN event with the left mouse button,
        return True if the button was clicked.
        If the event is a MOUSEMOTION event, return True if the hover state
        of the button changed.

        Parameters:
            event (pygame.event.Event): the event to be handled

        Returns:
            bool: whether the button state changed
        """
        is_hovered = False
        if (
            event.type == pygame.MOUSEBUTTONDOWN and event.button == 1
        ):  # Left mouse button
            if self.rect.collidepoint(event.pos):
                return True
        elif event.type == pygame.MOUSEMOTION:
            is_hovered = self.rect.collidepoint(event.pos)
            if is_hovered != self.is_hovered:
                self.is_hovered = is_hovered
                return True
        elif event.type == pygame.FINGERDOWN:
            x = int(event.x * screen.get_height())
            y = int(event.y * screen.get_width())
            if self.rect.collidepoint(x, y):
                return True
        return False

    def handle_event(self, event, screen):
        """
        Handle events related to the button.

        Parameters:
            event (pygame.event.Event): the event to be handled

        If the event is a MOUSEMOTION event, update the hover state of the button.
        If the event is a MOUSEBUTTONDOWN event with the left mouse button, and the button is hovered, call the action of the button.
        """
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
        elif (
            event.type == pygame.MOUSEBUTTONDOWN and event.button == 1
        ):  # Left mouse button
            if self.rect.collidepoint(event.pos):
                if self.action:
                    self.action()
        elif event.type == pygame.FINGERDOWN:
            x = int(event.x * screen.get_height())
            y = int(event.y * screen.get_width())
            if self.rect.collidepoint(x, y):
                if self.action:
                    self.action()


class Board:
    def __init__(self):
        """
        Initialize a Board object.

        Order the board in column, row, so when a square is clicked,
        the rows are looped until an empty square is found.

        self.board[j][i] = column j, row i

        row 0 is special - it is the row above the highest row where
        a square can be clicked to drop a piece into the column.

        This function initializes a Board object by creating a 2D list of Square objects
        and storing them in the Board object's `squares` attribute.

        The Board object represents a Connect 4 game board.
        """
        # self.board = []
        # for i in range(NUM_COLS):
        #     column = [None] * (NUM_ROWS + 1)
        #     self.board.append(column)
        self.squares = [[None] * NUM_ROWS for _ in range(NUM_COLS)]
        self.winner = None
        # create Square objects and store them in the 2D list
        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                x = BOARD_LEFT_MARGIN + col * (SQUARE_SIZE + LINE_WIDTH) + LINE_WIDTH
                y = BOARD_TOP_MARGIN + row * (SQUARE_SIZE + LINE_WIDTH) + LINE_WIDTH
                square = Square(x, y, SQUARE_SIZE)
                self.squares[col][row] = square

    def draw(self, screen, marker=RED):
        """
        Draw the board on the screen.

        This function fills the screen with the background color,
        draws a filled rectangle for the board, draws horizontal and
        vertical lines for the grid, and draws the markers for each
        square in the grid.

        Parameters:
            screen (pygame.Surface): the surface to draw on
        """
        screen.fill(BG_COLOR)
        # draw a filled rectangle before the lines
        pygame.draw.rect(
            screen,
            BOARD_COLOR,
            (BOARD_LEFT_MARGIN, BOARD_TOP_MARGIN, BOARD_WIDTH, BOARD_HEIGHT),
        )
        x = BOARD_LEFT_MARGIN
        y = BOARD_TOP_MARGIN + LINE_WIDTH_2
        # draw horizontal lines
        for row in range(BOARD_ROWS + 1):
            pygame.draw.line(
                screen,
                LINE_COLOR,
                (x, y),
                (x + BOARD_WIDTH, y),
                LINE_WIDTH,
            )
            y += SQUARE_SIZE + LINE_WIDTH

        # draw vertical lines
        x = BOARD_LEFT_MARGIN + LINE_WIDTH_2
        y = BOARD_TOP_MARGIN
        for col in range(BOARD_COLS + 1):
            pygame.draw.line(
                screen,
                LINE_COLOR,
                (x, y),
                (x, y + BOARD_HEIGHT),
                LINE_WIDTH,
            )
            x += SQUARE_SIZE + LINE_WIDTH

        # set the properties of the clickable squares
        for col in range(NUM_COLS):
            self.squares[col][0].marker = marker
            self.squares[col][0].selectable = True

        # draw the squares and markers
        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                square = self.squares[col][row]
                square.draw(screen)

    def check_winner(self):  # check if there is a winner
        """
        if 4 markers are in a row, return the marker
        if there is no winner, return None
        """
        # check for horizontal win
        for row in range(1, NUM_ROWS):
            for col in range(NUM_COLS - 3):
                marker = self.squares[col][row].marker
                if marker:  # if there is a marker
                    if (
                        marker == self.squares[col + 1][row].marker
                        and marker == self.squares[col + 2][row].marker
                        and marker == self.squares[col + 3][row].marker
                    ):
                        # add highlight to the winning squares
                        start = col
                        for col in range(start, start + 4):
                            self.squares[col][row].highlight = True
                        self.winner = marker
                        return marker  # return the marker if there is a winner
        # check for vertical win
        for col in range(NUM_COLS):
            for row in range(1, NUM_ROWS - 3):
                marker = self.squares[col][row].marker
                if marker:  # if there is a marker
                    if (
                        marker == self.squares[col][row + 1].marker
                        and marker == self.squares[col][row + 2].marker
                        and marker == self.squares[col][row + 3].marker
                    ):
                        # add highlight to the winning squares
                        start = row
                        for row in range(start, start + 4):
                            self.squares[col][row].highlight = True
                        self.winner = marker
                        return marker  # return the marker if there is a winner
        # check for downward diagonal win
        for col in range(NUM_COLS - 3):
            for row in range(1, NUM_ROWS - 4):
                marker = self.squares[col][row].marker
                if marker:  # if there is a marker
                    if (
                        marker == self.squares[col + 1][row + 1].marker
                        and marker == self.squares[col + 2][row + 2].marker
                        and marker == self.squares[col + 3][row + 3].marker
                    ):
                        # add highlight to the winning diagonal
                        for i in range(4):
                            self.squares[col + i][row + i].highlight = True
                        self.winner = marker
                        return marker  # return the marker if there is a winner
        # check for upward diagonal win
        for col in range(NUM_COLS - 3):
            for row in range(NUM_ROWS - 1, NUM_ROWS - 4, -1):
                marker = self.squares[col][row].marker
                if marker:  # if there is a marker
                    if (
                        marker == self.squares[col + 1][row - 1].marker
                        and marker == self.squares[col + 2][row - 2].marker
                        and marker == self.squares[col + 3][row - 3].marker
                    ):
                        # add highlight to the winning diagonal
                        for i in range(4):
                            self.squares[col + i][row - i].highlight = True
                        self.winner = marker
                        return marker  # return the marker if there is a winner
        return None  # return None if there is no winner

    def handle_click(self, x, y):
        """
        only row 0 represents columns that can be clicked
        """
        row = 0
        for col in range(NUM_COLS):
            square = self.squares[col][row]
            if square.point_in_square(x, y):
                break
            else:
                square = None

        if square:
            self.add_marker(col, square.marker)
            return square
        else:
            return None

    def reset(self):
        self.winner = None
        for row in range(1, NUM_ROWS):
            for col in range(NUM_COLS):
                self.squares[col][row].marker = None
                self.squares[col][row].highlight = None

    def add_marker(self, col, marker):
        for row in range(NUM_ROWS - 1, 0, -1):
            if self.squares[col][row].marker is None:
                self.squares[col][row].marker = marker
                return


class Square:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.xy1 = (x, y)
        self.xy2 = (x + size, y + size)
        self.size = size
        # marker can be None, RED, or BLUE
        self.marker = None
        self.highlight = False
        self.selectable = False

    def point_in_square(self, x, y):
        """
        Check if a point is inside the square.

        Parameters:
            x (int): the x coordinate of the point
            y (int): the y coordinate of the point

        Returns:
            bool: True if the point is inside the square, False otherwise
        """
        return (
            x > self.x
            and x < self.x + self.size
            and y > self.y
            and y < self.y + self.size
        )

    def draw(self, screen):
        """
        Draw a square on the given screen.

        If the square has a marker, it will be drawn in the correct color.
        If the square is highlighted, it will be drawn in the background color.
        Otherwise, it will be drawn in black.

        Parameters:
            screen (pygame.Surface): The screen to draw on.
        """
        if not self.marker:
            return

        if self.selectable:
            color = SELECTABLE_COLOR
        elif self.highlight:
            color = BG_COLOR
        else:
            color = BLACK
        pygame.draw.rect(
            screen,
            color,
            (self.x, self.y, self.size, self.size),
        )
        pygame.draw.circle(
            screen,
            self.marker,
            (self.x + self.size // 2, self.y + self.size // 2),
            CIRCLE_RADIUS,
            CIRCLE_WIDTH,
        )

    def handle_click(self, x, y):
        if self.point_in_square(x, y):
            return self  # return the square if it is clicked
        return None


def is_running_in_browser():
    """
    Check if the script is running in a browser environment.

    This function checks if the 'pyodide' module is available
    (used by PyScript) or if the 'js' module is available
    (used by PyScript or other JavaScript bindings).

    Returns:
        bool: True if running in a browser environment, False otherwise
    """
    if "pyodide" in sys.modules:
        return True
    try:
        import js  # Access JavaScript globals if available

        return True
    except ImportError:
        pass
    return False


async def main():
    """
    Main game loop.

    Initializes the game board, screen, and buttons. Then,
    enters a loop where it processes events, updates the game
    state, and redraws the screen.

    Exits the loop when the user closes the window or presses the
    'q' key when not running in a browser.
    """
    # browser = is_running_in_browser()
    browser = False
    board = Board()
    screen = create_screen()
    current_marker = RED
    game_started = False
    running = True
    board.draw(screen, current_marker)
    draw_title(screen)
    button = create_button(action=board.reset)
    draw_footer(screen, button)
    pygame.display.flip()
    update = False
    while running:
        for event in pygame.event.get():
            # print(event)
            # Check if the user closed the window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Check if the user pressed a key or clicked the mouse
            if (
                event.type == pygame.KEYDOWN
                or event.type == pygame.MOUSEBUTTONDOWN
                or event.type == pygame.FINGERDOWN
            ):
                if not game_started:
                    print("Game started")
                    game_started = True
                    # Skip the rest of the loop to get next event
                    continue
            update = False
            keys = pygame.key.get_pressed()
            # q quits the game if not running in a browser
            if keys[pygame.K_q] and not browser:
                running = False
            # update the screen if the button is clicked or hovered
            if button.update(event, screen):
                update = True
                button.handle_event(event, screen)
            # handle a mouse click or touch event only if the game is still in play
            elif not board.winner and (
                event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.FINGERDOWN
            ):
                x, y = None, None
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                elif event.type == pygame.FINGERDOWN:
                    x = int(event.x * screen.get_height())
                    y = int(event.y * screen.get_width())
                if x and y:
                    square = board.handle_click(x, y)
                    # update the screen if the user clicked on a selectable square
                    if square:
                        square.marker = current_marker
                        # update the current player
                        current_marker = BLUE if current_marker == RED else RED
                        # after a move, check if there is a winner
                        if board.check_winner():
                            print(f"Player {board.winner} wins!")
                        # elif board.check_draw():
                        #     print("It's a draw!")
                        update = True

            # the update flag prevents unnecessary redraws
            if update:
                update = False
                board.draw(screen, current_marker)
                draw_title(screen)
                draw_footer(screen, button)
                pygame.display.flip()

            # Let other tasks run
            await asyncio.sleep(0)


# This is the program entry point
asyncio.run(main())
