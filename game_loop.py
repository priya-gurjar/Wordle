import pygame
import random
import math
from sys import exit
from sprite import BorderedBox, get_boxes
from settings import TILE_HEIGHT, TILE_WIDTH, TILE_MARGIN, NUMBER_OF_ROWS, NUMBER_OF_COLUMNS, GAP
import wordle
import words

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
clock = pygame.time.Clock()

# Set the width and height of the screen [width, height]
size = (800, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Wordle")
box = pygame.sprite.Group()
random = random.randint(0, 12970)
solution_word = words.WORDS[random]
game_logic = wordle.GameLogic(solution_word)
all_boxes = get_boxes(screen.get_height(), screen.get_width(), TILE_HEIGHT, TILE_WIDTH, TILE_MARGIN, NUMBER_OF_ROWS,
                      NUMBER_OF_COLUMNS, GAP, game_logic)
for item in all_boxes:
    box.add(item)

# Loop until the user clicks the close button.
done = False
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if game_logic.is_game_over:
                done = True
                pygame.quit()
                exit()

            key_name = pygame.key.name(event.key)
            if key_name.isalpha() and len(key_name) == 1:
                print(pygame.key.name(event.key))
                game_logic.add_next_letter_to_current_guess_list(key_name)
                box.empty()
                all_boxes = get_boxes(screen.get_height(), screen.get_width(), TILE_HEIGHT, TILE_WIDTH, TILE_MARGIN,
                                      NUMBER_OF_ROWS,
                                      NUMBER_OF_COLUMNS, GAP, game_logic)
                for item in all_boxes:
                    box.add(item)

    # --- Drawing code should go here
    screen.fill(WHITE)
    if game_logic.is_game_over:
        if game_logic.is_game_won:
            font = pygame.font.SysFont('Comic Sans MS', 50)
            text = font.render('You Won', True, pygame.Color('black'))
            text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
            screen.blit(text, text_rect)
        elif game_logic.is_game_lost:
            font = pygame.font.SysFont('Comic Sans MS', 50)
            text = font.render('You Lost', True, pygame.Color('black'))
            text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
            screen.blit(text, text_rect)
    else:
        box.draw(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    pygame.display.update()
    box.update()
    clock.tick(60)
