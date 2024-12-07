import pygame

class Button:
    def __init__(self, window, x, y, width, height, button_font, button_color, text, text_color):
        self.window = window

        # Button
        self.button_rect = pygame.Rect(x, y, width, height)
        self.button_font = button_font
        self.button_color = button_color

        # Button text
        self.text = text
        self.text_color = text_color
        self.text_surface = self.button_font.render(self.text, 0, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=self.button_rect.center)

    def draw(self):
        # Draw the button
        pygame.draw.rect(self.window, self.button_color, self.button_rect)

        # Draw the button text
        self.window.blit(self.text_surface, self.text_rect)

    def is_pressed(self, position):
        return self.button_rect.collidepoint(position)