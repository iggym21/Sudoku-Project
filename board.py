import pygame
from constants import *

class Board:
    def __init__(self, width, height, window, difficulty):
        """Constructor for the Board class.
        window is a window from PyGame.
        difficulty is a variable to indicate if the user chose easy, medium, or hard."""
        self.width = width
        self.height = height
        self.window = window
        self.difficulty = difficulty

    def draw_grid(self):
        """Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
        Draws every cell on this board."""

        # Draw horizontal lines
        for i in range(1, BOARD_ROWS):
            pygame.draw.line(
                self.window,
                BLACK,
                (0, i * CELL_SIZE),
                (WINDOW_WIDTH, i * CELL_SIZE),
                THICK_LINE_WIDTH if i % 3 == 0 else THIN_LINE_WIDTH
            )

        # Draw vertical lines
        for i in range(1, BOARD_COLS):
            pygame.draw.line(
                self.window,
                BLACK,
                (i * CELL_SIZE, 0),
                (i * CELL_SIZE, WINDOW_HEIGHT // 10 * 9),
                THICK_LINE_WIDTH if i % 3 == 0 else THIN_LINE_WIDTH
            )

    def select_cell(self, row, col):
        """Marks the cell at (row, col) in the board as the current selected cell.
        Once a cell has been selected, the user can edit its value or sketched value."""

        pass
