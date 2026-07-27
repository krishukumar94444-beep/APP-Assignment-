class Vehicle:
    def __init__(self, vehicle_number, brand, price):
        self.vehicle_number = vehicle_number
        self.brand = brand
        self.price = price

    def category(self):
        if self.price >= 1000000:
            return "Luxury"
        else:
            return "Economy"

    def display(self):
        print("Vehicle Number :", self.vehicle_number)
        print("Brand          :", self.brand)
        print("Price          :", self.price)
        print("Category       :", self.category())
        print("-" * 30)


class Showroom:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print("Vehicle Added Successfully!\n")

    def display_vehicles(self):
        if len(self.vehicles) == 0:
            print("No vehicles available.")
        else:
            print("\n--- Vehicle Details ---")
            for vehicle in self.vehicles:
                vehicle.display()


# Main Program
showroom = Showroom()

while True:
    print("\n===== Vehicle Showroom Management System =====")
    print("1. Add Vehicle")
    print("2. Display All Vehicles")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        number = input("Enter Vehicle Number: ")
        brand = input("Enter Brand: ")
        price = float(input("Enter Price: "))

        vehicle = Vehicle(number, brand, price)
        showroom.add_vehicle(vehicle)

    elif choice == 2:
        showroom.display_vehicles()

    elif choice == 3:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
  Comment:-
  Vehicle Showroom Management System 
1. Add Vehicle
2. Display All Vehicles
3. Exit
Enter your choice: 1

Enter Vehicle Number: MH12AB1234
Enter Brand: BMW
Enter Price: 6500000
Vehicle Added Successfully!

   Vehicle Showroom Management System 
1. Add Vehicle
2. Display All Vehicles
3. Exit
Enter your choice: 2

    Vehicle Details 
Vehicle Number : MH12AB1234
Brand          : BMW
Price          : 6500000.0
Category       : Luxury
