import random 
import time 

arr1 = [random.randint(1, 1000) for _ in range(1000)]

arr2 =  arr1.copy()

start = time.time()

n = len(arr1)

for i in range(n): 
    for j in range(0, n - i - 1): 
        if arr1[j] > arr1[j + 1]: 
            arr1[j], arr1[j + 1] = arr1[j + 1], arr1[j]

end = time.time()

print("Bubble Sort Time:", end - start)

start = time.time()

for i in range(1, len(arr2)):
    key = arr2[i]
    j = i - 1

    while j >= 0 and key < arr2[j]: 
        arr2[j + 1] = arr2[j]
        j -= 1

    arr2[j + 1] = key 

end = time.time()

print("Insertion Sort Time:", end - start)