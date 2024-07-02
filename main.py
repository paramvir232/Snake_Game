from turtle import Turtle, Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

#Creating Class instances
food = Food()
screen = Screen()
turtle = Turtle()
snake = Snake()
scoreboard = Scoreboard()

# #Key Controls
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")
screen.onkeypress(snake.down, "Down")


def screen_settings():
    """Implements all screen settings for snake games"""
    screen.tracer(0)
    screen.title("My Snake Game")
    screen.bgcolor("black")
    screen.setup(width=600, height=600)
    screen.listen()


def wall_collision_check():
    """Returns True if snake collided with wall else return False"""
    for corrdinates in snake.get_snake_pos():
        if corrdinates <= -300 or corrdinates >= 300:
            return True
    return False


def body_collision_check():
    """Returns True if snake collided with itself else return False"""
    head = snake.head
    for snake_elment in snake.get_snake_list()[1:]:
        if head.distance(snake_elment) < 10:
            return True
    return False


def snake_game():
    """Main Game Functions Returns None"""
    speed = 0.3
    game_is_on = True
    screen_settings()
    while game_is_on:
        snake.move()

        #Detect collision with Food
        if snake.head.distance(food) < 15:
            if scoreboard.score < 10:
                speed -= 0.01
            else:
                speed -= 0.005
            scoreboard.increase_score()
            food.refresh()
            snake.increase_snake_length()

        # Detect collision with Wall and Body
        game_is_on = not wall_collision_check() and not body_collision_check()

        # Restart Mechanisms
        if not game_is_on:
            scoreboard.game_over()

            # Restart
            if screen.textinput(title="GAME OVER", prompt="You want to retry the game. Type y/n ") == 'y':
                game_is_on = True
                food.refresh()
                snake.restart(scoreboard.score)
                scoreboard.score = 0
                scoreboard.update_scoreboard()
                snake_game()

            # Exit
            else:
                time.sleep(2)
                screen.bye()

        screen.update()
        time.sleep(speed)


snake_game()

screen.exitonclick()
