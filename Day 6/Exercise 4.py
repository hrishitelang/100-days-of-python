def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if wall_in_front():
        turn_left()
    elif right_is_clear():
        turn_right()
        move()
        turn_right()
        move()
    elif front_is_clear():
        move()
