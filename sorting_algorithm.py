
students = []

# Add Student

def add_student(): 
    name = input("Enter student name: ")
    marks = int(input("Enter student marks: "))

    students.append([name, marks])

    print("Student added successfully!")

# Display Students

def display_students(data): 

    if len(data) == 0: 
        print("No student records found.")
    else: 
        print("\nStudent Records:")

        for student in data: 
            print(student[0], "-", student[1])

# Bubble Sort

def bubble_sort(): 

    data = students.copy()
    n = len(data)

    for i in range(n): 

        for j in range(n - i - 1): 

            if data[j][1] < data[j + 1][1]: 

                temp = data[j]
                data[j] = data[j + 1]
                data[j + 1] = temp

    print("\nSorted using Bubble Sort:")
    display_students(data)

# Insertion Sort 

def insertion_sort(): 

    data = students.copy()

    for i in range(1, len(data)): 

        current = data[i]
        j = i - 1

        while j >= 0 and data[j][1] < current[1]: 

            data[j + 1] = data[j]
            j = j - 1

        data[j + 1] = current

    print("\nSorted using Insertion Sort:")
    display_students(data)

# Merge Function

def merge(left, right): 

    result = []

    while len(left) > 0 and len(right) > 0: 

        if left[0][1] >= right[0][1]:

            result.append(left[0])
            left.pop(0)

        else: 

            result.append(right[0])
            right.pop(0)

    for student in left: 
        result.append(student)

    for student in right: 
        result.append(student)

    return result 

# Merge Sort 

def merge_sort(data): 

    if len(data) <= 1: 
        return data

    mid = len(data) // 2 

    left = data[:mid]
    right = data[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

# Main Menu 

while True: 

    print("\n===== STUDENT MARKS RANKING SYSTEM =====")

    print("1. Add Student")
    print("2. Display Students")
    print("3. Bubble Sort")
    print("4. Insertion Sort")
    print("5. Merge Sort")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1": 
        add_student()

    elif choice == "2": 
        display_students(students)

    elif choice == "3": 
        bubble_sort()

    elif choice == "4": 
        insertion_sort()

    elif choice == "5": 
        sorted_students = merge_sort(students.copy())

        print("\nSorted using Merge Sort:")
        display_students(sorted_students)

    elif choice == "6": 
        print("Thank you!")
        break

    else: 
        print("Invalid choice.")