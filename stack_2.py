# Restaurant manager 

class Restaurant: 

    def __init__(self): 
        self.orders = []

    def add_order(self): 
        order_id = input("Enter order ID: ")
        customer = input("Enter customer name: ")
        food = input("Enter food item: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter total price: "))

        order = {
            "id": order_id,
            "customer": customer,
            "food": food, 
            "quantity": quantity,
            "price": price
        }

        self.orders.append(order)

        print("Order placed successfully!")

    def display_orders(self): 
        if len(self.orders) == 0: 
            print("No pending orders.")

        else: 
            print("\nPending orders:")

            for order in self.orders: 
                print("\nOrder ID:", order["id"])
                print("Customer:", order["customer"])
                print("Food:", order["food"])
                print("Quantity:", order["quantity"])
                print("Total price:", order["price"])

    def view_latest_order(self): 
        if len(self.orders) == 0: 
            print("No orders available.")

        else: 
            print("Latest order:")
            print(self.orders[-1])

    def update_order(self): 
        if len(self.orders) == 0: 
            print("No orders available.")

        else: 
            order = self.orders[-1]

            order["food"] = input("Enter updated food item: ")
            order["quantity"] = int(input("Enter updated quantity: "))
            order["price"] = float(input("Enter updated price: "))

            print("Order updated successfully!")

    def prepare_order(self): 
        if len(self.orders) == 0: 
            print("No orders to prepare.")

        else: 
            order = self.orders.pop()

            print("\nOrder prepared successfully!")
            print("Order ID:", order["id"])
            print("Customer:", order["customer"])
            print("Food:", order["food"])

restaurant = Restaurant()

while True: 

    print("\n--- RESTAURANT ORDER MANAGER ---")
    print("1. Add order")
    print("2. Display orders")
    print("3. View latest order")
    print("4. Update latest order")
    print("5. Prepare latest order")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1": 
        restaurant.add_order()

    elif choice == "2": 
        restaurant.display_orders()

    elif choice == "3": 
        restaurant.view_latest_order()

    elif choice == "4": 
        restaurant.update_order()

    elif choice == "5": 
        restaurant.prepare_order()

    elif choice == "6": 
        break

    else: 
        print("Invalid choice.")