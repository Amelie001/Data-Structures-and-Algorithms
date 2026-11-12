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
