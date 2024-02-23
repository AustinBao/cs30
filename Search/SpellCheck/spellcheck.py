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

    part = input("Part a or b: ")
    searchtype = input("'binary' or 'linear': ")
    counter = 0

    match part:
        case "a":
            searchword = input("Enter word to find: ")
            if searchtype is "binary":
                result = binarySearch(dictionary, searchword)
                if result == -1:
                    return "Could not find word"
            else:
                result = linearSearch(dictionary, searchword)
                if result == -1:
                    return "Could not find word"

            return "Word found"

        case "b":

            if searchtype is "binary":
                for word in aliceWords:
                    result = binarySearch(dictionary, word)
                    if result != -1:
                        counter += 1
            else:
                result = linearSearch(dictionary, searchword)
                if result == -1:
                    return "Could not find word"

            return "Word found"

def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)


# Call main() to begin program
print(main())
