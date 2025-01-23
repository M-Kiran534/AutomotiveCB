import csv
import json
from data.vehicle import get_vehicles
from data.maintenance import get_maintenance_records

def export_data_to_csv(filename):
    vehicles = get_vehicles()
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Vehicle ID", "Make", "Model", "Year", "Mileage"])
        for vehicle in vehicles:
            writer.writerow([vehicle["id"], vehicle["make"], vehicle["model"], vehicle["year"], vehicle["mileage"]])
    print(f"Data exported to {filename} successfully!")

def export_data_to_json(filename):
    vehicles = get_vehicles()
    maintenance_records = {vehicle["id"]: get_maintenance_records(vehicle["id"]) for vehicle in vehicles}
    with open(filename, "w") as jsonfile:
        json.dump({"vehicles": vehicles, "maintenance": maintenance_records}, jsonfile, indent=4)
    print(f"Data exported to {filename} successfully!")
