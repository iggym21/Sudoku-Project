import pygame
from board import Board
from button import Button

def menu(screen):
    buttons = [
        Button("EASY", 170, 250, 200, 50, (0, 255, 0), (144, 238, 144), "easy"),
        Button("MEDIUM", 170, 320, 200, 50, (255, 255, 0), (255, 255, 153), "medium"),
        Button("HARD", 170, 390, 200, 50, (255, 165, 0), (255, 200, 100), "hard"),
        Button("EXIT", 170, 460, 200, 50, (255, 0, 0), (255, 100, 100), "exit")
    ]
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill((255, 255, 255))
        font = pygame.font.Font(None, 50)
        title_surface = font.render("Welcome to Sudoku", True, (0, 0, 0))
        title_rect = title_surface.get_rect(center=(270, 100))
        screen.blit(title_surface, title_rect)
        subtitle_surface = font.render("Select Game Mode:", True, (0, 0, 0))
        subtitle_rect = subtitle_surface.get_rect(center=(270, 200))
        screen.blit(subtitle_surface, subtitle_rect)
        for button in buttons:
            action = button.draw(screen)
            if action == "exit":
                pygame.quit()
                quit()
            elif action in ["easy", "medium", "hard"]:
                return action
        pygame.display.update()

def game_over_screen(screen, success):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill((255, 255, 255))
        if success:
            message = "Game Won!"
            color = (0, 255, 0)
        else:
            message = "Game Over!"
            color = (255, 0, 0)
        font = pygame.font.Font(None, 36)
        text_surface = font.render(message, True, color)
        text_rect = text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(text_surface, text_rect)
        ok_button = Button("OK", 190, 400, 150, 50, (0, 0, 255), (100, 100, 255), "ok")
        action = ok_button.draw(screen)
        if action == "ok":
            return
        pygame.display.update()

def game_screen(screen, difficulty):
    board = Board(540, 540, screen, difficulty)
    buttons = [
        Button("RESET", 20, 550, 150, 40, (100, 149, 237), (135, 206, 250), "reset"),
        Button("RESTART", 190, 550, 150, 40, (100, 149, 237), (135, 206, 250), "restart"),
        Button("EXIT", 360, 550, 150, 40, (255, 0, 0), (255, 100, 100), "exit")
    ]
    running = True
    selected_value = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked_cell = board.click(pos[0], pos[1])
                if clicked_cell:
                    board.select(*clicked_cell)
                for button in buttons:
                    action = button.draw(screen)
                    if action == "reset":
                        board.reset_to_original()
                    elif action == "restart":
                        return True
                    elif action == "exit":
                        pygame.quit()
                        quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    selected_value = 1
                elif event.key == pygame.K_2:
                    selected_value = 2
                elif event.key == pygame.K_3:
                    selected_value = 3
                elif event.key == pygame.K_4:
                    selected_value = 4
                elif event.key == pygame.K_5:
                    selected_value = 5
                elif event.key == pygame.K_6:
                    selected_value = 6
                elif event.key == pygame.K_7:
                    selected_value = 7
                elif event.key == pygame.K_8:
                    selected_value = 8
                elif event.key == pygame.K_9:
                    selected_value = 9
                elif event.key == pygame.K_RETURN and selected_value:
                    board.place_number(selected_value)
                    selected_value = None
        if board.is_full():
            if board.check_board():
                game_over_screen(screen, success=True)
            else:
                game_over_screen(screen, success=False)
            return False
        screen.fill((255, 255, 255))
        board.draw()
        for button in buttons:
            button.draw(screen)
        pygame.display.update()

def main():
    pygame.init()
    screen = pygame.display.set_mode((540, 600))
    pygame.display.set_caption("Sudoku")
    while True:
        difficulty = menu(screen)
        restart_game = game_screen(screen, difficulty)
        if not restart_game:
            break
    pygame.quit()

if __name__ == "__main__":
    main()
