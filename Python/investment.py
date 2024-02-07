import math
import random

accounts = [random.randint(0, 5000) for _ in range(20)]

while True:
    option = int(input(
        f"MAIN MENU \n 1. Print Accounts \n 2. Deposit \n 3. Withdrawal \n 4. Count Under $2000 \n 5. Generous Donor \n 6. Hacker Attack \n 7. Exit \nEnter Option #: "
        ))
    
    match option:
        case 1:
            print("ACCOUNT BALANCES")
            for i, value in enumerate(accounts):
                print(f"Acount {i}: ${value}")
        case 2:
            print("DEPOSIT")
            accnum = option("Enter account #: ")

        # case 3: 

        # case 4: 
        
        # case 5:

        # case 6:
            
        case 7:
            exit()

print(option)