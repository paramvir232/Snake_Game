from turtle import Turtle

SNAKE_LENGTH = 3
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# Inherit Turtle Class
class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.segement_list = []
        self.speed(0)
        self.generate_snake(SNAKE_LENGTH)
        self.seg_list = self.segement_list
        self.head = self.seg_list[0]
        # self.head.shape('triangle')
        # self.head.shapesize(stretch_len=1.5)
        self.head.color('red')
        # self.head.turtlesize(outline=1)
        # self.head.pencolor('yellow')

    def restart(self,score):
        """ Reset Snake's position and size with give current score """

        # Deleted added snake segements to reset size
        for snake_index in range(score):
            popped_item = self.segement_list.pop()
            popped_item.hideturtle()

        # Reset position and start snake from (0,0)
        x_pos = 20
        for snake in self.segement_list:
            snake.goto(x_pos, 0)
            snake.setheading(0)
            x_pos -= 20


    def generate_snake(self, SNAKE_LENGTH):
        """Generates snake with given snake length"""
        x_pos = 20
        for snake in range(SNAKE_LENGTH):
            self.add_seg((x_pos, 0))
            x_pos -= 20
        return self.segement_list

    def add_seg(self, position):
        """Adds single snake segment to snake"""
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("White")
        new_segment.turtlesize(outline=2)
        new_segment.pencolor('red')
        new_segment.goto(position)
        self.segement_list.append(new_segment)

    def move(self):
        """Moves snake by move distance"""
        for seg in range(len(self.seg_list) - 1, 0, -1):
            previous_seg = self.seg_list[seg - 1]
            x_cor = previous_seg.xcor()
            y_cor = previous_seg.ycor()
            self.seg_list[seg].goto(x_cor, y_cor)

        self.head.forward(MOVE_DISTANCE)

    def increase_snake_length(self):
        """Increases snake length bt a segment"""
        self.add_seg(self.seg_list[-1].pos())

    def up(self):
        """Change snake direction to Up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        """Change snake direction to Left"""
        if self.head.heading() != RIGHT:
            # print(self.head_pos)
            self.head.setheading(LEFT)

    def down(self):
        """Change snake direction to Down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        """Change snake direction to Right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def get_snake_pos(self):
        return self.head.position()

    def get_snake_list(self):
        return self.seg_list


