import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
data = pandas.read_csv('50_states.csv')
# data['state'] = data['state'].str.lower()
image = 'blank_states_img.gif'
screen.addshape(image)

tim = turtle.Turtle()
tim.penup()
tim.hideturtle()
turtle.shape(image)
# count = 0
# score = 0
# answer = turtle.textinput(title=f'{score}/50 States Correct', prompt="What is the name of the state?")
# flag = True
guessed_states = []
missing_states = []
while len(guessed_states) < 50:
    answer = turtle.textinput(title=f'{len(guessed_states)}/50 States Correct',
                              prompt="What is the name of the next state?").title()
    if answer == "Exit":
        for i in data['state']:
            
            if i not in guessed_states:
                missing_states.append(i)
        df = pandas.DataFrame(missing_states)
        df.to_csv('states_to_learn.csv')
        break
    for state in data['state']:
        if state == answer:
            # count += 1
            # score += 1
            guessed_states.append(state)
            i = data[data['state'] == answer].index
            corx = int(data.iloc[i]['x'])
            cory = int(data.iloc[i]['y'])
            tim.setposition(corx, cory)
            tim.write(state)

# screen.exitonclick()
