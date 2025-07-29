# import pygame
# import sys

# # Initialize Pygame
# pygame.init()

# # Set up some constants
# WIDTH = 600
# HEIGHT = 600
# LINE_WIDTH = 15
# WIN_LINE_WIDTH = 15
# BOARD_ROWS = 3
# BOARD_COLS = 3
# SQUARE_SIZE = 200
# CIRCLE_RADIUS = 60
# CIRCLE_WIDTH = 15
# CROSS_WIDTH = 25
# SPACE = 55
# # RGB
# RED = (255, 0, 0)
# BG_COLOR = (28, 170, 156)
# LINE_COLOR = (23, 145, 135)
# CIRCLE_COLOR = (239, 231, 200)
# CROSS_COLOR = (66, 66, 66)

# # Set up the display
# SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("TIC TAC TOE")

# # Board
# board = [[None] * BOARD_COLS for _ in range(BOARD_ROWS)]

# # Pygame Clock
# clock = pygame.time.Clock()


# def draw_lines():
#     # 1st horizontal
#     pygame.draw.line(
#         SCREEN, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH
#     )
#     # 2nd horizontal
#     pygame.draw.line(
#         SCREEN, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH
#     )

#     # 1st vertical
#     pygame.draw.line(
#         SCREEN, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH
#     )
#     # 2nd vertical
#     pygame.draw.line(
#         SCREEN, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH
#     )


# def draw_figures():
#     for row in range(BOARD_ROWS):
#         for col in range(BOARD_COLS):
#             if board[row][col] == "X":
#                 pygame.draw.line(
#                     SCREEN,
#                     CROSS_COLOR,
#                     (
#                         col * SQUARE_SIZE + SPACE,
#                         row * SQUARE_SIZE + SQUARE_SIZE - SPACE,
#                     ),
#                     (
#                         col * SQUARE_SIZE + SQUARE_SIZE - SPACE,
#                         row * SQUARE_SIZE + SPACE,
#                     ),
#                     CROSS_WIDTH,
#                 )
#                 pygame.draw.line(
#                     SCREEN,
#                     CROSS_COLOR,
#                     (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
#                     (
#                         col * SQUARE_SIZE + SQUARE_SIZE - SPACE,
#                         row * SQUARE_SIZE + SQUARE_SIZE - SPACE,
#                     ),
#                     CROSS_WIDTH,
#                 )
#             elif board[row][col] == "O":
#                 pygame.draw.circle(
#                     SCREEN,
#                     CIRCLE_COLOR,
#                     (
#                         col * SQUARE_SIZE + SQUARE_SIZE // 2,
#                         row * SQUARE_SIZE + SQUARE_SIZE // 2,
#                     ),
#                     CIRCLE_RADIUS,
#                     CIRCLE_WIDTH,
#                 )


# def mark_square(row, col, player):
#     board[row][col] = player


# def available_square(row, col):
#     return board[row][col] is None


# def is_board_full():
#     for row in range(BOARD_ROWS):
#         for col in range(BOARD_COLS):
#             if board[row][col] is None:
#                 return False
#     return True


# def check_win(player):
#     # vertical win check
#     for col in range(BOARD_COLS):
#         if (
#             board[0][col] == player
#             and board[1][col] == player
#             and board[2][col] == player
#         ):
#             return True

#     # horizontal win check
#     for row in range(BOARD_ROWS):
#         if (
#             board[row][0] == player
#             and board[row][1] == player
#             and board[row][2] == player
#         ):
#             return True

#     # asc diagonal win check
#     if board[2][0] == player and board[1][1] == player and board[0][2] == player:
#         return True

#     # desc diagonal win check
#     if board[0][0] == player and board[1][1] == player and board[2][2] == player:
#         return True

#     return False


# def restart():
#     SCREEN.fill(BG_COLOR)
#     draw_lines()
#     player = "X"
#     for row in range(BOARD_ROWS):
#         for col in range(BOARD_COLS):
#             board[row][col] = None
#     return player


# player = "X"

# # # Game loop
# # # Game loop
# # while True:
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             sys.exit()

# #         if event.type == pygame.MOUSEBUTTONDOWN and not is_board_full():
# #             mouseX = event.pos[0]  # x
# #             mouseY = event.pos[1]  # y
# #             clicked_row = int(mouseY // SQUARE_SIZE)
# #             clicked_col = int(mouseX // SQUARE_SIZE)

# #             if available_square(clicked_row, clicked_col):

# #                 mark_square(clicked_row, clicked_col, player)
# #                 if check_win(player):
# #                     print(f"Player {player} wins!")
# #                     pygame.display.update()
# #                     pygame.time.wait(2000)
# #                     player = restart()
# #                 else:
# #                     player = "O" if player == "X" else "X"

# #     SCREEN.fill(BG_COLOR)
# #     draw_lines()
# #     draw_figures()
# #     pygame.display.update()
# #     clock.tick(60)

# # Game loop
# winner = None
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()

