import pygame
from Final.Classes.Salad import Salad


def update(generals, screen, player, fruits, bombs, score, highscore, highscore_text, lives):

    # fills the screen with color
    screen.fill((100, 100, 100))

    # Displays stats
    score.blitme("top_center")
    highscore_text.blitme("top_right")
    highscore.blitme("top_right", 0, 20)
    lives.blitme("top_left")

    # Updates the fruit sprite group
    for fruit in fruits.sprites():
        fruit.blitme()
        fruit.move()
        fruit.update()
        fruit.blitme()
        fruit.update_salad(fruits)
    spawn_fruits(generals, screen, fruits)

    # Updates the bomb sprite group
    for bomb in bombs.sprites():
        bomb.blitme()
        bomb.move()
        bomb.update()
        bomb.blitme()
        bomb.update_salad(bombs)
    spawn_bombs(generals, screen, bombs)

    # Updates player position
    player.movement()
    player.blitme()
    eat(generals, player, fruits, bombs)

    # Updates the contents on the screen
    pygame.display.flip()


# Spawns the fruits according to the max amount allowed
def spawn_fruits(generals, screen, fruits):
    if len(fruits) < generals.max_fruit - generals.level:
        fruits.add(Salad(screen, "Images/Fruit.png"))


# Spawns the bombs according to the max amount allowed
def spawn_bombs(generals, screen, bombs):
    if len(bombs) < generals.max_bomb + generals.level:
        bombs.add(Salad(screen, "Images/Bomb.png"))


# Checks collision between the player and either the bomb group or the fruit group
def eat(generals, player, fruits, bombs):

    # If the player collides with the fruit group, the score will be added
    if pygame.sprite.spritecollide(player, fruits, True):
        generals.ate_fruit()
        
    # If the player collides with the bomb group, the player's lives will be subtracted
    if pygame.sprite.spritecollide(player, bombs, True):
        generals.ate_bomb()


# Game over screen
def gameover(screen, score, highscore, retry):

    # Fills the screen
    screen.fill((100, 100, 100))

    # Displays score and high score
    highscore.blitme("top_center", 0, 0, "High Score ")
    score.blitme("center", 0, -50, "Your Score ")

    # Draws the retry button
    retry.draw_button()

    # Updates the screen
    pygame.display.flip()


# Resets the game when the retry button is pressed
def reset(mouse_x, mouse_y, retry, generals):
    # Checks if the mouse is in side or hovering over the retry button
    if retry.rect.collidepoint(mouse_x, mouse_y):
        generals.lives = 5
        generals.score = 0
        generals.level = 0
