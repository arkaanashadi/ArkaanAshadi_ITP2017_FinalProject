class General:
    def __init__(self):

        # Variable for amount bomb spawn and fruit spawn for each "level"
        self.level = 0

        # Max amount of fruits
        self.max_fruit = 10

        # Max amount of bombs
        self.max_bomb = 3

        # Player lives
        self.lives = 5

        # Scores
        self.score = 0
        self.highscore = 0

        # Scoring parameters
        self.base_score = 100

    # Adds score when player collides with a fruit
    def ate_fruit(self):
        self.score += self.base_score * (self.level + 1)

    # Subtracts lives when player collides with a bomb
    def ate_bomb(self):
        self.lives -= 1

    # Updates the highscore when the current score exceeds the previous high score
    def update_highscore(self):
        if self.score >= self.highscore:
            self.highscore = self.score

    # Updates the level based on score acquired
    def levelup(self):
        if self.score > 2500:
            self.level = 1

        if self.score > 10000:
            self.level = 3

        if self.score > 30000:
            self.level = 5

        if self.score > 100000:
            self.level = 7

        if self.score > 250000:
            self.level = 9
