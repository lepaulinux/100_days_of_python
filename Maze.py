def turn_right():
    turn_left()
    turn_left()
    turn_left()
    move()


while front_is_clear():
    move()
while not at_goal():
    if wall_on_right() and front_is_clear():
        move()
    elif not wall_on_right():
        turn_right()
    elif wall_on_right() and wall_in_front:
        turn_left()
    elif wall_on_right() and wall_in_front():
        turn_left()
    elif not wall_on_right():
        turn_right()
    elif not wall_on_right() and wall_in_front:
        turn_left()



    
        

  
    


 

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
