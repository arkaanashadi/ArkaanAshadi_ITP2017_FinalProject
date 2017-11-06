import pygame.font


class RetryButton:
    def __init__(self, screen):
        # Gets screen information
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Button parameters
        self.width, self.height = 200, 50
        self.button_color = (10, 10, 10)

        # Font parameters
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Sets the dimensions of the button, and the initial position of the button
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Renders the text inside the button and sets the text on the middle of the button
        self.text = self.font.render("Retry?", True, self.text_color, self.button_color)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.rect.center

    # Builds the button
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.text, self.text_rect)
