from turtle import Turtle

FONT = ('Courier New', 20, 'bold')
ALIGN = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()


    def update_scoreboard(self):
        """Update/Refresh Scoreboard text"""
        self.clear()
        self.goto(0, 270)
        self.write(f"Score = {self.score}", align=ALIGN, font=FONT)
        # self.clear()

    def game_over(self):
        """Prints game over in center"""
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGN, font=FONT)


    def increase_score(self):
        """Increase score by 1 and updates score text"""
        self.clear()
        self.score += 1
        self.goto(0, 270)
        self.write(f"Score = {self.score}", align=ALIGN, font=FONT)

    def get_scores(self):
        return self.score
