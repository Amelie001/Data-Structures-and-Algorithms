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
        if len(left[i]) <= len(right[j]): 
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

list = ["coco", "zebra", "phone", "helicopter", "light", "apple", "tissue"]

print("Original list:", list)

sorted_list = merge_sort(list)

print("Sorted list:", sorted_list)