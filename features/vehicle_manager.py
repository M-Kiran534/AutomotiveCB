from data.vehicle import add_vehicle, get_vehicles, remove_vehicle

def add_vehicle_interaction():
    make = input("Enter vehicle make: ")
    model = input("Enter vehicle model: ")
    year = input("Enter vehicle year: ")
    mileage = input("Enter vehicle mileage: ")
    vehicle = {"id": len(get_vehicles()) + 1, "make": make, "model": model, "year": year, "mileage": mileage}
    add_vehicle(vehicle)
    print("Vehicle added successfully!")

def view_vehicles():
    vehicles = get_vehicles()
    if not vehicles:
        print("No vehicles found.")
        return
    for v in vehicles:
        print(f"ID: {v['id']}, Make: {v['make']}, Model: {v['model']}, Year: {v['year']}, Mileage: {v['mileage']}")
