import pygame
import sys
import os


os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 1200, 1200
MAZE_WIDTH = 32
MAZE_HEIGHT = 32
CELL_SIZE = WIDTH // MAZE_WIDTH
# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Clock to control the frame rate
clock = pygame.time.Clock()
pacman = pygame.image.load("pacman.png")
pacman = pygame.transform.scale(pacman, (CELL_SIZE, CELL_SIZE))


def get_initial_player_rect():
    """
    initial pacman position is i = 2, j = 1
    """
    i0 = 2
    j0 = 1
    x0 = i0 * CELL_SIZE
    y0 = j0 * CELL_SIZE
    player_rect = pygame.Rect(x0, y0, CELL_SIZE, CELL_SIZE)
    # player_rect = pygame.Rect((WIDTH - CELL_SIZE) // 25, CELL_SIZE, CELL_SIZE, CELL_SIZE)
    return player_rect


def create_maze():
    # Create a matrix of 1s using a list comprehension
    maze = [[1] * MAZE_WIDTH for _ in range(MAZE_HEIGHT)]
    """
    draw horizontal spaces
    """
    for i in range(2, 14):
        maze[1][i] = 0
        maze[1][14 + i] = 0
        maze[20][i] = 0
        maze[20][14 + i] = 0
    for i in range(2, 28):
        maze[5][i] = 0
        maze[29][i] = 0
    for i in range(2, 8):
        maze[8][i] = 0
        # maze[8][20 + i] = 0
        maze[8][29 - i] = 0
    for i in range(10, 14):
        maze[8][i] = 0
        # maze[8][6 + i] = 0
        maze[8][29 - i] = 0
    for i in range(10, 20):
        maze[11][i] = 0
        maze[17][i] = 0
    for i in range(2, 11):
        maze[14][i] = 0
        maze[14][17 + i] = 0
    for i in range(2, 14):
        maze[20][i] = 0
        maze[20][29 - i] = 0
    for i in range(2, 5):
        maze[23][i] = 0
        maze[23][29 - i] = 0
    for i in range(7, 23):
        maze[23][i] = 0
    for i in range(2, 8):
        maze[26][i] = 0
        maze[26][29 - i] = 0
    for i in range(10, 14):
        maze[26][i] = 0
        maze[26][29 - i] = 0
    for i in range(2, 28):
        maze[29][i] = 0

    """
    draw vertical spaces
    """
    for j in range(1, 9):
        maze[j][2] = 0
        maze[j][27] = 0
    for j in range(1, 27):
        maze[j][7] = 0
        maze[j][22] = 0
    for j in range(1, 6):
        maze[j][13] = 0
        maze[j][16] = 0
    for j in range(5, 9):
        maze[j][10] = 0
        maze[j][19] = 0
    for j in range(8, 12):
        maze[j][13] = 0
        maze[j][16] = 0
    for j in range(11, 21):
        maze[j][10] = 0
        maze[j][19] = 0
    for j in range(20, 24):
        maze[j][2] = 0
        maze[j][13] = 0
        maze[j][16] = 0
        maze[j][27] = 0
    for j in range(23, 27):
        maze[j][4] = 0
        maze[j][10] = 0
        maze[j][19] = 0
        maze[j][25] = 0
    for j in range(26, 30):
        maze[j][2] = 0
        maze[j][13] = 0
        maze[j][16] = 0
        maze[j][27] = 0

    return maze


def start_screen(screen):
    # Set up the window
    pygame.display.set_caption("Pac-Man")
    screen.fill(BLACK)
    clock.tick(FPS)


def draw_maze(maze):
    screen.fill(BLACK)
    # Draw the maze pathways
    for row in range(MAZE_HEIGHT):
        for col in range(MAZE_WIDTH):
            if maze[row][col] == 0:
                # Draw a empty space
                pygame.draw.rect(
                    screen,
                    WHITE,
                    (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE),
                )


