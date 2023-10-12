from parking_lot import ParkingLot
from utils import check_string


class ParkingManager:
    def __init__(self):
        print("Welcome to the Parking Lot Management System")
        self.levels = ['A', 'B']
        self.parking_lot = ParkingLot(self.levels)

    def run(self):
        while True:
            print("\nChoose an option:")
            print("1. Assign Parking Space")
            print("2. Retrieve Parking Spot")
            print("3. Print Parking Status")
            print("4. Exit")
            print("5. Levelup")
            choice = input("Enter your choice: ")

            if choice == '1':
                vehicle_number = input("Enter the vehicle number: ")
                if check_string(vehicle_number):
                    result = self.parking_lot.assign_parking_space(vehicle_number)
                    print("Duplicate vehicle found" if result is False else f"Assigned parking spot: {result}")
                else:
                    print(" invalid vehicle number")

            elif choice == '2':
                vehicle_number = input("Enter the vehicle number: ")
                result = self.parking_lot.retrieve_parking_spot(vehicle_number)
                if result:
                    print("retrieving your vehicle from:", result)
                else:
                    print("Vehicle not found in the parking lot")

            elif choice == '3':
                self.parking_lot.print_parking_status()

            elif choice == '4':
                print("Exiting the application.")
                break

            elif choice == '5':
                value = input("Enter the new level name: ")
                if value in self.levels:
                    print("Level already exists")
                else:
                    self.levels.append(value.upper())
                    self.parking_lot.update_level_slots(value.upper())
                    print(f"Added new level: {value}")
                    print(self.levels)

            else:
                print("Invalid choice. Please select a valid option")