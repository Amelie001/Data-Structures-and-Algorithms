def mergeSort(arr):
    
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


arr = [15, 2, 43, 8, 1, 6, 99]

evens = [x for x in arr if x % 2 == 0]

sorted_evens = mergeSort(evens)

print(sorted_evens)