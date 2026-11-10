
employees = []

def add_employee():

    name = input("Enter employee name: ")
    salary = float(input("Enter monthly salary: "))

    if salary >= 0:
        employees.append([name, salary])
        print("Employee added successfully!")
    else:
        print("Salary cannot be negative.")

def display_employees(data):

    if len(data) == 0:
        print("No employee records found.")

    else:
        print("\nEmployee Records:")

        for employee in data:
            print(employee[0], "-", employee[1])

def bubble_sort():

    data = employees.copy()
    n = len(data)

    for i in range(n):

        for j in range(n - i - 1):

            if data[j][1] < data[j + 1][1]:

                temp = data[j]
                data[j] = data[j + 1]
                data[j + 1] = temp

    print("\nSorted using Bubble Sort:")
    display_employees(data)

def insertion_sort():

    data = employees.copy()

    for i in range(1, len(data)):

        key = data[i]
        j = i - 1

        while j >= 0 and data[j][1] < key[1]:

            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

    print("\nSorted using Insertion Sort:")
    display_employees(data)

def merge_sort(data):

    if len(data) <= 1:
        return data

    mid = len(data) // 2

    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])

    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i][1] >= right[j][1]:

            result.append(left[i])
            i += 1

        else:

            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def display_merge_sort():

    data = merge_sort(employees.copy())

    print("\nSorted using Merge Sort:")
    display_employees(data)

def highest_salary():

    if len(employees) == 0:
        print("No employee records found.")

    else:
        highest = max(employees, key=lambda x: x[1])

        print("\nEmployee with Highest Salary:")
        print(highest[0], "-", highest[1])

def lowest_salary():

    if len(employees) == 0:
        print("No employee records found.")

    else:
        lowest = min(employees, key=lambda x: x[1])

        print("\nEmployee with Lowest Salary:")
        print(lowest[0], "-", lowest[1])

while True:

    print("\nEmployee Salary Management System")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Bubble Sort")
    print("4. Insertion Sort")
    print("5. Merge Sort")
    print("6. Highest Salary")
    print("7. Lowest Salary")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        display_employees(employees)

    elif choice == "3":
        bubble_sort()

    elif choice == "4":
        insertion_sort()

    elif choice == "5":
        display_merge_sort()

    elif choice == "6":
        highest_salary()

    elif choice == "7":
        lowest_salary()

    elif choice == "8":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")