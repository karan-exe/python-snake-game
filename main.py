from snake import Snake
from food import Food
from score_board import ScoreBoard
from turtle import Screen
from high_score_mod import HighScore
import time

screen = Screen()
screen.setup(width=600, height=600)
food = Food()
score = ScoreBoard()
high_score = HighScore()
orochimaru = Snake()

screen.bgcolor('black')
screen.title("Orochimaru")
screen.tracer(0)

screen.listen()
screen.onkey(fun=orochimaru.up, key='Up')
screen.onkey(fun=orochimaru.down, key='Down')
screen.onkey(fun=orochimaru.right, key='Right')
screen.onkey(fun=orochimaru.left, key='Left')

game_continues = True
while game_continues:
    screen.update()
    time.sleep(0.2)
    orochimaru.moving_snake()
    head_position = orochimaru.head.pos()
    headx = head_position[0]
    heady = head_position[1]

    food_position = food.pos()
    foodx = food_position[0]
    foody = food_position[1]

    with open("high score.txt") as hsfile:
        update = hsfile.read()
    updated_high_score = int(update)
    high_score.show_score(updated_high_score)
    # eating food
    if orochimaru.head.distance(food) < 15:
        orochimaru.snake_ate_food()
        score.score_increase()
        if score.score > updated_high_score:
            high_score.score_increase()
            with open("high score.txt", mode='w') as hsfile:
                hsfile.write(str(score.score))
        food.refresh()
    # collision with its own tail
    for blocks in range(1, len(orochimaru.initial_body)-1):
        if orochimaru.head.distance(orochimaru.initial_body[blocks]) < 5:
            for blocks in range(len(orochimaru.initial_body) - 1, 0, -1):
                time.sleep(0.1)
                screen.update()
                orochimaru.initial_body[blocks].hideturtle()
            game_continues = False
    #collision with wall
    if orochimaru.head.xcor() > 280 or orochimaru.head.ycor() > 280 or orochimaru.head.xcor() < -280 or orochimaru.head.ycor() < -280:
        for blocks in range(len(orochimaru.initial_body) - 1, 0, -1):
            screen.update()
            time.sleep(0.1)
            orochimaru.initial_body[blocks].hideturtle()
        game_continues = False

while True:
    screen.update()
    time.sleep(0.5)
    score.game_over()
    screen.update()
    time.sleep(0.25)

screen.exitonclick()