import pygame
from cell import Cell
from sudoku_generator import generate_sudoku

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.grid = None
        self.selected_cell = None
        self.initial_board = None
        self.initialize_board()

    def initialize_board(self):
        difficulty_map = {'easy': 30, 'medium': 40, 'hard': 50}
        removed_cells = difficulty_map.get(self.difficulty, 30)
        board = generate_sudoku(9, removed_cells)
        self.initial_board = [[cell for cell in row] for row in board]
        self.grid = [[Cell(board[row][col], row, col, self.screen) for col in range(9)] for row in range(9)]

    def draw(self):
        block_size = self.width // 9
        for i in range(10):
            thickness = 3 if i % 3 == 0 else 1
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * block_size), (self.width, i * block_size), thickness)
            pygame.draw.line(self.screen, (0, 0, 0), (i * block_size, 0), (i * block_size, self.height), thickness)
        for row in self.grid:
            for cell in row:
                cell.draw()

    def select(self, row, col):
        if self.selected_cell:
            self.grid[self.selected_cell[0]][self.selected_cell[1]].selected = False
        self.grid[row][col].selected = True
        self.selected_cell = (row, col)

    def click(self, x, y):
        block_size = self.width // 9
        row = y // block_size
        col = x // block_size
        if 0 <= row < 9 and 0 <= col < 9:
            return row, col
        return None

    def clear(self):
        if self.selected_cell:
            row, col = self.selected_cell
            if self.grid[row][col].value == 0:
                self.grid[row][col].sketched_value = 0

    def sketch(self, value):
        if self.selected_cell:
            row, col = self.selected_cell
            self.grid[row][col].sketched_value = value

    def place_number(self, value):
        if self.selected_cell:
            row, col = self.selected_cell
            cell = self.grid[row][col]
            if cell.value == 0:
                cell.set_cell_value(value)

    def reset_to_original(self):
        for row in range(9):
            for col in range(9):
                original_value = self.initial_board[row][col]
                self.grid[row][col].value = original_value
                self.grid[row][col].sketched_value = 0

    def is_full(self):
        return all(cell.value != 0 for row in self.grid for cell in row)

    def check_board(self):
        board = [[cell.value for cell in row] for row in self.grid]
        for i in range(9):
            if not self.valid_group([board[i][j] for j in range(9)]):
                return False
            if not self.valid_group([board[j][i] for j in range(9)]):
                return False
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box = [board[r][c] for r in range(box_row, box_row + 3) for c in range(box_col, box_col + 3)]
                if not self.valid_group(box):
                    return False
        return True

    @staticmethod
    def valid_group(group):
        return sorted(group) == list(range(1, 10))
