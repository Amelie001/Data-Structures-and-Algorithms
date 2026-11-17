# Hospital Management 

class HospitalQueue: 

    def __init__(self): 
        self.queue = []

    def add_patient(self): 
        pid = input("Enter patient ID: ")
        name = input("Enter patient name: ")
        symptoms = input("Enter symptoms: ")

        self.queue.append({
            "id": pid, "name": name, "symptoms": symptoms
        })

        print("Patient added.")

    def display(self): 
        if not self.queue: 
            print("No patients waiting.")

        for p in self.queue: 
            print(p)

    def search(self): 
        pid = input("Enter patient ID: ")

        for p in self.queue: 
            if p["id"] == pid: 
                print(p)
                return

        print("Patient not found.")

    def update(self): 
        pid = input("Enter patient ID to update: ")

        for p in self.queue: 
            if p["id"] == pid: 
                p["name"] = input("New name: ")
                p["symptoms"] = input("New symptoms: ")

                print("Patient updated.")
                return

        print("Patient not found.")

    def delete(self): 
        pid = input("Enter patient ID to delete: ")

        for p in self.queue: 
            if p["id"] == pid: 
                self.queue.remove(p)
                print("Patient deleted.")
                return

        print("Patient not found.")

    def dequeue(self): 
        if self.queue:
            print("Next patient:", self.queue.pop(0))

        else: 
            print("Queue is empty.")

    def peek(self):
        if self.queue:
            print("Next patient:", self.queue[0])

        else: 
            print("Queue is empty.")

    def menu(self): 
        while True:
            print("\n1. Add  2. Display  3. Search  4. Update")
            print("5. Delete by ID  6. Call next  7. Peek  8. Exit")
            choice = input("Enter choice: ")

            if choice == "1": 
                self.add_patient()

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

app = HospitalQueue()
app.menu()