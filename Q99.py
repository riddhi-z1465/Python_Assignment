# Create a class that uses the @property decorator to get/set an attribute with some validation logic.
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius  # Private attribute to store temperature

    @property
    def celsius(self):
        """Get the temperature in Celsius."""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Set the temperature in Celsius with validation."""
        if not isinstance(value, (int, float)):
            raise ValueError("Temperature must be a number.")
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C).")
        self._celsius = value

# Example usage
if __name__ == "__main__":
    temp = Temperature()  # Create a Temperature object

    # Set a valid temperature
    temp.celsius = 25
    print(f"Temperature in Celsius: {temp.celsius}")

    # Attempt to set an invalid temperature
    try:
        temp.celsius = -300  # This will raise an error
    except ValueError as e:
        print(e)  # Print the error message

    # Attempt to set a non-numeric value
    try:
        temp.celsius = "hot"  # This will also raise an error
    except ValueError as e:
        print(e)  # Print the error message