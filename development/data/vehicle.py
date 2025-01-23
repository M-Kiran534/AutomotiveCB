# data/vehicle.py

vehicles = []

def add_vehicle(vehicle_id, model, make, year):
    try:
        # Check if vehicle already exists
        if any(vehicle['id'] == vehicle_id for vehicle in vehicles):
            raise ValueError(f"Vehicle with ID {vehicle_id} already exists.")
        
        vehicle = {
            'id': vehicle_id,
            'model': model,
            'make': make,
            'year': year
        }
        vehicles.append(vehicle)
        print(f"Vehicle {model} added successfully.")
    except Exception as e:
        print(f"Error adding vehicle: {e}")

def get_vehicles():
    try:
        if not vehicles:
            raise ValueError("No vehicles found.")
        return vehicles
    except Exception as e:
        print(f"Error retrieving vehicles: {e}")
        return []
