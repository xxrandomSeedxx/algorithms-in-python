# Quick sort
a = [1, 12, 5, 16, 10, 20]

# partitioning
pivot = a[-1]
left = 0
right = len(a) - 1
for i in range(left, right + 1):
    if left < pivot:
        continue
    left = i
for j in range(right, 0, -1):
    if right > pivot:
        continue
    right = j