def draw_dots(dots):
    # Draw the maze dots
    for row in range(MAZE_HEIGHT):
        for col in range(MAZE_WIDTH):
            if dots[row][col] == 0:
                # Draw a dot
                x = col * CELL_SIZE
                y = row * CELL_SIZE
                pygame.draw.circle(
                    screen, RED, (x + CELL_SIZE // 2, y + CELL_SIZE // 2), 2
                )


def eat_dots(dots, player_rect):
    i, j = get_maze_cell_from_pixel(player_rect.x, player_rect.y)
    dot_found = False
    if dots[j][i] == 0:
        dot_found = True
    dots[j][i] = 1
    return dot_found


def draw_pacman(player_rect):
    screen.blit(pacman, player_rect)


def get_pacman_cell(player_rect):
    return (player_rect.x // CELL_SIZE, player_rect.y // CELL_SIZE)


def get_maze_cell_from_pixel(x, y):
    return (x // CELL_SIZE, y // CELL_SIZE)


def is_valid_pixel(x, y, maze):
    """
    x and y are floats
    i and j are ints
    cell is valid if it's not a wall and not out of bounds
    cell is a wall if it's a 1
    """
    i = int(x // CELL_SIZE)
    j = int(y // CELL_SIZE)
    return 0 <= i < MAZE_WIDTH and 0 <= j < MAZE_HEIGHT and maze[j][i] != 1


def is_valid_cell(x, y, maze):
    """
    Let dx = dy = cell size
    Let dx3 = dy3 = one third of the cell size floating point
    A pacman location is considered valid if these 4 points are all valid:
    (x + dx3, y + dy3)
    (x + 2 * dx3, y + dy3)
    (x + dx3, y + 2 * dy3)
    (x + 2 * dx3, y + 2 * dy3))
    """
    dx3 = dy3 = CELL_SIZE / 3
    return (
        is_valid_pixel(x + dx3, y + dy3, maze)
        and is_valid_pixel(x + dx3, y + dy3, maze)
        and is_valid_pixel(x + dx3, y + dy3, maze)
        and is_valid_pixel(x + dx3, y + dy3, maze)
    )


def wait_for_key():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False


def run():
    running = True
    countdown_timer = 60
    player_speed = 2
    score = 0
    game_started = False
    maze = create_maze()
    dots = create_maze()
    player_rect = get_initial_player_rect()
    draw_maze(maze)
    draw_dots(dots)
    draw_pacman(player_rect)
    # space_pressed = False
    pygame.display.flip()
    wait_for_key()

    while running:
        # Cap the frame rate
        clock.tick(FPS)
        # Countdown Timer Logic
        countdown_timer -= 1 / FPS  # Decrease the timer based on the frame rate
        if countdown_timer <= 0:
            break
            # running = False
        for event in pygame.event.get():
            # Check if the user closed the window
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if game_started:
                    game_started = True  # Set the flag to True to avoid calling start_screen repeatedly
                    continue  # Skip the rest of the loop until the game has started

        keys = pygame.key.get_pressed()

        if keys:
            update = False
            x, y = player_rect.x, player_rect.y
            if keys[pygame.K_RIGHT]:
                x += player_speed
                update = True
            elif keys[pygame.K_LEFT]:
                x -= player_speed
                update = True
            elif keys[pygame.K_UP]:
                y -= player_speed
                update = True
            elif keys[pygame.K_DOWN]:
                y += player_speed
                update = True
            # q quits the game
            elif keys[pygame.K_q]:
                running = False
            if not update:
                continue
            if not is_valid_cell(x, y, maze):
                continue
            player_rect.x = x
            player_rect.y = y
            draw_maze(maze)
            if eat_dots(dots, player_rect):
                score += 10
            draw_dots(dots)
            draw_pacman(player_rect)
            pygame.display.flip()


if __name__ == "__main__":
    start_screen(screen)
    run()
