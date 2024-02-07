import random

def displayAccounts():
    print("ACCOUNT BALANCES")
    for i, value in enumerate(accounts):
        print(f"Acount {i}: ${value}")

def deposit():
    print("DEPOSIT")
    accountnum = int(input("Enter account #: "))
    deposit = input("Enter amount to deposit: ")
    print(f"Acount {accountnum} Previous Balance: ${accounts[accountnum]}")
    accounts[accountnum] += int(deposit[1:])
    print(f"Acount {accountnum} New Balance: ${accounts[accountnum]}")

def withdrawal():
    print("WITHDRAWAL")
    accountnum = int(input("Enter account #: "))
    withdraw = input("Enter amount to withdraw: ")
    if int(accounts[accountnum]) < int(withdraw[1:]):
        print("Sorry, insufficient funds.")
    else:            
        print(f"Acount {accountnum} Previous Balance: ${accounts[accountnum]}")
        accounts[accountnum] -= int(withdraw[1:])
        print(f"Acount {accountnum} New Balance: ${accounts[accountnum]}")

def under2000():
    print("ACCOUNT(S) UNDER $2000")
    counter = 0
    for i, value in enumerate(accounts):
        if value < 2000:
            counter += 1
            print(f"Account {i}: ${value}")
    print(f"Account(s) with less that $2000: {counter}")

def generousDonor():
    print("GENEROUS DONOR")
    counter = 0
    for i, value in enumerate(accounts):
        if value < 2000:
            counter += 1
            print(f"Account {i} Previous Balance: ${accounts[i]}")
            accounts[i] += 500
            print(f"Account {i} New Balance: ${accounts[i]}")
    print(f"Accounts that recieved donations of $500: {counter}") 
    print(f"Total amount donated: {counter * 500}") 

def hacker():
    totalstolen = 0
    for i, value in enumerate(accounts):
        accounts[i] = value * 0.95
        totalstolen += value * 0.05
    print(f"Total stolen is: ${totalstolen}")


accounts = [random.randint(0, 5000) for _ in range(20)]

while True:
    option = int(input(
        f"MAIN MENU \n 1. Print Accounts \n 2. Deposit \n 3. Withdrawal \n 4. Count Under $2000 \n 5. Generous Donor \n 6. Hacker Attack \n 7. Exit \nEnter Option #: "
        ))
    
    match option: 
        case 1:
            displayAccounts()
        case 2:
            deposit()
        case 3: 
            withdrawal()
        case 4: 
            under2000()
        case 5:
            generousDonor()
        case 6:
            hacker()
        case 7:
            exit()

