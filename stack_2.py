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