#         if (
#             event.type == pygame.MOUSEBUTTONDOWN
#             and not is_board_full()
#             and winner is None
#         ):
#             mouseX = event.pos[0]  # x
#             mouseY = event.pos[1]  # y
#             clicked_row = int(mouseY // SQUARE_SIZE)
#             clicked_col = int(mouseX // SQUARE_SIZE)

#             if available_square(clicked_row, clicked_col):

#                 mark_square(clicked_row, clicked_col, player)
#                 if check_win(player):
#                     winner = player
#                     print(f"Player {winner} wins!")
#                 else:
#                     player = "O" if player == "X" else "X"

#     SCREEN.fill(BG_COLOR)
#     draw_lines()
#     for row in range(BOARD_ROWS):
#         for col in range(BOARD_COLS):
#             if board[row][col] == "X":
#                 if winner == "X":
#                     pygame.draw.line(
#                         SCREEN,
#                         RED,
#                         (
#                             col * SQUARE_SIZE + SPACE,
#                             row * SQUARE_SIZE + SQUARE_SIZE - SPACE,
#                         ),
#                         (
#                             col * SQUARE_SIZE + SQUARE_SIZE - SPACE,
#                             row * SQUARE_SIZE + SPACE,
#                         ),
#                         CROSS_WIDTH,
#                     )
#                     pygame.draw.line(
#                         SCREEN,
#                         RED,
#                         (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
#                         (
#                             col * SQUARE_SIZE + SQUARE_SIZE - SPACE,
#                             row * SQUARE_SIZE + SQUARE_SIZE - SPACE,
#                         ),
#                         CROSS_WIDTH,
#                     )
#                 else:
#                     pygame.draw.line(
#                         SCREEN,
#                         CROSS_COLOR,
#                         (
#                             col * SQUARE_SIZE + SPACE,
#                             row * SQUARE_SIZE + SQUARE_SIZE - SPACE,
#                         ),
#                         (
#                             col * SQUARE_SIZE + SQUARE_SIZE - SPACE,
#                             row * SQUARE_SIZE + SPACE,
#                         ),
#                         CROSS_WIDTH,
#                     )
#                     pygame.draw.line(
#                         SCREEN,
#                         CROSS_COLOR,
#                         (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
#                         (
#                             col * SQUARE_SIZE + SQUARE_SIZE - SPACE,
#                             row * SQUARE_SIZE + SQUARE_SIZE - SPACE,
#                         ),
#                         CROSS_WIDTH,
#                     )
#             elif board[row][col] == "O":
#                 if winner == "O":
#                     pygame.draw.circle(
#                         SCREEN,
#                         RED,
#                         (
#                             col * SQUARE_SIZE + SQUARE_SIZE // 2,
#                             row * SQUARE_SIZE + SQUARE_SIZE // 2,
#                         ),
#                         CIRCLE_RADIUS,
#                         CIRCLE_WIDTH,
#                     )
#                 else:
#                     pygame.draw.circle(
#                         SCREEN,
#                         CIRCLE_COLOR,
#                         (
#                             col * SQUARE_SIZE + SQUARE_SIZE // 2,
#                             row * SQUARE_SIZE + SQUARE_SIZE // 2,
#                         ),
#                         CIRCLE_RADIUS,
#                         CIRCLE_WIDTH,
#                     )
#     pygame.display.update()
#     clock.tick(60)

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
WIN_LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = 200
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55
# RGB
RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

# Set up the display
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT + 100))
pygame.display.set_caption("TIC TAC TOE")

# Board
board = [[None] * BOARD_COLS for _ in range(BOARD_ROWS)]

# Pygame Clock
clock = pygame.time.Clock()


def draw_lines():
    # 1st horizontal
    pygame.draw.line(
        SCREEN, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH
    )
    # 2nd horizontal
    pygame.draw.line(
        SCREEN, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH
    )

    # 1st vertical
    pygame.draw.line(
        SCREEN, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH
    )
    # 2nd vertical
    pygame.draw.line(
        SCREEN, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH
    )


def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == "X":
                pygame.draw.line(
                    SCREEN,
                    CROSS_COLOR,
                    (
                        col * SQUARE_SIZE + SPACE,
                        row * SQUARE_SIZE + SQUARE_SIZE - SPACE,
                    ),
                    (
                        col * SQUARE_SIZE + SQUARE_SIZE - SPACE,
                        row * SQUARE_SIZE + SPACE,
                    ),
                    CROSS_WIDTH,
                )
                pygame.draw.line(
                    SCREEN,
                    CROSS_COLOR,
                    (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                    (
                        col * SQUARE_SIZE + SQUARE_SIZE - SPACE,
                        row * SQUARE_SIZE + SQUARE_SIZE - SPACE,
                    ),
                    CROSS_WIDTH,
                )
            elif board[row][col] == "O":
                pygame.draw.circle(
                    SCREEN,
                    CIRCLE_COLOR,
                    (
                        col * SQUARE_SIZE + SQUARE_SIZE // 2,
                        row * SQUARE_SIZE + SQUARE_SIZE // 2,
                    ),
                    CIRCLE_RADIUS,
                    CIRCLE_WIDTH,
                )


def mark_square(row, col, player):
    board[row][col] = player


def available_square(row, col):
    return board[row][col] is None


def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] is None:
                return False
    return True


