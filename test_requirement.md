# Automotive Maintenance Tracker - Test Requirements and Cases

## Test Cases for **Add Vehicle**

### 1. **Functional Test: Add Valid Vehicle**
- **Description**: Test adding a vehicle with all valid details.
- **Expected Result**: Vehicle should be successfully added to the system with all details saved.

### 2. **Boundary Test: Add Vehicle with Minimum Fields**
- **Description**: Test adding a vehicle with only mandatory fields filled (e.g., vehicle name and ID).
- **Expected Result**: Vehicle should be added successfully, but optional fields can be left blank.

### 3. **Negative Test: Add Vehicle with Invalid Data**
- **Description**: Test adding a vehicle with invalid data (e.g., special characters in the vehicle ID, invalid year).
- **Expected Result**: System should reject the input and show an error message.

### 4. **Data Validation Test: Duplicate Vehicle ID**
- **Description**: Test adding a vehicle with an already existing vehicle ID.
- **Expected Result**: System should show an error message indicating that the vehicle ID already exists.

### 5. **Usability Test: User Interface for Adding Vehicle**
- **Description**: Ensure that the add vehicle UI is intuitive and easy to navigate.
- **Expected Result**: The user should easily understand how to add a vehicle, with helpful field labels and tooltips.

---

## Test Cases for **View Vehicles**

### 1. **Functional Test: View All Vehicles**
- **Description**: Test viewing all vehicles in the database.
- **Expected Result**: System should display a list of all vehicles added with their details.

### 2. **Performance Test: View Vehicles with Large Data Set**
- **Description**: Test viewing a large number of vehicles (e.g., 1000+).
- **Expected Result**: The system should display the list of vehicles without performance degradation.

### 3. **Sorting and Filtering Test: Sort and Filter Vehicles**
- **Description**: Test sorting vehicles by different parameters like ID, model, etc., and filtering vehicles based on criteria (e.g., by maintenance status).
- **Expected Result**: Vehicles should be sorted and filtered correctly as per the criteria.

### 4. **Usability Test: Pagination in View Vehicles**
- **Description**: Ensure that the system displays a limited number of vehicles per page and provides pagination for easy navigation.
- **Expected Result**: The pagination should work seamlessly, allowing the user to navigate through pages easily.

---

## Test Cases for **Book Maintenance**

### 1. **Functional Test: Book Maintenance for a Vehicle**
- **Description**: Test booking maintenance for an existing vehicle.
- **Expected Result**: Maintenance appointment should be booked, and the vehicle’s maintenance status should be updated.

### 2. **Negative Test: Book Maintenance for a Non-Existing Vehicle**
- **Description**: Test booking maintenance for a vehicle ID that doesn’t exist in the system.
- **Expected Result**: System should show an error message indicating that the vehicle ID is not found.

### 3. **Boundary Test: Book Maintenance on Future Date**
- **Description**: Test booking a maintenance appointment for a date in the future.
- **Expected Result**: Maintenance should be booked successfully for a future date.

### 4. **Usability Test: UI for Booking Maintenance**
- **Description**: Ensure the booking process is easy to understand with clear options for selecting date, time, and type of maintenance.
- **Expected Result**: The user should be able to book a maintenance appointment with minimal effort.

---

## Test Cases for **View Maintenance**

### 1. **Functional Test: View Maintenance Details for a Vehicle**
- **Description**: Test viewing the maintenance history for a specific vehicle.
- **Expected Result**: The system should display a list of maintenance activities performed on that vehicle with relevant details (date, type, cost, etc.).

### 2. **Performance Test: View Maintenance History for Multiple Vehicles**
- **Description**: Test viewing maintenance records for multiple vehicles at once.
- **Expected Result**: The system should handle the display of maintenance records efficiently.

### 3. **Negative Test: No Maintenance History for Vehicle**
- **Description**: Test viewing maintenance records for a vehicle that has not had any maintenance.
- **Expected Result**: System should display a message like "No maintenance history found for this vehicle."

---

## Test Cases for **Upcoming Maintenance Dates**

### 1. **Functional Test: Display Upcoming Maintenance Dates**
- **Description**: Test displaying the upcoming maintenance dates for all vehicles.
- **Expected Result**: The system should correctly list vehicles with scheduled maintenance dates in chronological order.

### 2. **Negative Test: No Upcoming Maintenance**
- **Description**: Test the scenario where no vehicle has upcoming maintenance scheduled.
- **Expected Result**: The system should display a message indicating "No upcoming maintenance."

### 3. **Boundary Test: Upcoming Maintenance Date in the Near Future**
- **Description**: Test displaying vehicles with upcoming maintenance dates that are within the next few days.
- **Expected Result**: The system should display maintenance appointments scheduled for the near future accurately.

---

## Test Cases for **Export Data (CSV and Excel)**

### 1. **Functional Test: Export Vehicles to CSV**
- **Description**: Test exporting all vehicle data to a CSV file.
- **Expected Result**: The system should generate a valid CSV file with the correct vehicle data.

### 2. **Functional Test: Export Vehicles to Excel**
- **Description**: Test exporting vehicle data to an Excel file.
- **Expected Result**: The system should generate a valid Excel file with the correct vehicle data.

### 3. **Data Integrity Test: Export Data Accuracy**
- **Description**: Test that the data exported to CSV or Excel matches the data shown in the system.
- **Expected Result**: The exported file should have all the correct details (no missing or incorrect data).

### 4. **Negative Test: Export Data with Empty Fields**
- **Description**: Test exporting data when some fields are empty (e.g., vehicles without maintenance history).
- **Expected Result**: The system should handle empty fields gracefully and not crash during the export process.

### 5. **Performance Test: Export Large Data Set**
- **Description**: Test exporting a large set of data (e.g., 1000+ vehicles) to both CSV and Excel formats.
- **Expected Result**: The system should export the data without significant delay or failure.

---

## Additional General Test Cases

### 1. **Security Test: Access Control**
- **Description**: Test if unauthorized users can access restricted features (e.g., adding or viewing maintenance details).
- **Expected Result**: The system should prevent unauthorized access and show an appropriate error message.

### 2. **Data Integrity Test: Consistency Across Views**
- **Description**: Test data consistency across different views (e.g., vehicle list, maintenance history).
- **Expected Result**: The data shown should be consistent across all views after updates, additions, or deletions.

### 3. **Backup and Restore Test**
- **Description**: Test the ability to backup the database and restore it to ensure no data loss.
- **Expected Result**: The system should be able to backup and restore data without any issues.

### 4. **Usability Test: Error Message Clarity**
- **Description**: Test the clarity and user-friendliness of error messages.
- **Expected Result**: Error messages should be clear, concise, and provide guidance on how to resolve the issue.

---

By performing these test cases, you can ensure that the Automotive Maintenance Tracker application is fully functional, efficient, and user-friendly.
