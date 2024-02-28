# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression

def linearSearch(anArray, item):
    for index in range(len(anArray)):
        if anArray[index] == item:
            return index
    return -1

def binarySearch(anArray, item):
    lower, upper = 0, len(anArray) - 1
    while lower <= upper:
        middle = (upper + lower) // 2
        if item == anArray[middle]:
            return middle
        elif item < anArray[middle]:
            upper = middle - 1
        else:
            lower = middle + 1

    return -1

def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    part = int(input("Main Menu \n 1: Spell Check a Word (Linear Search) \n 2: Spell Check a Word (Binary Search) \n 3: Spell Check Alice In Wonderland (Linear Search) \n 4: Spell Check Alice In Wonderland (Binary Search) \n 5: Exit \n Enter menu selection (1-5): "))
    
    match part:
        case 1:
            usersword = input("Enter word to search for: ") 
            print("Linear Search starting...")
            if linearSearch(dictionary, usersword) != -1:
                print(f"{usersword} is IN the dictionary at index {dictionary.index(usersword)}")
            else:
                print(f"{usersword} is NOT IN the dictionary")
        case 2:
            usersword = input("Enter word to search for: ")
            print("Binary Search starting...")
            if binarySearch(dictionary, usersword) != -1:
                print(f"'{usersword}' is IN the dictionary at index {dictionary.index(usersword)}")
            else:
                print(f"'{usersword}' is NOT IN the dictionary")
            

def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)


# Call main() to begin program
main()
