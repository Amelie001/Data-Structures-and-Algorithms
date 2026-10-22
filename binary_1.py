# Student Marks 

marks = [35, 42, 50, 58, 65, 72, 80, 88, 95, 100]

target = int(input("Enter the mark to search for: "))

low = 0
high = len(marks) - 1 
found = False 

while low <= high: 
    mid = (low + high) // 2

    if marks[mid] == target: 
        print("Mark found at index:", mid)
        found = True 
        break 

    elif marks[mid] < target: 
        low = mid + 1

    else: 
        high = mid - 1

if found == False:
    print("Marks not found.")