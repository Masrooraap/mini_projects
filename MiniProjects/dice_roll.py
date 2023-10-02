import  random
def DiceRoll():
    dice_sides = 6
    rolling = True
    while rolling:
        roll_command = input("do you want to roll again? ENTER=roll. Q=quit")
        if roll_command.lower() != "q":
            rolled_value = random.randint(1,dice_sides)
            rolling = True
            print("you have rolled:", rolled_value)
        else:
            rolling = False
    print("thanks for playing ")
DiceRoll()
