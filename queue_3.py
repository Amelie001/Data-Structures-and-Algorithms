
class Queue:

    def __init__(self, size):
        self.queue = [None] * size
        self.front = 0
        self.rear = 0
        self.size = size
        self.available = size

    def enqueue(self, order):

        if self.available == 0:
            print("Queue overflow!")

        else:
            self.queue[self.rear] = order
            self.rear = (self.rear + 1) % self.size
            self.available -= 1
            print("Order added successfully!")

    def display_orders(self):

        if self.available == self.size:
            print("No pending orders.")

        else:
            print("\nPending Orders:")

            for i in range(self.size - self.available):
                index = (self.front + i) % self.size
                print(self.queue[index])

    def update_order(self, order_id):

        for i in range(self.size - self.available):
            index = (self.front + i) % self.size
            order = self.queue[index]

            if order[0] == order_id:

                print("1. Update customer")
                print("2. Update product")
                print("3. Update status")

                choice = input("Enter choice: ")

                if choice == "1":
                    order[1] = input("New customer name: ")

                elif choice == "2":
                    order[2] = input("New product: ")

                elif choice == "3":
                    order[3] = input("New status: ")

                else:
                    print("Invalid choice!")
                    return

                print("Order updated successfully!")
                return

        print("Order not found!")

    def delete_order(self, order_id):

        orders = []

        for i in range(self.size - self.available):
            index = (self.front + i) % self.size
            order = self.queue[index]

            if order[0] == order_id:

                if order[3].lower() not in ["cancelled", "dispatched"]:
                    print("Only cancelled or dispatched orders can be deleted!")
                    return

            else:
                orders.append(order)

        if len(orders) == self.size - self.available:
            print("Order not found!")
            return

        self.queue = [None] * self.size
        self.front = 0
        self.rear = 0
        self.available = self.size

        for order in orders:
            self.enqueue(order)

        print("Order deleted successfully!")

    def dequeue(self):

        if self.available == self.size:
            print("Queue underflow!")

        else:
            order = self.queue[self.front]
            order[3] = "Dispatched"

            print("Processing order:", order)

            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size
            self.available += 1

    def peek(self):

        if self.available == self.size:
            print("Queue is empty!")

        else:
            print(self.queue[self.front])


queue1 = Queue(5)

while True:

    print("\nE-COMMERCE ORDER SYSTEM")
    print("1. Add order")
    print("2. Display orders")
    print("3. Update order")
    print("4. Delete order")
    print("5. Process next order")
    print("6. View next order")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        order_id = input("Enter order ID: ")
        customer = input("Enter customer name: ")
        product = input("Enter product: ")

        order = [order_id, customer, product, "Pending"]

        queue1.enqueue(order)

    elif choice == "2":
        queue1.display_orders()

    elif choice == "3":
        order_id = input("Enter order ID to update: ")
        queue1.update_order(order_id)

    elif choice == "4":
        order_id = input("Enter order ID to delete: ")
        queue1.delete_order(order_id)

    elif choice == "5":
        queue1.dequeue()

    elif choice == "6":
        queue1.peek()

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
