# utils/helpers.py

from datetime import datetime

def format_date(date_string):
    """Convert a date string (YYYY-MM-DD) to a datetime object."""
    try:
        return datetime.strptime(date_string, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return None
