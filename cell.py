import pygame
from constants import *

class Cell:
    def __init__(self, window, x, y, width, height, cell_font, cell_color, text, text_color, value):
        self.window = window

        # Adjusted dimensions for centered cell rectangle
        rect_width, rect_height = width - 10, height - 10
        rect_x = x + (width - rect_width) // 2
        rect_y = y + (height - rect_height) // 2

        # Cell
        self.cell_rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)
        self.cell_font = cell_font
        self.cell_color = cell_color

        # Cell text
        self.text = text
        self.text_color = text_color if value != 0 else ORANGE #Orange if cell is initially blank
        self.text_surface = self.cell_font.render(self.text, 0, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=self.cell_rect.center)

        #Value
        self.value = value
        self.sketched_value = 0
        #Press state
        self.pressed = False

    def draw_cell(self):
        """Draws this cell, along with the value inside it.
        If this cell has a nonzero value, that value is displayed.
        Otherwise, no value is displayed in the cell.
        The cell is outlined red if it is currently selected."""

        # Draw the cell
        pygame.draw.rect(self.window, RED if self.pressed is True else self.cell_color, self.cell_rect)
        self.text = str(self.value) if self.value != 0 else str(self.sketched_value) if self.sketched_value!=0 else ""
        self.text_surface = self.cell_font.render(self.text, 0, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=self.cell_rect.center)
        # Draw the cell text
        self.window.blit(self.text_surface, self.text_rect)


    def is_pressed(self, position):
        return self.cell_rect.collidepoint(position)


    def set_cell_value(self, value):
        """Setter for this cell’s value"""
        self.value = value


    def set_sketched_value(self, value):
        """Setter for this cell’s sketched value"""
        self.sketched_value = value
