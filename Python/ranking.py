import random

def printList():
    print("RANK LIST")
    if len(ranklist) == 0:
        print("No Items in the Rank List")
    else:
        counter = 1
        for item in ranklist:
            print(f"{counter}. {item}")
            counter += 1

def addItemToEnd():
    print("ADD ITEM TO END")
    ranklist.append(input("Enter Item: "))
    printList()

def removeLastItem():
    print("REMOVE LAST ITEM")
    ranklist.pop()
    printList()

def insertAtPosition():
    print("INSERT ITEM")
    position = int(input("Insert Position: "))
    item = input("Item to Insert: ")
    ranklist.insert(position, item)
    printList()

def removeAtPosition():
    print("REMOVE AT POSITION")
    position = int(input("Position to remove: "))

    try:
        ranklist.pop(position)
    except IndexError:
        print("Please Enter a Valid Positiion")
    else:
        print(f"{ranklist[position]} removed from position {position}")
        printList()

def moveToPosition():
    pass

def editItem():
    pass

ranklist = ["Pizza", "Salad", "Pasta", "Apple"]

while True:
    option = int(input(
        f"*** MAIN MENU *** \n 1. Print List \n 2. Add Item to End \n 3. Remove Last Item \n 4. Insert at Position \n 5. Remove at Position \n 6. Move to Position \n 7. Edit Item \n 8. Exit \n Enter Option #: "
        ))
    
    match option: 
        case 1:
            printList()
        case 2:
            addItemToEnd()
        case 3: 
            removeLastItem()
        case 4: 
            insertAtPosition()
        case 5:
            removeAtPosition()
        case 6:
            moveToPosition()
        case 7:
            editItem()
        case 8:
            exit()
