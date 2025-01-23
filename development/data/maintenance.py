# data/maintenance.py

maintenance_records = []

def add_maintenance(vehicle_id, date, description, cost):
    try:
        # Validate cost
        if cost < 0:
            raise ValueError("Cost cannot be negative.")
        
        record = {
            'vehicle_id': vehicle_id,
            'date': date,
            'description': description,
            'cost': cost
        }
        maintenance_records.append(record)
        print("Maintenance record added successfully.")
    except Exception as e:
        print(f"Error adding maintenance record: {e}")

def get_maintenance_records(vehicle_id):
    try:
        records = [record for record in maintenance_records if record['vehicle_id'] == vehicle_id]
        if not records:
            raise ValueError(f"No maintenance records found for Vehicle ID {vehicle_id}.")
        return records
    except Exception as e:
        print(f"Error retrieving maintenance records: {e}")
        return []
