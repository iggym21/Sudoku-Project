import pygame, sys
from constants import *
from button import Button
from board import Board
from cell import Cell
import sudoku_generator
cells = {}  #Global dictionary to store cells
def game_start_screen():
    # Background
    window.fill(WHITE)
    # Title
    title_text = "Welcome to Sudoku"
    title_font = pygame.font.Font(None, TITLE_FONT)
    title_surface = title_font.render(title_text, 0, BLACK)
    title_rect = title_surface.get_rect(
        center=(
            WINDOW_WIDTH // 2,
            WINDOW_HEIGHT // 4
        )
    )
    window.blit(title_surface, title_rect)
    # Select Game Mode
    select_game_mode_text = "Select Game Mode:"
    select_game_mode_font = pygame.font.Font(None, SELECT_GAME_MODE_FONT)
    select_game_mode_surface = select_game_mode_font.render(select_game_mode_text, 0, BLACK)
    select_game_mode_rect = select_game_mode_surface.get_rect(
        center=(
            WINDOW_WIDTH // 2,
            WINDOW_HEIGHT // 2
        )
    )
    window.blit(select_game_mode_surface, select_game_mode_rect)
    # Game mode buttons
    ## Easy mode button
    easy_mode_button = Button(
        window=window,
        x=0,
        y=GAME_MODE_BUTTON_Y_AXIS,
        width=GAME_MODE_BUTTON_WIDTH,
        height=GAME_MODE_BUTTON_HEIGHT,
        button_font=GAME_MODE_BUTTON_FONT,
        button_color=YELLOW,
        text="Easy",
        text_color=WHITE,
    )
    easy_mode_button.draw()
    ## Medium mode button
    medium_mode_button = Button(
        window=window,
        x=300,
        y=GAME_MODE_BUTTON_Y_AXIS,
        width=GAME_MODE_BUTTON_WIDTH,
        height=GAME_MODE_BUTTON_HEIGHT,
        button_font=GAME_MODE_BUTTON_FONT,
        button_color=ORANGE,
        text="Medium",
        text_color=WHITE,
    )
    medium_mode_button.draw()
    ## Hard mode button
    hard_mode_button = Button(
        window=window,
        x=600,
        y=GAME_MODE_BUTTON_Y_AXIS,
        width=GAME_MODE_BUTTON_WIDTH,
        height=GAME_MODE_BUTTON_HEIGHT,
        button_font=GAME_MODE_BUTTON_FONT,
        button_color=RED,
        text="Hard",
        text_color=WHITE,
    )
    hard_mode_button.draw()
    return easy_mode_button, medium_mode_button, hard_mode_button
def game_in_progress_screen(difficulty):
    # Background
    window.fill(WHITE)
    board = Board(
        width=WINDOW_WIDTH,
        height=WINDOW_HEIGHT,
        window=window,
        difficulty=difficulty
    )
    board.draw_grid()
    #Creates a board using sudoku_generator
    removed_cells = 30 if difficulty == "Easy" else 40 if difficulty == "Medium" else 50
    sudoku_board = sudoku_generator.generate_sudoku(9, removed_cells) #Creates a board with the number of corresponding removed cells
    for row in range(9):
        for col in range(9):
            cell = Cell(
                window=window,
                x=col * CELL_SIZE,
                y=row * CELL_SIZE,
                width=CELL_SIZE,
                height=CELL_SIZE,
                cell_font=CELL_FONT,
                cell_color=WHITE,
                text=f"{row}, {col}",
                text_color=BLACK,
                value = sudoku_board[row][col]
            )
            cell.draw_cell()
            cells[(row, col)] = cell
    # Create in-game buttons
    ## Reset button
    reset_button = Button(
        window=window,
        x=0,
        y=GAME_IN_PROGRESS_BUTTON_Y_AXIS + 3,
        width=GAME_IN_PROGRESS_BUTTON_WIDTH,
        height=GAME_IN_PROGRESS_BUTTON_HEIGHT,
        button_font=GAME_IN_PROGRESS_BUTTON_FONT,
        button_color=YELLOW,
        text="Reset",
        text_color=WHITE,
    )
    reset_button.draw()
    ## Restart button
    restart_button = Button(
        window=window,
        x=300,
        y=GAME_IN_PROGRESS_BUTTON_Y_AXIS + 3,
        width=GAME_IN_PROGRESS_BUTTON_WIDTH,
        height=GAME_IN_PROGRESS_BUTTON_HEIGHT,
        button_font=GAME_IN_PROGRESS_BUTTON_FONT,
        button_color=ORANGE,
        text="Restart",
        text_color=WHITE,
    )
    restart_button.draw()
    ## Exit button
    exit_button = Button(
        window=window,
        x=600,
        y=GAME_IN_PROGRESS_BUTTON_Y_AXIS + 3,
        width=GAME_IN_PROGRESS_BUTTON_WIDTH,
        height=GAME_IN_PROGRESS_BUTTON_HEIGHT,
        button_font=GAME_IN_PROGRESS_BUTTON_FONT,
        button_color=RED,
        text="Exit",
        text_color=WHITE,
    )
    exit_button.draw()
    return reset_button, restart_button, exit_button
