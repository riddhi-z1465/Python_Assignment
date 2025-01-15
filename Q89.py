# Modify the Car class to have default values for make and model if not provided.
class Car:
    def __init__(self, make="Toyota", model="Corolla"):
        self.make = make  # Car make
        self.model = model  # Car model

    def info(self):
        """Return information about the car."""
        return f"Car Make: {self.make}, Model: {self.model}"

if __name__ == "__main__":
    # Create a car with default values
    default_car = Car()
    print(default_car.info())  # Output: Car Make: Toyota, Model: Corolla

    # Create a car with specified make and model
    custom_car = Car(make="Honda", model="Civic")
    print(custom_car.info())  # Output: Car Make: Honda, Model: Civic