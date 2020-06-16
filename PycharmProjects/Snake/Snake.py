import turtle
import time
import random
import winsound

wn = turtle.Screen()
wn.title("Snake Game by Arian Naghibi")
wn.bgpic("grass.gif")
wn.setup(width=600, height=600)


# Food
food = turtle.Turtle()
food.speed(0)
wn.register_shape("apple.gif")
food.shape("apple.gif")
food.penup()
food.setpos(random.randint(-280, 280), random.randint(-280, 280))

# Boulder
boulder1 = turtle.Turtle()
boulder1.speed(0)
wn.register_shape("boulder.gif")
boulder1.shape("boulder.gif")
boulder1.penup()
boulder1.setpos(1000, -1000)

boulder2 = turtle.Turtle()
boulder2.speed(0)
wn.register_shape("boulder.gif")
boulder2.shape("boulder.gif")
boulder2.penup()
boulder2.setpos(1000, -1000)

boulder3 = turtle.Turtle()
boulder3.speed(0)
wn.register_shape("boulder.gif")
boulder3.shape("boulder.gif")
boulder3.penup()
boulder3.setpos(1000, -1000)

# Snake Head
snake_head = turtle.Turtle()
snake_head.speed(0)
wn.register_shape("snake head.gif")
snake_head.shape("snake head.gif")
snake_head.penup()
snake_head.setpos(0, 0)
snake_head.direction = "none"

# Snake Body
segments = []

# Score-board
score = 0
high_score = 0
score_board = turtle.Turtle()
score_board.speed(0)
score_board.color("white")
score_board.penup()
score_board.hideturtle()
score_board.setpos(0, 260)
score_board.write(f"Score: {str(score)}     High Score: {str(high_score)}", align="center",
                  font=("Arial", 16, "bold"))

# Game Over
game_over = turtle.Turtle()
game_over.speed(0)
game_over.color("white")
game_over.penup()
game_over.hideturtle()
game_over.setpos(0, 0)

# Functions
def move_left():
    if snake_head.direction != "right":
        snake_head.direction = "left"


def move_right():
    if snake_head.direction != "left":
        snake_head.direction = "right"


def move_up():
    if snake_head.direction != "down":
        snake_head.direction = "up"


def move_down():
    if snake_head.direction != "up":
        snake_head.direction = "down"


def move():
    if snake_head.direction == "left":
        snake_head.setx(snake_head.xcor() - 20)
    elif snake_head.direction == "right":
        snake_head.setx(snake_head.xcor() + 20)
    elif snake_head.direction == "up":
        snake_head.sety(snake_head.ycor() + 20)
    elif snake_head.direction == "down":
        snake_head.sety(snake_head.ycor() - 20)
    else:
        pass


# keyboard binding
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(move_up, "Up")
wn.onkeypress(move_down, "Down")


