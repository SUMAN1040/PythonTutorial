"""
Classic Snake Game
Built with Python's standard library (Turtle graphics).

Controls:
  - W / Up Arrow    : Move Up
  - S / Down Arrow  : Move Down
  - A / Left Arrow  : Move Left
  - D / Right Arrow : Move Right
  - P               : Pause / Unpause
  - - / _           : Slow Down Speed
  - + / =           : Speed Up
  - R / Space       : Restart Game
  - Q / Escape      : Quit
"""

import turtle
import time
import random

# Game Configuration
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
GRID_SIZE = 20
INITIAL_DELAY = 0.20   # Slower, more comfortable starting speed (0.2s per move)
MIN_DELAY = 0.06       # Minimum delay cap
SPEED_INCREMENT = 0.003  # Very gradual speed-up per food eaten

# Colors (Modern Dark Theme)
BG_COLOR = "#181825"
HEADER_BG = "#11111b"
BORDER_COLOR = "#313244"
HEAD_COLOR = "#a6e3a1"
BODY_COLOR = "#94e2d5"
FOOD_COLOR = "#f38ba8"
TEXT_COLOR = "#cdd6f4"
ACCENT_COLOR = "#f9e2af"
GAME_OVER_COLOR = "#eba0ac"

# Game State
score = 0
high_score = 0
delay = INITIAL_DELAY
is_paused = False
is_game_over = False
segments = []

# Setup Screen
wn = turtle.Screen()
wn.title("Classic Snake Game")
wn.bgcolor(BG_COLOR)
wn.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
wn.tracer(0)  # Turns off screen updates for smooth rendering

# Draw Game Border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color(BORDER_COLOR)
border_pen.penup()
border_pen.setposition(-280, -280)
border_pen.pendown()
border_pen.pensize(3)
for _ in range(4):
    border_pen.forward(560)
    border_pen.left(90)
border_pen.hideturtle()

# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color(HEAD_COLOR)
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color(FOOD_COLOR)
food.penup()
food.goto(0, 100)

# Score Pen
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color(TEXT_COLOR)
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0, 255)

# Message Pen (Game Over / Pause)
msg_pen = turtle.Turtle()
msg_pen.speed(0)
msg_pen.penup()
msg_pen.hideturtle()


def update_score_display():
    score_pen.clear()
    score_pen.write(
        f"Score: {score}    |    High Score: {high_score}",
        align="center",
        font=("Courier", 16, "bold"),
    )


def show_message(title, subtitle, color=TEXT_COLOR):
    msg_pen.clear()
    msg_pen.color(color)
    msg_pen.goto(0, 20)
    msg_pen.write(title, align="center", font=("Courier", 24, "bold"))
    msg_pen.goto(0, -20)
    msg_pen.write(subtitle, align="center", font=("Courier", 14, "normal"))


def clear_message():
    msg_pen.clear()


# Movement Handlers
def go_up():
    if head.direction != "down" and not is_paused and not is_game_over:
        head.direction = "up"


def go_down():
    if head.direction != "up" and not is_paused and not is_game_over:
        head.direction = "down"


def go_left():
    if head.direction != "right" and not is_paused and not is_game_over:
        head.direction = "left"


def go_right():
    if head.direction != "left" and not is_paused and not is_game_over:
        head.direction = "right"


def toggle_pause():
    global is_paused
    if is_game_over:
        return
    is_paused = not is_paused
    if is_paused:
        show_message("PAUSED", "Press 'P' to Resume", ACCENT_COLOR)
    else:
        clear_message()


def slow_down():
    global delay
    # Increase delay to slow down snake (capped at 0.5s)
    delay = min(0.50, delay + 0.03)


def speed_up():
    global delay
    # Decrease delay to speed up snake
    delay = max(MIN_DELAY, delay - 0.03)


def move():
    if head.direction == "up":
        head.sety(head.ycor() + GRID_SIZE)
    elif head.direction == "down":
        head.sety(head.ycor() - GRID_SIZE)
    elif head.direction == "left":
        head.setx(head.xcor() - GRID_SIZE)
    elif head.direction == "right":
        head.setx(head.xcor() + GRID_SIZE)


