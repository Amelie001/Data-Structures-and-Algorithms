# Library Management System

books = ["1984", "Never Let Me Go", "The Maze Runner", "Animal Farm", "Farenheit 451"]

while True: 

    book_title = input("Enter a book title: ")

    found = False 

    for i in range(len(books)): 
        if books[i] == book_title: 
            print("Book found at index:", i)
            found = True 
            break

    if found == False: 
        print("Book not available.")