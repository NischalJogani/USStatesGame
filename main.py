import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(730, 530)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
states_guessed = []

while len(states_guessed) < 50:
    user_guess = screen.textinput(f"{len(states_guessed)}/50 Guessed", prompt="Type in a state of America").title()

    if user_guess == "Exit":
        missing_states = [state for state in all_states if state not in states_guessed]
        missing_states_data = pandas.DataFrame(missing_states)
        missing_states_data.to_csv("states_to_learn.csv")
        break

    if user_guess in all_states:
        states_guessed.append(user_guess)
        t = turtle.Turtle()
        t.ht()
        t.penup()

        state_data = data[data.state == user_guess]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

