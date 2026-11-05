
products = []

def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))

    products.append([name, price])

    print("Product added successfully!")

def display_products(data):

    if len(data) == 0:
        print("No products found.")
    else:
        print("\nAvailable Products:")

        for product in data:
            print(product[0], "- £", format(product[1], ".2f"))

def bubble_sort():

    data = products.copy()
    n = len(data)

    for i in range(n):

        for j in range(n - i - 1):

            if data[j][1] > data[j + 1][1]:

                temp = data[j]
                data[j] = data[j + 1]
                data[j + 1] = temp

    print("\nSorted using Bubble Sort:")
    display_products(data)

def insertion_sort():

    data = products.copy()

    for i in range(1, len(data)):

        current = data[i]
        j = i - 1

        while j >= 0 and data[j][1] > current[1]:

            data[j + 1] = data[j]
            j = j - 1

        data[j + 1] = current

    print("\nSorted using Insertion Sort:")
    display_products(data)

def merge(left, right):

    result = []

    while len(left) > 0 and len(right) > 0:

        if left[0][1] <= right[0][1]:

            result.append(left[0])
            left.pop(0)

        else:

            result.append(right[0])
            right.pop(0)

    for product in left:
        result.append(product)

    for product in right:
        result.append(product)

    return result

def merge_sort(data):

    if len(data) <= 1:
        return data

    mid = len(data) // 2

    left = data[:mid]
    right = data[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def cheapest_product():

    if len(products) == 0:
        print("No products found.")
    else:
        cheapest = products[0]

        for product in products:

            if product[1] < cheapest[1]:
                cheapest = product

        print("\nCheapest Product:")
        print(cheapest[0], "- £", format(cheapest[1], ".2f"))

def most_expensive_product():

    if len(products) == 0:
        print("No products found.")
    else:
        expensive = products[0]

        for product in products:

            if product[1] > expensive[1]:
                expensive = product

        print("\nMost Expensive Product:")
        print(expensive[0], "- £", format(expensive[1], ".2f"))

while True:

    print("\n===== Online Shopping Price Comparison System =====")

    print("1. Add Product")
    print("2. Display Products")
    print("3. Bubble Sort")
    print("4. Insertion Sort")
    print("5. Merge Sort")
    print("6. Cheapest Product")
    print("7. Most Expensive Product")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        display_products(products)

    elif choice == "3":
        bubble_sort()

    elif choice == "4":
        insertion_sort()

    elif choice == "5":
        sorted_products = merge_sort(products.copy())

        print("\nSorted using Merge Sort:")
        display_products(sorted_products)

    elif choice == "6":
        cheapest_product()

    elif choice == "7":
        most_expensive_product()

    elif choice == "8":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")