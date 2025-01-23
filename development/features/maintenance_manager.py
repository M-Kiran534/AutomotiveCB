# features/maintenance_manager.py

from data.maintenance import add_maintenance, get_maintenance_records

def add_maintenance_interaction(vehicle_id):
    try:
        print(f"\nAdding maintenance record for Vehicle ID {vehicle_id}:")
        date = input("Enter Maintenance Date (YYYY-MM-DD): ")
        description = input("Enter Maintenance Description: ")
        cost = float(input("Enter Maintenance Cost: "))

        add_maintenance(vehicle_id, date, description, cost)
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"Error: {e}")

def view_maintenance_interaction(vehicle_id):
    try:
        print(f"\nMaintenance Records for Vehicle ID {vehicle_id}:")
        records = get_maintenance_records(vehicle_id)
        
        if not records:
            raise ValueError(f"No maintenance records found for Vehicle ID {vehicle_id}.")
        
        for record in records:
            print(f"Date: {record['date']}, Description: {record['description']}, Cost: {record['cost']}")
    except Exception as e:
        print(f"Error: {e}")
