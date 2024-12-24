def turn_right():
    turn_left()
    turn_left()
    turn_left()

def stay_right():
    while wall_on_right():
        if wall_in_front():
            turn_left()
        else:
            move()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
