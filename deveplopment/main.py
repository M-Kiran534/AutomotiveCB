from features.vehicle_manager import add_vehicle_interaction, view_vehicles
from features.maintenance_manager import add_maintenance_interaction, view_maintenance_interaction
from features.remainders import display_reminders
from data.export import export_data_to_csv, export_data_to_json

def main_menu():
    while True:
        print("\nAutomotive Maintenance Tracker")
        print("1. Add Vehicle")
        print("2. View Vehicles")
        print("3. Add Maintenance Record")
        print("4. View Maintenance Records")
        print("5. Show Maintenance Reminders")
        print("6. Export Data (CSV)")
        print("7. Export Data (JSON)")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_vehicle_interaction()
        elif choice == "2":
            view_vehicles()
        elif choice == "3":
            vehicle_id = int(input("Enter the vehicle ID: "))
            add_maintenance_interaction(vehicle_id)
        elif choice == "4":
            vehicle_id = int(input("Enter the vehicle ID: "))
            view_maintenance_interaction(vehicle_id)
        elif choice == "5":
            display_reminders()
        elif choice == "6":
            export_data_to_csv("vehicles.csv")
        elif choice == "7":
            export_data_to_json("vehicles.json")
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