def check_win(player):
    # vertical win check
    for col in range(BOARD_COLS):
        if (
            board[0][col] == player
            and board[1][col] == player
            and board[2][col] == player
        ):
            return True

    # horizontal win check
    for row in range(BOARD_ROWS):
        if (
            board[row][0] == player
            and board[row][1] == player
            and board[row][2] == player
        ):
            return True

    # asc diagonal win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        return True

    # desc diagonal win check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True

    return False


def restart():
    SCREEN.fill(BG_COLOR)
    draw_lines()
    player = "X"
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = None
    return player


def draw_button(text, x, y, width, height, color, hover_color):
    pygame.draw.rect(SCREEN, color, (x, y, width, height))
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, (255, 255, 255))
    SCREEN.blit(
        text_surface,
        (
            x + width // 2 - text_surface.get_width() // 2,
            y + height // 2 - text_surface.get_height() // 2,
        ),
    )


def main():
    player = "X"
    winner = None
    start_button_enabled = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and start_button_enabled:
                start_button_enabled = False

            if (
                event.type == pygame.MOUSEBUTTONDOWN
                and not start_button_enabled
                and not is_board_full()
                and winner is None
            ):
                mouseX = event.pos[0]  # x
                mouseY = event.pos[1]  # y
                if mouseY < HEIGHT:
                    clicked_row = int(mouseY // SQUARE_SIZE)
                    clicked_col = int(mouseX // SQUARE_SIZE)

                    if available_square(clicked_row, clicked_col):

                        mark_square(clicked_row, clicked_col, player)
                        if check_win(player):
                            winner = player
                            print(f"Player {winner} wins!")
                        else:
                            player = "O" if player == "X" else "X"

        SCREEN.fill(BG_COLOR)
        if start_button_enabled:
            draw_button(
                "Start",
                WIDTH // 2 - 100,
                HEIGHT + 25,
                200,
                50,
                (0, 255, 0),
                (0, 200, 0),
            )
        else:
            draw_lines()
            for row in range(BOARD_ROWS):
                for col in range(BOARD_COLS):
                    if board[row][col] == "X":
                        if winner == "X":
                            pygame.draw.line(
                                SCREEN,
                                RED,
                                (
                                    col * SQUARE_SIZE + SPACE,
                                    row * SQUARE_SIZE + SQUARE_SIZE - SPACE,
                                ),
                                (
                                    col * SQUARE_SIZE + SQUARE_SIZE - SPACE,
                                    row * SQUARE_SIZE + SPACE,
                                ),
                                CROSS_WIDTH,
                            )
                            pygame.draw.line(
                                SCREEN,
                                RED,
                                (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                (
                                    col * SQUARE_SIZE + SQUARE_SIZE - SPACE,
                                    row * SQUARE_SIZE + SQUARE_SIZE - SPACE,
                                ),
                                CROSS_WIDTH,
                            )
                        else:
                            pygame.draw.line(
                                SCREEN,
                                CROSS_COLOR,
                                (
                                    col * SQUARE_SIZE + SPACE,
                                    row * SQUARE_SIZE + SQUARE_SIZE - SPACE,
                                ),
                                (
                                    col * SQUARE_SIZE + SQUARE_SIZE - SPACE,
                                    row * SQUARE_SIZE + SPACE,
                                ),
                                CROSS_WIDTH,
                            )
                            pygame.draw.line(
                                SCREEN,
                                CROSS_COLOR,
                                (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                (
                                    col * SQUARE_SIZE + SQUARE_SIZE - SPACE,
                                    row * SQUARE_SIZE + SQUARE_SIZE - SPACE,
                                ),
                                CROSS_WIDTH,
                            )
                    elif board[row][col] == "O":
                        if winner == "O":
                            pygame.draw.circle(
                                SCREEN,
                                RED,
                                (
                                    col * SQUARE_SIZE + SQUARE_SIZE // 2,
                                    row * SQUARE_SIZE + SQUARE_SIZE // 2,
                                ),
                                CIRCLE_RADIUS,
                                CIRCLE_WIDTH,
                            )
                        else:
                            pygame.draw.circle(
                                SCREEN,
                                CIRCLE_COLOR,
                                (
                                    col * SQUARE_SIZE + SQUARE_SIZE // 2,
                                    row * SQUARE_SIZE + SQUARE_SIZE // 2,
                                ),
                                CIRCLE_RADIUS,
                                CIRCLE_WIDTH,
                            )
            if winner is not None:
                start_button_enabled = True
                winner = None
        pygame.display.update()
        clock.tick(60)