def check_board():
    """Checks if board is full
    If board is full, then checks if the game was won or lost"""
    count = 0
    for row in range(9):
        for col in range(9):
            curr_cell = cells[(row, col)]
            count+= 1 if curr_cell.value !=0 or curr_cell.sketched_value != 0 else 0
    if count==81: #Checks if the 9x9 board only contains filled cells
        #Determine if the game is won or lost
        temp = []
        desired_list = [1,2,3,4,5,6,7,8,9]
        #Check rows
        for row in range(9):
            temp = [max(cells[(row, col)].value, cells[(row,col)].sketched_value) for col in range(9)]
        if sorted(temp)!=desired_list:
            print("row")
            game_over_screen()
            return
        #Check columns
        for col in range(9):
            temp = [max(cells[(row, col)].value, cells[(row,col)].sketched_value) for row in range(9)]
        if sorted(temp)!=desired_list:
            game_over_screen()
            print("col")
            return
        temp = []
        #Check boxes
        for i in range(3):
            for j in range(3):
                temp = []
                curr_row = i*3; curr_col = j*3
                for row in range(curr_row, curr_row+3):
                    for col in range(curr_col, curr_col+3):
                        temp.append(max(cells[(row, col)].value, cells[(row,col)].sketched_value))
                if sorted(temp)!=desired_list:
                    game_over_screen()
                    print("boxes")
                    return
        game_won_screen()
def game_over_screen():
    #background
    window.fill(WHITE)
    #font
    font = pygame.font.Font(None, TITLE_FONT)
    text_surface = font.render("Game Over :(", True, BLACK)
    text_rect = text_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
    window.blit(text_surface, text_rect)

    #game over restart button
    restart_button = Button(
        window=window,
        x=(WINDOW_WIDTH - GAME_IN_PROGRESS_BUTTON_WIDTH) // 2,
        y=GAME_IN_PROGRESS_BUTTON_Y_AXIS // 2 + 150,
        width=GAME_IN_PROGRESS_BUTTON_WIDTH,
        height=GAME_IN_PROGRESS_BUTTON_HEIGHT,
        button_font=GAME_IN_PROGRESS_BUTTON_FONT,
        button_color=ORANGE,
        text="Restart",
        text_color=WHITE,
    )
    restart_button.draw()

    pygame.display.update()

    # Wait for user to interact
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.is_pressed(event.pos):
                    main()  # Restart the game
                    return


def game_won_screen():
    #background
    window.fill(WHITE)
    #font
    font = pygame.font.Font(None, TITLE_FONT)
    text_surface = font.render("Game Won!", True, BLACK)
    text_rect = text_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
    window.blit(text_surface, text_rect)

    # game won Exit Button
    exit_button = Button(
        window=window,
        x=(WINDOW_WIDTH - GAME_IN_PROGRESS_BUTTON_WIDTH) // 2,
        y=GAME_IN_PROGRESS_BUTTON_Y_AXIS // 2 + 150,
        width=GAME_IN_PROGRESS_BUTTON_WIDTH,
        height=GAME_IN_PROGRESS_BUTTON_HEIGHT,
        button_font=GAME_IN_PROGRESS_BUTTON_FONT,
        button_color=ORANGE,
        text="Exit",
        text_color=WHITE,
    )
    exit_button.draw()

    pygame.display.update()

    # Wait for user to interact
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.is_pressed(event.pos):
                    pygame.quit()
                    sys.exit()

