from io import StringIO
import pytest
from unittest.mock import patch
from development.features.vehicle_manager import add_vehicle_interaction

def test_addVehicle():
    with patch("buildins.input", side_effect=[101, "",""]):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            add_vehicle_interaction()
            output = mock_stdout.getvalue()

            assert "Vehicle model is mandatory. Please enter a valid model." in output
            assert "Vehicle make is mandatory. Please enter a valid make." in output

def test_add_vehicle_success():
    with patch("builtins.input", side_effect=[102, "Sedan", "Toyota"]):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            add_vehicle_interaction()
            
            # Get the printed output from the function
            output = mock_stdout.getvalue()
            
            # Assert that the success message appears
            assert "Vehicle Sedan added successfully." in output
