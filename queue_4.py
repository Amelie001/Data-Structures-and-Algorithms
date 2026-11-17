# Library Book Reservation Queue 

class Reservation: 

    def __init__(self): 
        self.reservations = []

    def add_reservation(self): 
        student_id = input("Enter student ID: ")
        book_title = input("Enter book title: ")

        self.reservations.append({
            "id": student_id, "book_title": book_title 
        })

        print("Reservation added successfully!")

    def display(self): 
        if not self.reservations: 
            print("No books found.")

        for s in self.reservations:
            print(s)

    def update(self): 
        student_id = input("Enter student ID to update: ")

        for s in self.reservations: 
            if s["id"] == student_id: 
                s["book_title"] = input("New book title: ")

                print("Book updated.")
                return

    def delete(self): 
        student_id = input("Enter student ID to delete: ")

        for s in self.reservations: 
            if s["id"] == student_id: 
                self.reservations.remove(s)
                print("Reservation removed.")
                return

        print("Reservation not found.")

    def dequeue(self): 
        if self.reservations: 
            print("Next reservation:", self.reservations.pop(0))

        else:
            print("No reservations found.")

    def peek(self): 
        if self.reservations: 
            print("Next reservation:", self.reservations[0])

        else:
            print("No reservations found.")

    def menu(self):
        while True: 
            print("\n1. Add \n2. Display \n3. Update \n4. Delete \n5. Dequeue \n6. Peek \n7. Exit")

            choice = input("Enter choice: ")

            if choice == "1": 
                self.add_reservation()

            elif choice == "2":
                self.display()

            elif choice == "3": 
                self.update()

            elif choice == "4": 
                self.delete()

            elif choice == "5": 
                self.dequeue()

            elif choice == "6": 
                self.peek()

            elif choice == "7":
                break

            else:
                print("Invalid choice.")

book = Reservation()
book.menu()