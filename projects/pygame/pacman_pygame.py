import pygame
import sys

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 800
# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Clock to control the frame rate
clock = pygame.time.Clock()


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


def draw_maze():
    maze_width = 28
    maze_height = 29
    # Create a matrix of 1s using a list comprehension
    maze = [[1] * maze_width for _ in range(maze_height)]
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
    cell_size = WIDTH // maze_width

    # Draw the maze
    for row in range(maze_height):
        for col in range(maze_width):
            if maze[row][col] == 0:
                # Draw a empty space
                pygame.draw.rect(
                    screen,
                    WHITE,
                    (col * cell_size, row * cell_size, cell_size, cell_size),
                )
            else:
                # Draw an empty space
                # pygame.draw.rect(screen, WHITE, (col * cell_size, row * cell_size, cell_size, cell_size))
                pass

    # Update the display
    pygame.display.flip()


def wait_for_key():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False


start_screen(screen)
wait_for_key()

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