wn.tracer(0, 0)
while True:
    wn.update()

    # Food location
    if food.distance(snake_head) < 20:
        food.setpos(random.randint(-280, 280), random.randint(-280, 280))
        for segment in segments:
            if food.distance(segment) < 20:
                food.setpos(random.randint(-280, 280), random.randint(-280, 280))
        winsound.PlaySound("bite.wav", winsound.SND_ASYNC)
        # Add score
        score += 10
        score_board.clear()
        score_board.write(f"Score: {str(score)}     High Score: {str(high_score)}", align="center",
                          font=("Arial", 16, "bold"))

    # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        wn.register_shape("snake body.gif")
        new_segment.shape("snake body.gif")
        new_segment.penup()
        segments.append(new_segment)
        # Boulder location
        if len(segments) > 0 and len(segments) % 3 == 0:
            boulder1.setpos(random.randint(-280, 280), random.randint(-280, 280))
            boulder2.setpos(random.randint(-280, 280), random.randint(-280, 280))
            boulder3.setpos(random.randint(-280, 280), random.randint(-280, 280))
            if boulder1.distance(food) < 20:
                boulder1.setpos(random.randint(-280, 280), random.randint(-280, 280))
            if boulder2.distance(food) < 20:
                boulder2.setpos(random.randint(-280, 280), random.randint(-280, 280))
            if boulder3.distance(food) < 20:
                boulder3.setpos(random.randint(-280, 280), random.randint(-280, 280))
            if boulder1.distance(snake_head) < 200:
                boulder1.setpos(random.randint(-280, 280), random.randint(-280, 280))
            if boulder2.distance(snake_head) < 200:
                boulder2.setpos(random.randint(-280, 280), random.randint(-280, 280))
            if boulder3.distance(snake_head) < 200:
                boulder3.setpos(random.randint(-280, 280), random.randint(-280, 280))
            if boulder1.distance(boulder2) < 20:
                boulder1.setpos(random.randint(-280, 280), random.randint(-280, 280))
            if boulder2.distance(boulder3) < 20:
                boulder2.setpos(random.randint(-280, 280), random.randint(-280, 280))
            if boulder3.distance(boulder1) < 20:
                boulder3.setpos(random.randint(-280, 280), random.randint(-280, 280))
            for segment in segments:
                if boulder1.distance(segment) < 20:
                    boulder1.setpos(random.randint(-280, 280), random.randint(-280, 280))
                if boulder2.distance(segment) < 20:
                    boulder2.setpos(random.randint(-280, 280), random.randint(-280, 280))
                if boulder3.distance(segment) < 20:
                    boulder3.setpos(random.randint(-280, 280), random.randint(-280, 280))

    # Move the end segments first in reverse order
    for segment in range(len(segments)-1, 0, -1):
        segments[segment].setpos(segments[segment-1].xcor(), segments[segment-1].ycor())

    # Move segment 0 to where the head is
    if len(segments) > 0:
        segments[0].setpos(snake_head.xcor(), snake_head.ycor())

    # Move the segment before the head
    move()

    time.sleep(0.1)

    # Boulder collision checking
    if boulder1.distance(snake_head) < 20 or boulder2.distance(snake_head) < 20 or boulder3.distance(snake_head) < 20:
        winsound.PlaySound("game over.wav", winsound.SND_ASYNC)
        game_over.write(f"GAME OVER", align="center", font=("Arial", 20, "bold"))
        time.sleep(3)
        game_over.clear()
        snake_head.setpos(0, 0)
        snake_head.direction = "none"
        # Hide the segments after death so they don't stay on screen
        for segment in segments:
            segment.setpos(1000, 1000)
        # Clears the segments list so the snake starts with just his head
        segments.clear()
        food.setpos(random.randint(-280, 280), random.randint(-280, 280))
        boulder1.setpos(-1000, 1000)
        boulder2.setpos(-1000, 1000)
        boulder3.setpos(-1000, 1000)
        # Score
        if high_score < score:
            high_score = score
        else:
            pass
        score = 0
        score_board.clear()
        score_board.write(f"Score: {str(score)}     High Score: {str(high_score)}", align="center",
                          font=("Arial", 16, "bold"))

    # Border collision checking
    if snake_head.xcor() < -280 or snake_head.xcor() > 280 or snake_head.ycor() < -280 or snake_head.ycor() > 280:
        winsound.PlaySound("game over.wav", winsound.SND_ASYNC)
        game_over.write(f"GAME OVER", align="center", font=("Arial", 20, "bold"))
        time.sleep(3)
        game_over.clear()
        snake_head.setpos(0, 0)
        snake_head.direction = "none"
        for segment in segments:
            segment.setpos(1000, 1000)
        segments.clear()
        food.setpos(random.randint(-280, 280), random.randint(-280, 280))
        boulder1.setpos(-1000, 1000)
        boulder2.setpos(-1000, 1000)
        boulder3.setpos(-1000, 1000)
        # Score
        if high_score < score:
            high_score = score
        else:
            pass
        score = 0
        score_board.clear()
        score_board.write(f"Score: {str(score)}     High Score: {str(high_score)}", align="center",
                          font=("Arial", 16, "bold"))
    # Snake body collision checking
    for segment in segments:
        if snake_head.distance(segment) < 20:
            winsound.PlaySound("game over.wav", winsound.SND_ASYNC)
            game_over.write(f"GAME OVER", align="center", font=("Arial", 20, "bold"))
            time.sleep(3)
            game_over.clear()
            snake_head.setpos(0, 0)
            snake_head.direction = "none"
            for segment in segments:
                segment.setpos(1000, 1000)
            segments.clear()
            food.setpos(random.randint(-280, 280), random.randint(-280, 280))
            boulder1.setpos(-1000, 1000)
            boulder2.setpos(-1000, 1000)
            boulder3.setpos(-1000, 1000)
            # Score
            if high_score < score:
                high_score = score
            else:
                pass
            score = 0
            score_board.clear()
            score_board.write(f"Score: {str(score)}     High Score: {str(high_score)}", align="center",
                              font=("Arial", 16, "bold"))

