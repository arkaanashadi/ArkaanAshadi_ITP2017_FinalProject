import pygame
import os
import random
from pygame.sprite import Sprite


class Salad(Sprite):
    def __init__(self, screen, pic):
        super(Salad, self).__init__()

        # Gets screen information
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Sets the spawn points and it's parameters
        self.spawn_margin = 35
        self.spawn_top = self.screen_rect.top - self.spawn_margin  # -35
        self.spawn_bottom = self.screen_rect.bottom + self.spawn_margin  # 635
        self.spawn_left = self.screen_rect.left - self.spawn_margin  # - 35
        self.spawn_right = self.screen_rect.right + self.spawn_margin  # 835

        # Spawn point ranges
        self.spawnx_edge = [self.spawn_left, self.spawn_right]
        self.spawnx_range = [x for x in range((self.screen_rect.left + self.spawn_margin),
                                              (self.screen_rect.right - self.spawn_margin))]
        self.spawny_edge = [self.spawn_top, self.spawn_bottom]
        self.spawny_range = [x for x in range((self.screen_rect.top + self.spawn_margin),
                                              (self.screen_rect.bottom - self.spawn_margin))]

        # Gets the salad image and it's dimensions
        self.image = pygame.image.load(str(os.path.abspath(pic)))
        self.rect = self.image.get_rect()

        # Sets the initial position of the salad
        self.rect.centerx = random.choice([random.choice(self.spawnx_edge), random.choice(self.spawnx_range)])

        if self.rect.centerx in self.spawnx_edge:
            self.rect.centery = random.choice(self.spawny_range[1:-1])

        else:
            self.rect.centery = random.choice([self.spawn_top] + [self.spawn_bottom])

        # Movement
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    # Moves the salad based on where it was spawned
    def move(self):
        if self.rect.centery == self.spawn_top:
            self.moving_down = True

        elif self.rect.centery == self.spawn_bottom:
            self.moving_up = True

        elif self.rect.centerx == self.spawn_right:
            self.moving_left = True

        elif self.rect.centerx == self.spawn_left:
            self.moving_right = True

    # Updates the salad's current position, based on where they were spawned from
    def update(self):
        if self.moving_up:
            self.rect.centery -= 3

        elif self.moving_down:
            self.rect.centery += 3

        elif self.moving_left:
            self.rect.centerx -= 3

        elif self.moving_right:
            self.rect.centerx += 3

    # Draws the salads to the screen
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    # Removes salads that are out of bounds
    def update_salad(self, salad):
        if ((self.moving_down == True) and (self.rect.top > self.screen_rect.bottom)) or \
            ((self.moving_up == True) and (self.rect.bottom < self.screen_rect.top)) or \
            ((self.moving_left == True) and (self.rect.right < self.screen_rect.left)) or \
            ((self.moving_right == True) and (self.rect.left > self.screen_rect.right)):
            salad.remove(self)
