import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()

guessed_state = []

while len(guessed_state) < 50:
    answer_state = turtle.textinput(title=f"{len(guessed_state)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == 'Exit':
        # missing_states = []
        # for state in all_state:
        #     if state not in guessed_state:
        #         missing_states.append(state)
        missing_states = [state for state in all_state if state not in guessed_state]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn1.csv")

        break
    if answer_state in all_state:
        guessed_state.append(answer_state)
        tom = turtle.Turtle()
        tom.hideturtle()
        tom.penup()

        state_data = data[data.state == answer_state]
        tom.goto(int(state_data.x), int(state_data.y))

        tom.write(answer_state)

# a = list(set(all_state) - set(guessed_state))
# b = pandas.DataFrame(a)
# b.to_csv('states_to_learn.csv')

'''
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

'''