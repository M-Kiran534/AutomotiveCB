# features/reminders.py

from datetime import datetime, timedelta

# Simulate some sample maintenance reminders
reminders = [
    {'vehicle_id': 1, 'reminder': 'Change oil', 'date': datetime.now() + timedelta(days=10)},
    {'vehicle_id': 2, 'reminder': 'Tire rotation', 'date': datetime.now() + timedelta(days=15)},
]

def display_reminders():
    try:
        print("\nUpcoming Maintenance Reminders:")
        current_date = datetime.now()
        
        if not reminders:
            raise ValueError("No reminders set.")

        for reminder in reminders:
            reminder_date = reminder['date']
            if reminder_date > current_date:
                print(f"Vehicle ID: {reminder['vehicle_id']}, Reminder: {reminder['reminder']}, Date: {reminder_date.strftime('%Y-%m-%d')}")
            else:
                print(f"Vehicle ID: {reminder['vehicle_id']} - {reminder['reminder']} (Past due)")
    except Exception as e:
        print(f"Error: {e}")
