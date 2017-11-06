import pygame
import os


class Player:
    def __init__(self, screen):

        # Gets screen information
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Sets the player image initial orientation
        self.orientation = 0

        # Gets the player images and it's dimensions
        self.image = [pygame.image.load(str(os.path.abspath("Images/PlayerU.png"))),
                      pygame.image.load(str(os.path.abspath("Images/PlayerD.png"))),
                      pygame.image.load(str(os.path.abspath("Images/PlayerL.png"))),
                      pygame.image.load(str(os.path.abspath("Images/PlayerR.png")))]
        self.rect = self.image[self.orientation].get_rect()

        # Sets the player initial position
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # Player movement status
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    # Draws the player image on the screen
    def blitme(self):
        self.screen.blit(self.image[self.orientation], self.rect)

    # Updates the orientation of the player image and updates the player image's position
    def movement(self):
        if self.moving_up and self.rect.top > 0:
            self.rect.centery -= 3
            self.orientation = 0

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 3
            self.orientation = 1

        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 3
            self.orientation = 2

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 3
            self.orientation = 3
