def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def minimum_swaps(arr):
    annotated = [*enumerate(arr)]
    annotated.sort(key = lambda it: it[1])

    count = 0

    i = 0
    while i < len(arr):
        if annotated[i][0] == i:
            i += 1
            continue
        swap(annotated, i, annotated[i][0])
        count += 1

    return count
 
# Driver Code     
arr = [7, 1, 3, 2, 4, 5, 6]
print(minimum_swaps(arr))
