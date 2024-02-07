import random

def changeName():
    print("CHANGE NAME")
    firstname = input("Please enter first name: ")
    lastname = input("Please enter last name: ")
    print(f"Name has been changed to {firstname} {lastname}") 
    return firstname, lastname

def displayRandomNickname(firstname, nicknames, lastname):
    print("RANDOM NICKNAME")
    i = random.randint(0, len(nicknames))
    print(f"{firstname} '{nicknames[i]}' {lastname}")

def displayAllNicknames(firstname, nicknames, lastname):
    print("ALL NICKNAMES")
    for names in nicknames:
        print(f"{firstname} '{names}' {lastname}")

def addNickname():
    print("ADD A NICKNAME")
    name = input("Please enter a nickname to add: ")
    if name not in nicknames:
        nicknames.append(name)
        print(f"{name} added to the nickname list.")
    else:
        print(f"{name} already in the nickname list.")

def removeNickname():
    print("REMOVE A NICKNAME")
    name = input("Please enter a nickname to remove: ")
    if name not in nicknames:
        print(f"{name} was not found in the nickname list.")
    else:
        nicknames.remove(name)
        print(f"{name} removed from the nickname list.")



nicknames = ["Joe", "The Harsh", "Bob", "The Small", "The Raunch", "The Great"]

firstname, lastname = changeName()

while True:
    option = int(input(
        f"MAIN MENU ({firstname} {lastname}) \n 1. Change Name \n 2. Display a Random Nickname \n 3. Display All Nicknames \n 4. Add a Nickname \n 5. Remove a Nickname \n 6. Exit \n"
        ))
    
    match option: 
        case 1:
            firstname, lastname = changeName()
        case 2:
            displayRandomNickname(firstname, nicknames, lastname)
        case 3: 
            displayAllNicknames(firstname, nicknames, lastname)
        case 4: 
            addNickname()
        case 5:
            removeNickname()
        case 6:
            exit()
            

