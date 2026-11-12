# Customer Support Ticket Manager 

class CustomerSupportTicket: 

    def __init__(self): 
        self.complaints = []

    def add_ticket(self): 
        ticket_id = input("Enter ticket ID: ")
        customer_name = input("Enter customer name: ")
        issue_description = input("Enter issue description: ")
        priority = input("Enter priority: ")

        complaint = {
            "id": ticket_id, 
            "customer": customer_name,
            "issue description": issue_description, 
            "priority": priority
        }

        self.complaints.append(complaint)

        print("Complaint stored successfully!")

    def display_tickets(self):
        if len(self.complaints) == 0: 
            print("No complaints stored.")

        else: 
            print("\nStored complaints:")

            for complaint in self.complaints:
                print("\nTicket ID:", complaint["id"])
                print("Customer:", complaint["customer"])
                print("Issue description:", complaint["issue description"])
                print("Priority:", complaint["priority"])

    def update_ticket(self): 
        if len(self.complaints) == 0: 
            print("No complaints stored.")

        else: 
            latest = self.complaints[-1]

            latest["customer"] = input("Enter new customer name: ")
            latest["issue description"] = input("Enter new issue description: ")
            latest["priority"] = input("Enter new priority: ")

            print("Ticket updated successfully!")

    def resolve_ticket(self):
        if len(self.complaints) == 0:
            print("No complaints to resolve.")

        else:
            resolved = self.complaints.pop()

            print("Ticket resolved successfully!")
            print("Resolved ticket:", resolved["id"])

    def view_latest_ticket(self):
        if len(self.complaints) == 0:
            print("No complaints stored.")

        else:
            latest = self.complaints[-1]

            print("\nLatest Ticket:")
            print("Ticket ID:", latest["id"])
            print("Customer:", latest["customer"])
            print("Issue description:", latest["issue description"])
            print("Priority:", latest["priority"])


manager = CustomerSupportTicket()

while True:
    print("\nCustomer Support Ticket Manager")
    print("1. Add Ticket")
    print("2. Display All Tickets")
    print("3. Update Latest Ticket")
    print("4. Resolve Latest Ticket")
    print("5. View Latest Ticket")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        manager.add_ticket()

    elif choice == "2":
        manager.display_tickets()

    elif choice == "3":
        manager.update_ticket()

    elif choice == "4":
        manager.resolve_ticket()

    elif choice == "5":
        manager.view_latest_ticket()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")