#   THIS IS SNAKE WATER GAME

import random
list=["snake","water","gun"]

chances=10
computer_point=0
human_point=0
no_of_chances=0

print("\t \t \t THIS IS A GAME \t \t \t")
print("YOU HAVE TO PICK SNAKE OR WATER OR GUN")

try:

    while no_of_chances<chances:
        print("please!enter snake or water or gun")
        _input=input("Enter snake or water or gun:")
        _random=random.choice(list)

        if _input==_random:
            print("you both choose same so u did not get any point")

        elif _input=="water" and _random=="snake":
            computer_point=computer_point+1
            print(f"computer have choosen {_random} and you choosen  {_input}")
            print("computer got point")
            print(f"you got {human_point} and computer got {computer_point}")
        elif _input == "snake" and _random == "water":
            human_point=human_point+1
            print(f"computer have choosen {_random} and you choosen  {_input}")
            print("you got a point")
            print(f"you got {human_point} and computer got {computer_point}")
        elif _input == "snake" and _random == "gun":
            computer_point = computer_point + 1
            print(f"computer have choosen {_random} and you choosen  {_input}")
            print("computer got point")
            print(f"you got {human_point} and computer got {computer_point}")
        elif _input == "gun" and _random == "snake":
            human_point=human_point+1
            print(f"computer have choosen {_random} and you choosen  {_input}")
            print("you got point")
            print(f"you got {human_point} and computer got {computer_point}")
        elif _input == "gun" and _random == "water":
            computer_point = computer_point + 1
            print(f"computer have choosen {_random} and you choosen  {_input}")
            print("computer got point")
            print(f"you got {human_point} and computer got {computer_point}")
        elif _input == "water" and _random == "gun":
            human_point=human_point+1
            print(f"computer have choosen {_random} and you choosen  {_input}")
            print("you got point")
            print(f"you got {human_point} and computer got {computer_point}")
        else:
            print("PLEASE! ENTER ONLY VALID INPUT")
        no_of_chances=no_of_chances+1
        print(f'you left out with {chances-no_of_chances} of {chances}')
except Exception as e:
    print(e)
print("please enter the valid input")
print("GAME OVER")
if human_point==computer_point:
    print("game is end up with tie")
elif human_point>computer_point:
    print("YOU HAVE WON THE GAME")
else:
    print("COMPUTER HAVE WON THE GAME")