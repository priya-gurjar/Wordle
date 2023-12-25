import pygame


class BorderedBox(pygame.sprite.Sprite):
    def __init__(self, color, width, height,
                 border_width=5, border_color=pygame.Color('black'),
                 top=0, left=0, letter='', font_size=50):
        super().__init__()
        self.image = pygame.Surface([width + 2 * border_width, height + 2 * border_width])
        pygame.draw.rect(self.image, border_color, (0, 0, width + 2 * border_width, height + 2 * border_width),
                         border_width)
        pygame.draw.rect(self.image, color, (border_width, border_width, width, height))
        if letter:
            font = pygame.font.SysFont('Comic Sans MS', font_size)
            text = font.render(letter, True, pygame.Color('black'))
            text_rect = text.get_rect(center=(width / 2 + border_width, height / 2 + border_width))
            self.image.blit(text, text_rect)
        self.rect = self.image.get_rect(top=top, left=left)

    def update(self):
        pass


def get_boxes(screen_height, screen_width,
              tile_height, tile_width, tile_margin,
              number_of_rows, number_of_columns,
              tile_gap=0, game_logic_state=None):
    margin_left = (screen_width - (tile_width * number_of_columns + tile_margin * (number_of_columns - 1) + tile_gap * (
            number_of_columns - 1))) / 2
    margin_top = (screen_height - (tile_height * number_of_rows + tile_margin * (number_of_rows - 1) + tile_gap * (
            number_of_rows - 1))) / 2
    boxes = []
    if game_logic_state:
        game_logic_state_list = game_logic_state.get_guess_list().copy()
        game_logic_state_list.append(game_logic_state.get_current_guess_list())
    for row in range(number_of_rows):
        for column in range(number_of_columns):
            if game_logic_state and row < len(game_logic_state_list) and \
                    column < len(game_logic_state_list[row]):
                color = pygame.Color('gray')
                if game_logic_state_list[row][column][1]:
                    color = pygame.Color('yellow')
                if game_logic_state_list[row][column][2]:
                    color = pygame.Color('green')
                boxes.append(BorderedBox(color, tile_width, tile_height, 5, pygame.Color('black'),
                                         margin_top + (tile_height + tile_margin + tile_gap) * row,
                                         margin_left + (tile_width + tile_margin + tile_gap) * column,
                                         game_logic_state_list[row][column][0]))
            else:
                boxes.append(BorderedBox(pygame.Color('gray'), tile_width, tile_height, 5, pygame.Color('black'),
                                         margin_top + (tile_height + tile_margin + tile_gap) * row,
                                         margin_left + (tile_width + tile_margin + tile_gap) * column))
    return boxes
