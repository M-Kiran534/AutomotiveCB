# Requirements for Automotive Maintenance Tracker Project

## Python Version
- Python 3.x (Recommended: Python 3.7 or higher)

## Dependencies
To run the project, you'll need the following Python packages:

- **pandas**: For handling CSV and JSON export.
- **json**: (Standard Library) For exporting data to JSON.
- **csv**: (Standard Library) For exporting data to CSV.
- **datetime**: (Standard Library) For date and time manipulation.

## Installation

1. **Install Python** (if not installed already):
   - Download and install Python from [python.org](https://www.python.org/downloads/).

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install pandas
   ```

## Usage

- Run the `main.py` file to start the application:
  ```bash
  python main.py
  ```

## Optional (For Export)
- **CSV Export**: Used in `data/export.py` for exporting vehicle data to CSV.
- **JSON Export**: Used in `data/export.py` for exporting vehicle data to JSON.
