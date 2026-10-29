numbers = [15, 32, 59, 21, 48]

for i in range(len(numbers)):
    for j in range(len(numbers) - 1 - i):
        if numbers[j] % 10 > numbers[j + 1] % 10:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted list:", numbers)