import pygame
from Final.Functions import Functions as Func, Events as Event
from Final.Classes import Player, General
from Final.Classes.Display import Show
from Final.Classes.RetryButton import RetryButton
from pygame.sprite import Group


# The main program
def run():
    # Initializes pygame
    pygame.init()

    # The classes and groups used in the program
    generals = General.General()
    screen = pygame.display.set_mode((800, 600))
    player = Player.Player(screen)
    fruits = Group()
    bombs = Group()

    while True:
        # Buttons and text in the program
        score = Show(generals, screen, generals.score, 30)
        highscore = Show(generals, screen, generals.highscore, 30)
        highscore_text = Show(generals, screen, "High Score", 30)
        lives = Show(generals, screen, generals.lives, 50)
        retry = RetryButton(screen)

        # Check events every iteration
        Event.events(retry, generals, player)

        # Updates made in the general class
        generals.update_highscore()
        generals.levelup()

        # Checks if the amount of lives are above 0, if so the program will keep running
        if generals.lives > 0:
            Func.update(generals, screen, player, fruits, bombs, score, highscore, highscore_text, lives)
        elif generals.lives <= 0:
            Func.gameover(screen, score, highscore, retry)


run()
