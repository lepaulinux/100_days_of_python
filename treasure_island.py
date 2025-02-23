from os import waitid
from pyexpat.errors import messages

# Display ASCII art for the game title
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     ""=.|                  |
|___________________|__"=._o`"-._        ""=.______________|___________________
          |                ""=._o`"=._      _`"=._                     |
 _________|_____________________:=._o ""=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; ""=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    ""-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o ""=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      "".o|o_.--"    ;o;____/______/______/____
/______/______/______/""=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__""=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____""=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____""=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

# Welcome message
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# First decision point: Crossroad
print("You're at a cross road. Where do you want to go? ")
answer = input("Type \"left\" or \"right\": \n").lower()  # Convert input to lowercase

if answer == "left":
    # Second decision point: Lake
    lake_opt = input("You've come to a lake. There is an island in the middle of the lake.\nType \"wait\" to wait for a boat. Type \"swim\" to swim across. \n").lower()
    
    if lake_opt == "wait":
        # Third decision point: Doors
        door_opt = input("You arrive at the island unharmed. There is a house with 3 doors.\nOne red, one yellow and one blue. Which colour do you choose? \n").lower()
        
        if door_opt == "red":
            print("Burned by fire.\nGame Over.")
        elif door_opt == "yellow":
            print("You Win!")
            print(r'''    
             ___________
            '._==_==_=_.''
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
              `"""""""`
''')
        elif door_opt == "blue":
            print("Eaten by beasts.\nGame Over.")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout.\nGame Over")
elif answer == "right":
    print("You fall into a hole.\nGame Over.")
