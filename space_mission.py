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

        except ValueError as e: 

            print("Error:", e)

    def delete_crew_member(self): 

        print("\n===== DELETE CREW MEMBER =====")

        try: 

            crew_id = int(input("Enter crew ID to delete: "))
            member = self.find_crew_member(crew_id)

            if member is None: 
                raise ValueError("Crew member not found.")

            self.crew_members.remove(member)
            print("\nCrew member deleted successfully!")

        except ValueError as e: 

            print("Error:", e)

    def perform_crew_duties(self): 

        print("\n===== CREW DUTIES =====")

        if len(self.crew_members) == 0:
            print("No crew members available.")
            return 

        for member in self.crew_members: 
            member.perform_duty()

    def random_event(self): 

        events = [
            "Solar Storm",
            "Oxygen Leak",
            "Meteor Shower", 
            "Normal Day",
            "Equipment Failure", 
            "Food Supply Problem"
        ]

        event = random.choice(events)

        print("\n========================================")
        print("             MISSION EVENT") 
        print("========================================")

        print("Event:", event)

        if event == "Solar Storm": 
            print("A powerful solar storm is approaching!")

            self.spacecraft.damage_hull(15)
            self.spacecraft.reduce_fuel(5)

            print("Hull damaged by 15%.")
            print("Fuel reduced by 5%.")

        elif event == "Oxygen Leak": 
            print("WARNING! Oxygen leak detected!")

            self.spacecraft.reduce_oxygen(20)
            print("Oxygen reduced by 20%.")

        elif event == "Meteor Shower": 
            print("A meteor shower has hit the spacecraft!")

            self.spacecraft.damage_hull(20)
            print("Hull damaged by 20%.")

        elif event == "Normal Day": 
            print("Everything is normal today.")

            self.spacecraft.reduce_food(5)
            self.spacecraft.reduce_oxygen(5)

        elif event == "Equipment Failure": 
            print("A piece of equipment has stopped working.")

            self.spacecraft.damage_hull(10)
            print("Hull damaged by 10%.")

        elif event == "Food Supply Problem": 
            print("Food storage system malfunction!")

            self.spacecraft.reduce_food(15)
            print("Food reduced by 15%.")

    def start_day(self): 

        print("\n=======================================")
        print("             DAY", self.day)
        print("=======================================")

        if len(self.crew_members) == 0: 
            print("There are no crew members!")
            print("Add crew members before starting the mission.")
            return 

        self.spacecraft.reduce_oxygen(5)
        self.spacecraft.reduce_food(5)
        self.spacecraft.reduce_fuel(3)

        print("\nResources consumed.")

        self.random_event()

        print("\n===== CREW ACTIVITIES =====")

        self.perform_crew_duties()
        self.spacecraft.display_status()
        self.day += 1

        if self.spacecraft.is_mission_over(): 
            print("\n===============================")
            print("         MISSION FAILED")
            print("===============================")
            print("One or more spacecraft resources")
            print("have reached zero.")

        else: 
            print("\nMission continues successfully!")

    def save_mission(self): 

        try: 

            with open("mission_log.txt", "w") as file: 
                file.write("===== SPACE MISSION LOG =====\n\n")
                file.write("Current Mission Day: ")
                file.write(str(self.day))
                file.write("\n\n")
                file.write("===== CREW =====\n")

                for member in self.crew_members: 
                    file.write(
                        str(member.crew_id)
                        + ","
                        + member.name
                        + ","
                        + member.get_role()
                        + ","
                        + str(member.age)
                        + "\n"
                    )

                file.write("\n===== SPACECRAFT =====\n")
                file.write("Oxygen: " + str(self.spacecraft.get_oxygen()) + "%\n")
                file.write("Fuel: " + str(self.spacecraft.get_fuel()) + "%\n")
                file.write("Food: " + str(self.spacecraft.get_food()) + "%\n")
                file.write("Hull: " + str(self.spacecraft.get_hull()) + "%\n")

            print("\n Mission saved successfully!")

        except OSError as e: 

            print("Error while saving mission:", e)

    def load_mission(self): 

        try: 

            with open("mission_data.txt", "r") as file: 
                data = file.readlines()

            self.crew_members.clear()

            for line in data: 
                line = line.strip()

                if line == "": 
                    continue

                if line.startswith("#"): 
                    continue 

                parts = line.split(",")

                if len(parts) != 4: 
                    continue 

                crew_id = int(parts[0])
                name = parts[1]
                role = parts[2]
                age = int(parts[3])

                if role == "Astronaut": 
                    member = Astronaut(crew_id, name, age)

                elif role == "Engineer": 
                    member = Engineer(crew_id, name, age)

                elif role == "Scientist": 
                    member = Scientist(crew_id, name, age)

                elif role == "Doctor": 
                    member = Doctor(crew_id, name, age)

                else: 
                    continue 

                self.crew_members.append(member)

            print("\nMission data loaded successfully!")

        except FileNotFoundError: 
            print("\nmission_data.txt was not found.")

        except ValueError: 
            print("\nInvalid data found in the file.")

    def view_mission_log(self): 

        print("\n===== MISSION LOG =====")

        try: 

            with open("mission_log.txt", "r") as file: 
                data = file.read()

                if data.strip() == "": 
                    print("Mission log is empty.")

                else: 
                    print(data)

        except FileNotFoundError: 
            print("No mission log exists yet.")

        except OSError as e: 
            print("Could not read file:", e)

def main(): 

    mission = Mission()

    print("==================================================")
    print("            SPACE MISSION SIMULATOR")
    print("==================================================")
    print("\nLoading existing misison data...")

    mission.load_mission()

    while True: 
        print("\n")
        print("===============================================")
        print("                 MAIN MENU")
        print("===============================================")
        print("1. Add Crew Member")
        print("2. View Crew Member")
        print("3. Update Crew Member")
        print("4. Delete Crew Member")
        print("5. Perform Crew Duties")
        print("6. Start Next Mission Day")
        print("7. View Spacecraft Status")
        print("8. Save Mission")
        print("9. View Mission Log")
        print("10. Exit")