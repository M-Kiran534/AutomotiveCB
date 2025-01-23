# features/vehicle_manager.py

from data.vehicle import add_vehicle, get_vehicles

def add_vehicle_interaction():
    try:
        print("\nAdding a new vehicle:")

        # Ensure vehicle ID is provided
        while True:
            try:
                vehicle_id = int(input("Enter Vehicle ID: "))
                if vehicle_id <= 0:
                    raise ValueError("Vehicle ID must be a positive integer.")
                break
            except ValueError as ve:
                print(f"Invalid input: {ve}. Please try again.")
        
        # Ensure vehicle model is provided
        while True:
            model = input("Enter Vehicle Model: ").strip()
            if not model:
                print("Vehicle model is mandatory. Please enter a valid model.")
            else:
                break

        # Ensure vehicle make is provided
        while True:
            make = input("Enter Vehicle Make: ").strip()
            if not make:
                print("Vehicle make is mandatory. Please enter a valid make.")
            else:
                break
        
        # Ensure vehicle year is provided (optional, but if provided, it should be a valid number)
        while True:
            try:
                year = input("Enter Vehicle Year (optional, leave empty if unknown): ").strip()
                if year and not year.isdigit():
                    raise ValueError("Year must be a valid number.")
                break
            except ValueError as ve:
                print(f"Invalid input: {ve}. Please try again.")

        add_vehicle(vehicle_id, model, make, year)
    except Exception as e:
        print(f"Error: {e}")

def view_vehicles():
    try:
        print("\nList of Vehicles:")
        vehicles = get_vehicles()
        if not vehicles:
            raise ValueError("No vehicles available.")
        
        for vehicle in vehicles:
            print(f"ID: {vehicle['id']}, Model: {vehicle['model']}, Make: {vehicle['make']}, Year: {vehicle['year']}")
    except Exception as e:
        print(f"Error: {e}")
