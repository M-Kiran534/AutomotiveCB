import json

VEHICLE_FILE = "vehicles.json"

def load_vehicles():
    try:
        with open(VEHICLE_FILE, "r") as f:
            data = json.load(f)
            if not isinstance(data, list):  # Ensure the data is a list
                return []
            return data
    except FileNotFoundError:
        return []  # If the file does not exist, return an empty list
    except json.JSONDecodeError:
        return []  # If the file is corrupted, return an empty list

def save_vehicles(vehicles):
    if not isinstance(vehicles, list):
        raise ValueError("The vehicles data must be a list.")
    with open(VEHICLE_FILE, "w") as f:
        json.dump(vehicles, f, indent=4)

def add_vehicle(vehicle_data):
    vehicles = load_vehicles()
    vehicles.append(vehicle_data)  # Add the new vehicle to the list
    save_vehicles(vehicles)        # Save the updated list back to the file

def get_vehicles():
    return load_vehicles()

def remove_vehicle(vehicle_id):
    vehicles = load_vehicles()
    vehicles = [v for v in vehicles if v["id"] != vehicle_id]
    save_vehicles(vehicles)
