import pygame
import pygame.font


# Displays a text at the specified positions
class Show:
    def __init__(self, generals, screen, given_text, font_size):
        # Initializes pygame.font
        pygame.font.init()

        # Gets screen information and generals
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.generals = generals

        # Sets the font and the specified text
        self.font = pygame.font.SysFont(None, font_size)
        self.given_text = given_text


    # Draws the text, taking in various parameters
    def blitme(self, location, x_offset=0, y_offset=0, pre_additional_text="", post_additional_text=""):

        # Renders the text and gets it's dimensions
        self.text = self.font.render(str(pre_additional_text) +
                                     str(self.given_text) +
                                     str(post_additional_text), False, (0, 0, 0))
        self.rect = self.text.get_rect()

        # Checks which location should the text be placed on, takes in the offset parameter if provided
        if location == "top_center":
            self.rect.centerx = self.screen_rect.centerx + x_offset
            self.rect.y = 0 + y_offset

        elif location == "top_left":
            self.rect.x = 0 + x_offset
            self.rect.y = 0 + y_offset

        elif location == "center":
            self.rect.centerx = self.screen_rect.centerx + x_offset
            self.rect.centery = self.screen_rect.centery + y_offset

        elif location == "top_right":
            self.rect.right = self.screen_rect.right + x_offset
            self.rect.y = 0 + y_offset

        # Draws the text
        self.screen.blit(self.text, self.rect)

