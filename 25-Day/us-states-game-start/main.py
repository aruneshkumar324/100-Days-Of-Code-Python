import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

score = 0

game_on = True

while game_on:
    if score <= 50:
        answer_state = turtle.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()

        data = pandas.read_csv("50_states.csv")

        state_data = data[data.state == answer_state]

        state_count = data[data.state == answer_state].count()

        state_count = state_count.state

        x_value = float(state_data.x)
        y_value = float(state_data.y)
        print(state_data)
        turtle.penup()
        turtle.goto(x_value, y_value)
        turtle.write(answer_state, align="center", font=('Arial', 12, 'normal'))

        score += 1
    else:
        game_on = False

