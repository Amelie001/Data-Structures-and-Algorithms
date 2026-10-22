import time 

numbers = list(range(1, 10001))

target = 10000

start_time = time.time()

found = False 
for num in numbers: 
    if num == target: 
        found = True 
        break 

end_time = time.time()

linear_time = end_time - start_time 
print("Linear search time:", linear_time)

start_time = time.time()

low = 0 
high = len(numbers) - 1 
found = False 

while low <= high: 
    mid = (low + high) // 2 

    if numbers[mid] == target: 
        found = True 
        break
    elif numbers[mid] < target: 
        low = mid + 1
    else: 
        high = mid - 1 

end_time = time.time()

binary_time = end_time - start_time 
print("Binary search time:", binary_time)