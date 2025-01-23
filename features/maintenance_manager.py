from data.maintenance import add_maintenance_record, get_maintenance_records

def add_maintenance_interaction(vehicle_id):
    service_type = input("Enter the type of maintenance (e.g., Oil Change, Tire Rotation): ")
    date = input("Enter the date of maintenance (YYYY-MM-DD): ")
    mileage = input("Enter the vehicle mileage at the time of maintenance: ")
    record = {
        "vehicle_id": vehicle_id,
        "service_type": service_type,
        "date": date,
        "mileage": mileage,
    }
    add_maintenance_record(record)
    print("Maintenance record added successfully!")

def view_maintenance_interaction(vehicle_id):
    records = get_maintenance_records(vehicle_id)
    if not records:
        print("No maintenance records found for this vehicle.")
        return
    for record in records:
        print(f"Date: {record['date']}, Service: {record['service_type']}, Mileage: {record['mileage']}")
