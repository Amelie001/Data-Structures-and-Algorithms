# Smallest Missing Number 

numbers = [0, 1, 2, 4, 5, 6, 8, 9, 10, 12, 13, 14, 16]

low = 0
high = len(numbers) - 1

while low <= high:
    mid = (low + high) // 2

    if numbers[mid] == mid:
        low = mid + 1
    else:
        high = mid - 1

print("Smallest missing number:", low)