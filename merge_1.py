def merge_sort(arr): 

    if len(arr) <= 1: 
        return arr

    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right): 

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

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right): 
        result.append(right[j])
        j += 1

    return result 


numbers = [38, 12, 27, 43, 9, 31, 18, 25]

print("Original list:", numbers)

sorted_numbers = merge_sort(numbers)

print("Sorted list:", sorted_numbers)