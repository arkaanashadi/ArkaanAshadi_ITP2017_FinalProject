import sys
import pygame
from Final.Functions import Functions as Func


# Check event types
def events(retry, generals, player):
    pygame.init()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            keydown(event, player)

        elif event.type == pygame.KEYUP:
            keyup(event, player)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            Func.reset(mouse_x, mouse_y, retry, generals)


# Checks which key is being pressed down, and execute command accordingly
def keydown(event, player):
    if event.key == pygame.K_s:
        player.moving_down = True

    if event.key == pygame.K_w:
        player.moving_up = True

    if event.key == pygame.K_d:
        player.moving_right = True

    if event.key == pygame.K_a:
        player.moving_left = True

    if event.key == pygame.K_q:
        sys.exit()


# Checks which key is no longer being pressed down, and execute command accordingly
def keyup(event, player):
    if event.key == pygame.K_s:
        player.moving_down = False

    if event.key == pygame.K_w:
        player.moving_up = False

    if event.key == pygame.K_d:
        player.moving_right = False

    if event.key == pygame.K_a:
        player.moving_left = False
