from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from block import Block
import time

# The lines of code just below creates the screen for the breakout game
screen = Screen()
screen.tracer(0)
screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.title('BreakOut Game')

# THis line of code creates the paddle for the game
paddle = Paddle((0, -280))

# This line of code creates the scoreboard which will display the player's scores
score = Scoreboard()

# This line of code will create the ball for the game
ball = Ball()

# This line of code will initialize the Block
blocks = Block()

# The lines of code will move player board sideways to the left or to the right
#screen.listen will enable the game to listen to actions by either a mouse or keyboard
screen.listen()
#onkeypress will listen to key presses of the player on the keyboard
screen.onkeypress(paddle.go_left, 'Left')
screen.onkeypress(paddle.go_right, 'Right')


#This line of code will run a for loop to create a number of blocks in the given range. 
for _ in range(0, 108):
    blocks.create_block()

#game is on is a condition which will serve as the condition for our while loop. 
game_is_on = True
while game_is_on:
    #screen.update will continue to refresh the screen for new activities to be displayed accordingly
    screen.update()
    time.sleep(ball.move_speed)

    ball.move()
    ball.increase_speed()

    # code to bounce ball when it hits extremities of x-axis
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    ## code to create ceiling for ball
    if ball.ycor() > 260:
        ball.bounce_y()

    # code to bounce ball when it hits the paddle
    if ball.distance(paddle) < 50 and ball.ycor() > - 280:
        ball.bounce_y()

    # reset ball if it misses paddle
    if ball.ycor() <= -300:
        ball.reset_ball()
        # reduce life by -1 if paddle misses ball
        score.reduce_life()

        # if life is reduced from 3 all the way to zero, game should end
        if score.lives == 0:
            game_is_on = False
            score.game_over()

    # remove block if it is hit by ball
    for brick in blocks.all_blocks:
        if brick.distance(ball) < 50:
            ball.bounce_y()
            brick.clear()
            brick.penup()
            brick.goto(-3000, 3000)
            blocks.all_blocks.remove(brick)
            score.point()

        # end game when there are no bricks
        if len(blocks.all_blocks) == 0:
            game_is_on = False
            score.game_over()

screen.mainloop()
