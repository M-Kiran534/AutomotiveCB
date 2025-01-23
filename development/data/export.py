# data/export.py

import csv
import json
from data.vehicle import vehicles

def export_data_to_csv(filename):
    try:
        if not vehicles:
            raise ValueError("No vehicles to export.")
        
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'model', 'make', 'year'])
            writer.writeheader()
            for vehicle in vehicles:
                writer.writerow(vehicle)
        print(f"Data successfully exported to {filename}")
    except Exception as e:
        print(f"Error exporting data to CSV: {e}")

def export_data_to_json(filename):
    try:
        if not vehicles:
            raise ValueError("No vehicles to export.")
        
        with open(filename, mode='w') as file:
            json.dump(vehicles, file, indent=4)
        print(f"Data successfully exported to {filename}")
    except Exception as e:
        print(f"Error exporting data to JSON: {e}")
