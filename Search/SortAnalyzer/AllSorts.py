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


print(bubbleSort([6, 9, 2, 3, 5]))
print(selectionSort([6, 9, 2, 3, 5]))
print(insertionSort([6, 9, 2, 3, 5]))
