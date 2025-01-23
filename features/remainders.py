from datetime import datetime, timedelta
from data.vehicle import get_vehicles
from data.maintenance import get_maintenance_records

def get_upcoming_maintenance_reminders():
    vehicles = get_vehicles()
    reminders = []

    for vehicle in vehicles:
        records = get_maintenance_records(vehicle["id"])
        if not records:
            continue

        # Find the last maintenance record
        last_record = max(records, key=lambda r: datetime.strptime(r["date"], "%Y-%m-%d"))
        last_date = datetime.strptime(last_record["date"], "%Y-%m-%d")
        last_mileage = int(last_record["mileage"])

        # Check for reminders (e.g., oil change every 5000 miles or 6 months)
        next_mileage = last_mileage + 5000
        next_date = last_date + timedelta(days=180)  # Approx. 6 months

        if datetime.now() > next_date or int(vehicle["mileage"]) > next_mileage:
            reminders.append({
                "vehicle": f"{vehicle['make']} {vehicle['model']} ({vehicle['year']})",
                "next_mileage": next_mileage,
                "next_date": next_date.strftime("%Y-%m-%d"),
            })

    return reminders

def display_reminders():
    reminders = get_upcoming_maintenance_reminders()
    if not reminders:
        print("No upcoming maintenance reminders.")
        return

    print("Upcoming Maintenance Reminders:")
    for reminder in reminders:
        print(f"- Vehicle: {reminder['vehicle']}")
        print(f"  Next Mileage: {reminder['next_mileage']}, Next Date: {reminder['next_date']}")
