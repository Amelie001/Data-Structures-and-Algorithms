# Vehicle Rental System

from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, vehicle_id, brand, model, price_per_day):
        self.__vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.price_per_day = price_per_day
        self.__is_rented = False

    def get_vehicle_id(self):
        return self.__vehicle_id

    def get_rental_status(self):
        return self.__is_rented

    def rent_vehicle(self):
        if not self.__is_rented:
            self.__is_rented = True
            print("Vehicle rented successfully!")
        else:
            print("Vehicle is already rented.")

    def return_vehicle(self):
        if self.__is_rented:
            self.__is_rented = False
            print("Vehicle returned successfully!")
        else:
            print("Vehicle is not currently rented.")

    @abstractmethod
    def calculate_rental_cost(self, days):
        pass

    def display_details(self):
        print("Vehicle ID:", self.__vehicle_id)
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price per day: £", self.price_per_day)

        if self.__is_rented:
            print("Status: Rented")
        else:
            print("Status: Available")


class Car(Vehicle):

    def calculate_rental_cost(self, days):
        return self.price_per_day * days


class Bike(Vehicle):

    def calculate_rental_cost(self, days):
        return self.price_per_day * days * 0.8


class Scooter(Vehicle):

    def calculate_rental_cost(self, days):
        return self.price_per_day * days * 0.7


vehicles = []


def add_vehicle():

    print("\n----- ADD VEHICLE -----")
    print("1. Car")
    print("2. Bike")
    print("3. Scooter")

    vehicle_type = input("Choose vehicle type: ")

    vehicle_id = input("Enter vehicle ID: ")
    brand = input("Enter brand: ")
    model = input("Enter model: ")

    try:
        price = float(input("Enter price per day: £"))

        if price <= 0:
            raise ValueError

    except ValueError:
        print("Please enter a valid positive price.")
        return

    if vehicle_type == "1":
        vehicle = Car(vehicle_id, brand, model, price)

    elif vehicle_type == "2":
        vehicle = Bike(vehicle_id, brand, model, price)

    elif vehicle_type == "3":
        vehicle = Scooter(vehicle_id, brand, model, price)

    else:
        print("Invalid vehicle type.")
        return

    vehicles.append(vehicle)

    print("Vehicle added successfully!")


def view_vehicles():

    if len(vehicles) == 0:
        print("No vehicles available.")
        return

    print("\n----- VEHICLES -----")

    for vehicle in vehicles:
        vehicle.display_details()
        print("--------------------")


def find_vehicle(vehicle_id):

    for vehicle in vehicles:

        if vehicle.get_vehicle_id() == vehicle_id:
            return vehicle

    return None


def rent_vehicle():

    vehicle_id = input("Enter vehicle ID: ")

    vehicle = find_vehicle(vehicle_id)

    if vehicle is None:
        print("Vehicle not found.")
        return

    if vehicle.get_rental_status():
        print("Vehicle is already rented.")
        return

    try:
        days = int(input("How many days would you like to rent it? "))

        if days <= 0:
            raise ValueError

    except ValueError:
        print("Please enter a valid number of days.")
        return

    cost = vehicle.calculate_rental_cost(days)

    print("Estimated rental cost: £", round(cost, 2))

    vehicle.rent_vehicle()


def return_vehicle():

    vehicle_id = input("Enter vehicle ID: ")

    vehicle = find_vehicle(vehicle_id)

    if vehicle is None:
        print("Vehicle not found.")
        return

    vehicle.return_vehicle()


def delete_vehicle():

    vehicle_id = input("Enter vehicle ID: ")

    vehicle = find_vehicle(vehicle_id)

    if vehicle is None:
        print("Vehicle not found.")
        return

    if vehicle.get_rental_status():
        print("You cannot delete a vehicle that is currently being rented.")
        return

    vehicles.remove(vehicle)

    print("Vehicle deleted successfully!")


while True:

    print("\n===== VEHICLE RENTAL SYSTEM =====")
    print("1. Add Vehicle")
    print("2. View Vehicles")
    print("3. Rent Vehicle")
    print("4. Return Vehicle")
    print("5. Delete Vehicle")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_vehicle()

    elif choice == "2":
        view_vehicles()

    elif choice == "3":
        rent_vehicle()

    elif choice == "4":
        return_vehicle()

    elif choice == "5":
        delete_vehicle()

    elif choice == "6":
        print("Thank you for using the Vehicle Rental System!")
        break

    else:
        print("Invalid choice. Please try again.")