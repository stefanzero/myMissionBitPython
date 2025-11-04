import pygame
import random
import sys


def start_screen(screen):
    # Constants
    WIDTH, HEIGHT = 800, 600
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    FONT_SIZE = 30

    # Font for displaying the text
    font = pygame.font.Font(None, FONT_SIZE)

    # Fill the screen with the background color
    screen.fill(BLACK)

    # Introduction text
    intro_text = [
        "Welcome, Alien Abductor!",
        "You're behind on your weekly quota of abductions.",
        "Help the alien catch up by abducting targets on Earth!",
        "",
        "----------------------------------------------------------------------------------------------",
        "Move the UFO with ARROWS and",
        "press SPACE to abduct cows with the track bean.",
        "----------------------------------------------------------------------------------------------",
        "",
        "Press any key to start the game...",
        "",
    ]

    # Render and display the introduction text
    y_position = HEIGHT // 4
    for line in intro_text:
        text = font.render(line, True, WHITE)
        text_rect = text.get_rect(center=(WIDTH // 2, y_position))
        screen.blit(text, text_rect)
        y_position += FONT_SIZE

    pygame.display.flip()

    # Wait for a key press to start the game
    wait_for_key()


def wait_for_key():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False
