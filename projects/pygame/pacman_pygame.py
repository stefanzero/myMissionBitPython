import pygame
import sys
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 800
MAZE_WIDTH = 28
MAZE_HEIGHT = 29
CELL_SIZE = WIDTH // MAZE_WIDTH
# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Clock to control the frame rate
clock = pygame.time.Clock()
pacman = pygame.image.load("pacman.png")
pacman = pygame.transform.scale(pacman, (CELL_SIZE, CELL_SIZE))
# player_rect = pygame.Rect(WIDTH // 2 - 25, 10, 50, 50)
player_rect = pygame.Rect((WIDTH - CELL_SIZE) // 25, CELL_SIZE, CELL_SIZE, CELL_SIZE)
arrows = [
    pygame.K_RIGHT,
    pygame.K_LEFT,
    pygame.K_UP,
    pygame.K_DOWN,
]


def start_screen(screen):
    # Set up the window
    # window_width = 640
    # window_height = 640
    # window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Pac-Man Maze")

    screen.fill(BLACK)
    draw_maze()
    # Cap the frame rate
    clock.tick(FPS)
    # x = 0
    # y = 0
    # while x < WIDTH:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             sys.exit()
    #         if event.type == pygame.KEYDOWN:
    #             x += 10
    #             y += 10
    #             draw_pacman(x, y, screen, "right")
    #             pygame.display.update()


def draw_maze():
    screen.fill(BLACK)
    # Create a matrix of 1s using a list comprehension
    maze = [[1] * MAZE_WIDTH for _ in range(MAZE_HEIGHT)]
    for i in range(1, 13):
        maze[1][i] = 0
        maze[1][14 + i] = 0
    for j in range(2, 5):
        maze[j][1] = 0
        maze[j][6] = 0
        maze[j][12] = 0
        maze[j][15] = 0
        maze[j][21] = 0
        maze[j][26] = 0

    # Draw the maze
    for row in range(MAZE_HEIGHT):
        for col in range(MAZE_WIDTH):
            if maze[row][col] == 0:
                # Draw a empty space
                pygame.draw.rect(
                    screen,
                    WHITE,
                    (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE),
                )
            else:
                # Draw an empty space
                # pygame.draw.rect(screen, WHITE, (col * cell_size, row * cell_size, cell_size, cell_size))
                pass

    # Update the display
    # pygame.display.flip()


def draw_pacman():
    # player_rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, WHITE, player_rect)
    screen.blit(pacman, player_rect)


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
    player_speed = 1
    game_started = False
    draw_maze()
    draw_pacman()
    space_pressed = False
    pygame.display.flip()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if game_started:
                    game_started = True  # Set the flag to True to avoid calling start_screen repeatedly
                    continue  # Skip the rest of the loop until the game has started
                elif event.key == pygame.K_SPACE:
                    space_pressed = True
            elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                space_pressed = False

        keys = pygame.key.get_pressed()

        # Move the player
        # player_rect.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player_speed
        # player_rect.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * player_speed

        if keys:
            for key in keys:
                if key in arrows:
                    if key == pygame.K_RIGHT:
                        player_rect.x += player_speed
                    elif key == pygame.K_LEFT:
                        player_rect.x -= player_speed
                    elif key == pygame.K_UP:
                        player_rect.y -= player_speed
                    elif key == pygame.K_DOWN:
                        player_rect.y += player_speed
                    # Ensure the player stays within the screen boundaries
                    player_rect.x = max(
                        0, min(player_rect.x, WIDTH - player_rect.width)
                    )
                    player_rect.y = max(
                        0, min(player_rect.y, HEIGHT - player_rect.height)
                    )
                    draw_maze()
                    draw_pacman()
                    pygame.display.flip()
        # pygame.display.update()
        # Cap the frame rate
        clock.tick(FPS)
        # Countdown Timer Logic
        countdown_timer -= 1 / FPS  # Decrease the timer based on the frame rate
        if countdown_timer <= 0:
            running = False


start_screen(screen)
run()
# wait_for_key()

"""
    # Define the maze size
    maze_width = 12
    maze_height = 12

    # Define the maze layout
    maze = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    # Define the maze cell size
    # cell_size = window_width // maze_width
    cell_size = WIDTH // maze_width

    # Draw the maze
    for row in range(maze_height):
        for col in range(maze_width):
            if maze[row][col] == 1:
                # Draw a wall
                pygame.draw.rect(
                    screen,
                    BLACK,
                    (col * cell_size, row * cell_size, cell_size, cell_size),
                )
            else:
                # Draw an empty space
                pygame.draw.rect(screen, WHITE, (col * cell_size, row * cell_size, cell_size, cell_size))
                
    # Update the display
    pygame.display.flip()
"""
