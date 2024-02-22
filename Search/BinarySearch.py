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


nums = [10, 30, 40, 45, 70, 80, 85, 90, 100]
words = ["at", "ball", "cat", "dog", "eye", "fish", "good"]
unsorted = [30, 20, 70, 40, 50, 100, 90]

print(binarySearch(nums, 100))
print(binarySearch(nums, 75))
print(binarySearch(words, "fish"))
print(binarySearch(words, "at"))
print(binarySearch(unsorted, 70))

