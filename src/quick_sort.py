# Quick sort
array = [10, 80, 30, 90, 40, 70]


def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] > pivot:
            continue
        i += 1
        if array[i] == array[j]:
            continue
        (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quicksort(array, low, high):
    # partitioning
    if low < high:
        p1 = partition(array, low, high)
        quicksort(array, low, p1 - 1)
        quicksort(array, p1 + 1, high)


quicksort(array, 0, len(array) - 1)

print(array)
