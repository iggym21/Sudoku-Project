import pygame

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.sketched_value = 0
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        font = pygame.font.Font(None, 40)
        cell_size = 60
        x = self.col * cell_size
        y = self.row * cell_size
        rect_color = (200, 200, 200) if self.selected else (255, 255, 255)
        pygame.draw.rect(self.screen, rect_color, (x, y, cell_size, cell_size))
        pygame.draw.rect(self.screen, (0, 0, 0), (x, y, cell_size, cell_size), 2)
        if self.value != 0:
            text = font.render(str(self.value), True, (0, 0, 0))
            self.screen.blit(text, (x + 20, y + 10))
        elif self.sketched_value != 0:
            text = font.render(str(self.sketched_value), True, (128, 128, 128))
            self.screen.blit(text, (x + 5, y + 5))
