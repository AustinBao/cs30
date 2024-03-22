# SORT ANALYZER STARTER CODE
import inspect
import time


def bubbleSort(anArray):
    for j in range(len(anArray) - 1):
        for i in range(len(anArray) - 1 - j):
            if anArray[i] > anArray[i + 1]:
                temp = anArray[i]
                anArray[i] = anArray[i + 1]
                anArray[i + 1] = temp
    return anArray


def selectionSort(anArray):
    for i in range(len(anArray) - 1):
        minimum = i
        for j in range(i + 1, len(anArray)):
            if anArray[j] < anArray[minimum]:
                minimum = j
        temp = anArray[i]
        anArray[i] = anArray[minimum]
        anArray[minimum] = temp
    return anArray


def insertionSort(anArray):
    for i in range(1, len(anArray)):
        value = anArray[i]
        insertpos = i
        while insertpos > 0 and anArray[insertpos - 1] > value:
            anArray[insertpos] = anArray[insertpos - 1]
            insertpos -= 1

        anArray[insertpos] = value

    return anArray


# RETURN DATA FROM FILE AS AN ARRAY OF INTERGERS
def loadDataArray(fileName):
    temp = []

    # Read file line by line
    fileref = open(fileName, "r")
    for line in fileref:
        line = line.strip()  # Clean up line
        temp.append(int(line))  # Add integer to temp list

    fileref.close()

    return temp


# LOAD DATA FILE INTO GLOBAL VARIABLES
randomData = loadDataArray("data-files/random-values.txt")
reversedData = loadDataArray("data-files/reversed-values.txt")
nearlySortedData = loadDataArray("data-files/nearly-sorted-values.txt")
fewUniqueData = loadDataArray("data-files/few-unique-values.txt")


def sortTimes(sortType, dataset, datasetName):
    starttime = time.time()
    sortType(dataset)
    endtime = time.time()
    print(f"{sortType.__name__} on {datasetName} took: {endtime - starttime} seconds")


# Bubble sort
# sortTimes(bubbleSort, randomData, "randomData")
# sortTimes(bubbleSort, reversedData, "reversedData")
# sortTimes(bubbleSort, nearlySortedData, "nearlySortedData")
# sortTimes(bubbleSort, fewUniqueData, "fewUniqueData")
# Selection sort
# sortTimes(selectionSort, randomData, "randomData")
# sortTimes(selectionSort, reversedData, "reversedData")
# sortTimes(selectionSort, nearlySortedData, "nearlySortedData")
# sortTimes(selectionSort, fewUniqueData, "fewUniqueData")
# Insertion sort
sortTimes(insertionSort, randomData, "randomData")
sortTimes(insertionSort, reversedData, "reversedData")
sortTimes(insertionSort, nearlySortedData, "nearlySortedData")
sortTimes(insertionSort, fewUniqueData, "fewUniqueData")
