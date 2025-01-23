import json

MAINTENANCE_FILE = "maintenance.json"

def add_maintenance_record(record):
    records = load_maintenance_records()
    records.append(record)
    save_maintenance_records(records)

def get_maintenance_records(vehicle_id):
    records = load_maintenance_records()
    return [r for r in records if r["vehicle_id"] == vehicle_id]

def load_maintenance_records():
    try:
        with open(MAINTENANCE_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_maintenance_records(records):
    with open(MAINTENANCE_FILE, "w") as f:
        json.dump(records, f, indent=4)