def main():
    easy_mode_button, medium_mode_button, hard_mode_button = game_start_screen()
    game_in_progress = False
    game_mode = None
    while not game_in_progress:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if close button in pressed
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: # if mouse is clicked
                x, y = event.pos # mouse click coordinates
                if easy_mode_button.is_pressed(event.pos): # if easy mode button is pressed
                    game_mode = 'Easy'
                    game_in_progress = True
                elif medium_mode_button.is_pressed(event.pos): # if medium mode button is pressed
                    game_mode = 'Medium'
                    game_in_progress = True
                elif hard_mode_button.is_pressed(event.pos): # if hard mode button is pressed
                    game_mode = 'Hard'
                    game_in_progress = True
                #print(f"{game_mode} mode selected")
                continue
        pygame.display.update()
    reset_button, restart_button, exit_button = game_in_progress_screen(game_mode) # go to game in progress screen
    pygame.display.update()
    pressed_button = None
    pressed_row = None; pressed_col = None
    while game_in_progress: # if game is in progress
        for in_game_event in pygame.event.get():
            if in_game_event.type == pygame.QUIT:  # if close button in pressed
                pygame.quit()
                sys.exit()
            if in_game_event.type == pygame.MOUSEBUTTONDOWN: # if mouse is clicked
                x, y = in_game_event.pos # mouse click coordinates
                if reset_button.is_pressed(in_game_event.pos): # if reset button is pressed
                    pressed_button = 'Reset'
                    for row in range(9):
                        for col in range(9):
                            cells[(row,col)].sketched_value = 0
                    game_in_progress = True
                elif restart_button.is_pressed(in_game_event.pos): # if restart button is pressed
                    main()
                elif exit_button.is_pressed(in_game_event.pos): # if exit button is pressed
                    pressed_button = 'Exit'
                    game_in_progress = False
                #print(f"{pressed_button} pressed")
            if in_game_event.type == pygame.MOUSEBUTTONDOWN and pressed_row == None and in_game_event.pos[1]<900:  # if mouse is clicked
                x, y = in_game_event.pos  # mouse click coordinates
                pressed_row = y // CELL_SIZE
                pressed_col = x // CELL_SIZE
                if cells[(pressed_row, pressed_col)].value ==0: #Only allow changes if the cell doesn't have a default value
                    #print(f'row: {pressed_row}, col: {pressed_col}')
                    cells[(pressed_row, pressed_col)].pressed = True
                else:
                    pressed_row, pressed_col = None, None
            if in_game_event.type == pygame.KEYDOWN and pressed_row != None: #If something is clicked and a cell IS selected
                if pygame.K_0 <= in_game_event.key <= pygame.K_9: # if the pressed key is a number key
                    key = in_game_event.key - pygame.K_0  # Subtract the pygame constant for '0' to get the numeric value
                    #print(key)
                    cells[(pressed_row, pressed_col)].pressed = False #Stop drawing as red
                    cells[(pressed_row, pressed_col)].set_sketched_value(key)
                    pressed_row = None; pressed_col = None
        for row in range(9):
            for col in range(9):
                cells[(row,col)].draw_cell()
        check_board()
        pygame.display.update()
if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # size of the game window
    pygame.display.set_caption('Sudoku') # title of the game window
    GAME_MODE_BUTTON_FONT = pygame.font.Font(None, GAME_MODE_BUTTON_HEIGHT // 3)
    CELL_FONT = pygame.font.Font(None, CELL_SIZE // 3)
    GAME_IN_PROGRESS_BUTTON_FONT = pygame.font.Font(None, GAME_IN_PROGRESS_BUTTON_HEIGHT // 3)
    easy_mode_button, medium_mode_button, hard_mode_button = game_start_screen()
    game_in_progress = False
    game_mode = None
    main()