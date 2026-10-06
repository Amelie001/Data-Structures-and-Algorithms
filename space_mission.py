# Space Mission Simulator 

from abc import ABC, abstractmethod 
import random 

class CrewMember(ABC): 

    def __init__(self, crew_id, name, age): 
        self.crew_id = crew_id 
        self.name = name 
        self.age = age 

    @abstractmethod 
    def perform_duty(self): 
        pass

    @abstractmethod
    def get_role(self): 
        pass 

    def display_info(self): 
        print("-----------------------------")
        print("Crew ID:", self.crew_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Role:", self.get_role())

class Astronaut(CrewMember): 

    def get_role(self): 
        return "Astronaut"

    def perform_duty(self): 
        print(self.name, "is exploring the planet.")

class Engineer(CrewMember): 

    def get_role(self): 
        return "Engineer"

    def perform_duty(self): 
        print(self.name, "is checking and repairing the spacecraft.")

class Scientist(CrewMember): 

    def get_role(self): 
        return "Scientist"

    def perform_duty(self): 
        print(self.name, "is collecting and analyzing scientific data.")

class Doctor(CrewMember): 

    def get_role(self): 
        return "Doctor"

    def perform_duty(self): 
        print(self.name, "is checking the health of the crew.")

class Spacecraft: 

    def __init__(self): 
        self.__oxygen = 100
        self.__fuel = 100
        self.__food = 100 
        self.__hull = 100 

    def get_oxygen(self): 
        return self.__oxygen 

    def get_fuel(self): 
        return self.__fuel 

    def get_food(self): 
        return self.__food 

    def get_hull(self): 
        return self.__hull 

    def display_status(self): 
        print("\n===============================")
        print("      SPACECRAFT STATUS")
        print("==============================")
        print("Oxygen:", self.__oxygen, "%")
        print("Fuel:", self.__fuel, "%")
        print("Hull:", self.__hull, "%")
        print("=============================")

    def reduce_oxygen(self, amount): 
        self.__oxygen -= amount 
        if self.__oxygen < 0: 
            self.__oxygen = 0 

    def reduce_fuel(self, amount): 
        self.__fuel -= amount 
        if self.__fuel < 0: 
            self.__fuel = 0

    def reduce_food(self, amount): 
        if self.__food < 0: 
            self.__food = 0

    def damage_hull(self, amount): 
        self.__hull -= amount 
        if self.__hull < 0: 
            self.__hull = 0

    def repair_hull(self, amount): 
        self.__hull += amount 
        if self.__hull > 100: 
            self.__hull = 100

    def is_mission_over(self): 

        if self.__oxygen <= 0: 
            return True 

        if self.__fuel <= 0: 
            return True

        if self.__food <= 0: 
            return True 

        if self.__hull <= 0: 
            return True 

        return False 

class Mission: 

    def __init__(self): 
        self.crew_members = []
        self.spacecraft = Spacecraft()
        self.day = 1 

    def add_crew_member(self):

        print("\n===== ADD CREW MEMBER =====")

        try: 

            crew_id = int(input("Enter crew ID: "))

            for member in self.crew_members: 

                if member.crew_id == crew_id: 
                    print("Crew ID already exists!")
                    return

            name = input("Enter name: ")

            age = int(input("Enter age: "))

            if age <= 0: 
                raise ValueError("Age must be greater than 0.")

            print("\nChoose role:")
            print("1. Astronaut")
            print("2. Engineer")
            print("3. Scientist")
            print("4. Doctor")

            role = input("Enter choice: ")

            if role == "1":
                member = Astronaut(crew_id, name, age)

            elif role == "2": 
                member = Engineer(crew_id, name, age)

            elif role == "3": 
                member = Scientist(crew_id, name, age)

            elif role == "4": 
                member - Doctor(crew_id, name, age)

            else: 
                raise ValueError("Invalid role.")

            self.crew_members.append(member)

            print("\nCrew member added successfully!")

        except ValueError as e: 
            print("Error:", e)

    def view_crew(self): 

        print("\n===== CREW MEMBERS =====")

        if len(self.crew_members) == 0: 

            print("No crew mambers found.")
            return 

        for member in self.crew_members: 

            member.display_info()

    def find_crew_member(self, crew_id): 

        for member in self.crew_members: 

            if member.crew_id == crew_id: 
                return member 

        return None

    def update_crew_member(self): 

        print("\n===== UPDATE CREW MEMBER =====")

        try: 

            crew_id = int(input("Enter crew ID to update: "))
            member = self.find_crew_member(crew_id)

            if member is None: 
                raise ValueError("Crew member not found.")

            print("\nCurrent details:")
            member.display_info()
            new_name = input("\nEnter new name: ")
            new_age = int(input("Enter new age: "))

            if new_age <= 0: 
                raise ValueError("Age must be greater than 0.")

            member.name = new_name 
            member.age = new_age
            print("\nCrew member updated successfully!")

        except