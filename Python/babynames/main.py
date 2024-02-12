# BABY NAMES DATA ASSIGNMENT START CODE

import json


def main():
    # Load Baby Data from File
    file = open("baby-names-data.json")
    baby_data = json.load(file)
    print(type(baby_data))
    file.close()

    # Main Menu
    loop = True
    while loop:
        selection = getMenuSelection()

        if selection == "1":
            displayAll(baby_data)
        elif selection == "2":
            searchGender(baby_data)
        elif selection == "3":
            searchRank(baby_data)
        elif selection == "4":
            searchStartLetter(baby_data)
        elif selection == "5":
            searchNameLength(baby_data)
        elif selection == "6":
            print("\nGOODBYE!\n")
            loop = False


def getMenuSelection():
    # Print Menu & Return User Selection
    print("\n*** BABY DATA - MAIN MENU ***")
    print("* 1: Display All")
    print("* 2: Search by Gender")
    print("* 3: Search by Rank")
    print("* 4: Search by Starting Letter")
    print("* 5: Search by Name Length")
    print("* 6: Exit")

    return input("* Enter Option #: ")


def displayAll(baby_data):
    # Display All Baby Data
    print("\nDISPLAY ALL")
    for baby in baby_data:
        print(f"{baby['name']} (Rank: {baby['rank']}, Gender: {baby['gender']})")


def searchGender(baby_data):
    # Dislay All Baby Names based on Genders
    print("\nSEARCH BY GENDER")
    inputgender = input("Enter a gender (Boy/Girl): ")
    print('\n')
    for baby in baby_data:
        if baby["gender"] == inputgender:
            print(f"{baby['name']} (Rank: {baby['rank']}, Gender: {baby['gender']})")



def searchRank(baby_data):
    # Display All Baby Names based on Rank
    print("\nSEARCH BY RANK")
    minrank = int(input("Enter a minimum rank: "))
    maxrank = int(input("Enter a maximum rank: "))
    print('\n')
    for baby in baby_data:
        if baby["rank"] >= minrank and baby["rank"] <= maxrank:
            print(f"{baby['name']} (Rank: {baby['rank']}, Gender: {baby['gender']})")



def searchStartLetter(baby_data):
    # Insert User Item into a Position
    print("\nSEARCH BY START LETTER")
    startletter = input("Enter a starting letter: ")
    print('\n')
    for baby in baby_data:
        if baby["name"][0] == startletter:
            print(f"{baby['name']} (Rank: {baby['rank']}, Gender: {baby['gender']})")


def searchNameLength(baby_data):
    # Remove item from position
    print("\nSEARCH BY NAME LENGTH")
    counter = 0
    length = int(input("Enter a name length: "))
    for baby in baby_data:
        if len(baby["name"]) == length:
            print(f"{baby['name']} (Rank: {baby['rank']}, Gender: {baby['gender']})")
            counter += 1
    print(f"Number of names found: {counter}")

# Invoke main to begin program
main()
