import math
import random

def roll2Dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    return f"{dice1}, {dice2} (sum: {dice1 + dice2})"

while True:
    option = int(input(
    f"Dice Roll Simulator Menu \n 1. Roll Dice Once \n 2. Roll Dice 5 Times \n 3. Roll Dice 'n' Times \n 4. Roll Dice until Snake Eyes \n 5. Exit \n Select an option (1-5): "
    ))

    if option == 1:
        print(roll2Dice())
        pass
    elif option == 2:
        for i in range(5):
            print(roll2Dice())
        pass
    elif option == 3:
        n = int(input("How many rolls would you like? "))
        for i in range(n):
            print(roll2Dice())
        pass
    elif option == 4:
        counter = 0 
        while True:
            result = roll2Dice()
            print(result)
            x,y = result[0], result[3]
            counter += 1
            if x == "1" and y == "1":
                print(f"SNAKE EYES! It took {counter} rolls to get snake eyes")
                pass
    else:
        break
    
    
    