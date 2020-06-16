import turtle
import winsound

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.title("Ping-Ping Game by Arian Naghibi")

# Score
score_a = 0
score_b = 0
score_board = turtle.Turtle()
score_board.speed(0)
score_board.color("white")
score_board.penup()
score_board.hideturtle()
score_board.setpos(0, 260)
score_board.write(f"Player One: {str(score_a)}     Player Two: {str(score_b)}", align="center",
                  font=("Arial", 16, "bold"))

# Paddle A
paddle_a = turtle.Turtle()
# Turn off animation transition
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("red")
# Pull the pen up – no drawing when object is moving
paddle_a.penup()
paddle_a.setpos(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("blue")
paddle_b.penup()
paddle_b.setpos(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
# Pull the pen up – no drawing when moving
ball.penup()
ball.setpos(0, 0)
ball.dx = 0.4
ball.dy = 0.4


# Functions
def paddle_a_up():
    paddle_a.sety(paddle_a.ycor() + 20)


def paddle_a_down():
    paddle_a.sety(paddle_a.ycor() - 20)


def paddle_b_up():
    paddle_b.sety(paddle_b.ycor() + 20)


def paddle_b_down():
    paddle_b.sety(paddle_b.ycor() - 20)


# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Turn off Automatic update and delay between each update
wn.tracer(0, 0)
while True:
    # Perform a TurtleScreen manual update. To be used when tracer is turned off.
    wn.update()
    # Move the ball
    ball.setpos(ball.xcor() + ball.dx, ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("wall.wav", winsound.SND_ASYNC)
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("wall.wav", winsound.SND_ASYNC)
    elif ball.xcor() > 390:
        score_a += 1
        score_board.clear()
        score_board.write(f"Player One: {str(score_a)}     Player Two: {str(score_b)}", align="center",
                          font=("Arial", 16, "bold"))
        ball.setpos(0, 0)
        ball.dx *= -1
        winsound.PlaySound("point.wav", winsound.SND_ASYNC)
    elif ball.xcor() < -390:
        score_b += 1
        score_board.clear()
        score_board.write(f"Player One: {str(score_a)}     Player Two: {str(score_b)}", align="center",
                          font=("Arial", 16, "bold"))
        ball.setpos(0, 0)
        ball.dx *= -1
        winsound.PlaySound("point.wav", winsound.SND_ASYNC)
    else:
        pass
    # Paddle and ball collision checking
    if 350 > ball.xcor() > 340 and paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50:
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    elif -350 < ball.xcor() < -340 and paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50:
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    else:
        pass