def spawn_food():
    while True:
        # Generate random position aligned with grid (-260 to 260)
        x = random.randint(-13, 13) * GRID_SIZE
        y = random.randint(-13, 12) * GRID_SIZE

        # Ensure food doesn't spawn on snake head or body
        on_snake = (head.distance(x, y) < 15)
        for seg in segments:
            if seg.distance(x, y) < 15:
                on_snake = True
                break

        if not on_snake:
            food.goto(x, y)
            break


def trigger_game_over():
    global is_game_over, high_score
    is_game_over = True
    head.direction = "stop"
    if score > high_score:
        high_score = score
        update_score_display()
    show_message(
        "GAME OVER",
        "Press 'SPACE' or 'R' to Restart\nPress 'Q' to Quit",
        GAME_OVER_COLOR,
    )


def reset_game():
    global score, delay, is_game_over, is_paused, segments
    if not is_game_over:
        return

    clear_message()

    # Remove all segment turtles
    for seg in segments:
        seg.goto(1000, 1000)
    segments.clear()

    # Reset state
    head.goto(0, 0)
    head.direction = "stop"
    score = 0
    delay = INITIAL_DELAY
    is_game_over = False
    is_paused = False

    update_score_display()
    spawn_food()


def quit_game():
    try:
        wn.bye()
    except Exception:
        pass


# Keyboard Bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_up, "W")
wn.onkeypress(go_up, "Up")

wn.onkeypress(go_down, "s")
wn.onkeypress(go_down, "S")
wn.onkeypress(go_down, "Down")

wn.onkeypress(go_left, "a")
wn.onkeypress(go_left, "A")
wn.onkeypress(go_left, "Left")

wn.onkeypress(go_right, "d")
wn.onkeypress(go_right, "D")
wn.onkeypress(go_right, "Right")

wn.onkeypress(toggle_pause, "p")
wn.onkeypress(toggle_pause, "P")

wn.onkeypress(slow_down, "minus")

wn.onkeypress(speed_up, "plus")
wn.onkeypress(speed_up, "equal")

wn.onkeypress(reset_game, "r")
wn.onkeypress(reset_game, "R")
wn.onkeypress(reset_game, "space")

wn.onkeypress(quit_game, "q")
wn.onkeypress(quit_game, "Q")
wn.onkeypress(quit_game, "Escape")

# Initial display
update_score_display()
spawn_food()

# Main Game Loop
try:
    while True:
        wn.update()

        if not is_paused and not is_game_over:
            # Check for collision with border (-270 to 270 boundary)
            if (
                head.xcor() > 270
                or head.xcor() < -270
                or head.ycor() > 270
                or head.ycor() < -270
            ):
                trigger_game_over()

            # Check for collision with food
            elif head.distance(food) < 18:
                spawn_food()

                # Add a new body segment
                new_segment = turtle.Turtle()
                new_segment.speed(0)
                new_segment.shape("square")
                new_segment.color(BODY_COLOR)
                new_segment.penup()
                segments.append(new_segment)

                # Increase score and speed
                score += 10
                if score > high_score:
                    high_score = score
                update_score_display()

                # Shorten delay to increase speed
                delay = max(MIN_DELAY, delay - SPEED_INCREMENT)

            # Move body segments in reverse order
            if not is_game_over and head.direction != "stop":
                for index in range(len(segments) - 1, 0, -1):
                    x = segments[index - 1].xcor()
                    y = segments[index - 1].ycor()
                    segments[index].goto(x, y)

                # Move segment 0 to head position
                if len(segments) > 0:
                    segments[0].goto(head.xcor(), head.ycor())

                move()

                # Check for collision between head and body segments
                for segment in segments:
                    if segment.distance(head) < 15:
                        trigger_game_over()
                        break

        time.sleep(delay)

except turtle.Terminator:
    pass
except Exception:
    pass
