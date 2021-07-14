import turtle

import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")

states = data.state.to_list()
guessed_states = []

def create_state():
    state = turtle.Turtle()
    state.hideturtle()
    state.penup()
    state_data = data[data["state"] == answer_state]
    state.goto(int(state_data.x), int(state_data.y))
    state.write(answer_state)


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 State Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_state = [state for state in states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("state_to_learn.csv")
        break
    if answer_state in states:
        guessed_states.append(answer_state)
        create_state()

