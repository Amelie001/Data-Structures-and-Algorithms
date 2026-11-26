# Restaurant Order Processing System

class RestaurantQueue:

    def __init__(self):
        self.queue = []

    def add_order(self):
        oid = input("Enter order ID: ")
        dish = input("Enter dish: ")
        quantity = int(input("Enter quantity: "))

        for order in self.queue:
            if order["id"] == oid:
                print("Order ID already exists.")
                return

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return

        self.queue.append({
            "id": oid, "dish": dish, "quantity": quantity
        })

        print("Order added.")

    def display(self):
        if not self.queue:
            print("No pending orders.")
            return

        for order in self.queue:
            print(order)

    def search(self):
        oid = input("Enter order ID: ")

        for order in self.queue:
            if order["id"] == oid:
                print(order)
                return

        print("Order not found.")

    def update(self):
        oid = input("Enter order ID to update: ")

        for order in self.queue:
            if order["id"] == oid:
                dish = input("Enter new dish: ")
                quantity = int(input("Enter new quantity: "))

                if quantity <= 0:
                    print("Quantity must be greater than 0.")
                    return

                order["dish"] = dish
                order["quantity"] = quantity

                print("Order updated.")
                return

        print("Order not found.")

    def delete(self):
        oid = input("Enter order ID to delete: ")

        for order in self.queue:
            if order["id"] == oid:
                self.queue.remove(order)
                print("Order deleted.")
                return

        print("Order not found.")

    def dequeue(self):
        if self.queue:
            print("Preparing order:", self.queue.pop(0))

        else:
            print("Queue is empty.")

    def peek(self):
        if self.queue:
            print("Next order:", self.queue[0])

        else:
            print("Queue is empty.")

    def menu(self):
        while True:
            print("\n1. Add Order \n2. Display Orders \n3. Search Order \n4. Update Order \n5. Delete Order \n6. Prepare Next Order \n7. Peek \n8. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.add_order()

            elif choice == "2":
                self.display()

            elif choice == "3":
                self.search()

            elif choice == "4":
                self.update()

            elif choice == "5":
                self.delete()

            elif choice == "6":
                self.dequeue()

            elif choice == "7":
                self.peek()

            elif choice == "8":
                break

            else:
                print("Invalid choice.")

app = RestaurantQueue()
app.menu()