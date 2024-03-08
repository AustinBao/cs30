# SORT ANALYZER STARTER CODE

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


# Bubble sort
startTime = time.time()
bubbleSort(randomData)
endTime = time.time()
print(f"Bubble Sort Random Data: {endTime - startTime} seconds")

startTime = time.time()
bubbleSort(reversedData)
endTime = time.time()
print(f"Bubble Sort Reversed Data: {endTime - startTime} seconds")

startTime = time.time()
bubbleSort(nearlySortedData)
endTime = time.time()
print(f"Bubble Sort Nearly Data: {endTime - startTime} seconds")

startTime = time.time()
bubbleSort(fewUniqueData)
endTime = time.time()
print(f"Bubble Sort Random Data: {endTime - startTime} seconds")




startTime = time.time()
selectionSort(randomData)
endTime = time.time()
print(f"Selection Sort Random Data: {endTime - startTime} seconds")

startTime = time.time()
selectionSort(reversedData)
endTime = time.time()
print(f"Selection Sort Reversed Data: {endTime - startTime} seconds")

startTime = time.time()
selectionSort(nearlySortedData)
endTime = time.time()
print(f"Selection Sort Nearly Data: {endTime - startTime} seconds")

startTime = time.time()
selectionSort(fewUniqueData)
endTime = time.time()
print(f"Selection Sort Random Data: {endTime - startTime} seconds")




startTime = time.time()
insertionSort(randomData)
endTime = time.time()
print(f"insertion Sort Random Data: {endTime - startTime} seconds")

startTime = time.time()
insertionSort(reversedData)
endTime = time.time()
print(f"insertion Sort Reversed Data: {endTime - startTime} seconds")

startTime = time.time()
insertionSort(nearlySortedData)
endTime = time.time()
print(f"insertion Sort Nearly Data: {endTime - startTime} seconds")

startTime = time.time()
insertionSort(fewUniqueData)
endTime = time.time()
print(f"insertion Sort Random Data: {endTime - startTime} seconds")
