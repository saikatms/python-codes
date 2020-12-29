def swap(numbers, i, j):
    numbers[i], numbers[j] = numbers[j], numbers[i]

def minimum_swaps(numbers):
    annotated = [*enumerate(numbers)]
    annotated.sort(key = lambda it: it[1])

    count = 0

    i = 0
    while i < len(numbers):
        if annotated[i][0] == i:
            i += 1
            continue
        swap(annotated, i, annotated[i][0])
        count += 1
    return count
 
numbers = [7, 1, 3, 2, 4, 5, 6]
print(minimum_swaps(numbers))
