# Quick sort

def partition(low, high):
    pivot = nums[-1]
    i = low - 1
    for j in range(low, high):
        if nums[j] > pivot:
            continue
        i


def quicksort(low, high):
    # partitioning
    p1 = partition(low, high)

nums = [1, 12, 5, 16, 10, 20]
quicksort(0, len(nums) - 1)
