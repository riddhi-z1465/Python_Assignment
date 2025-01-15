# Define a class Car with a constructor that sets make, model, and year. Create an instance and display its details.
class Car:
    def __init__(self, make, model, year):
        self.make = make    # Car make
        self.model = model  # Car model
        self.year = year    # Car year

    def info(self):
        """Return information about the car."""
        return f"Car Make: {self.make}, Model: {self.model}, Year: {self.year}"

if __name__ == "__main__":
    # Create an instance of Car
    my_car = Car(make="Ford", model="Mustang", year=2021)

    # Display the car's details
    print(my_car.info())  # Output: Car Make: Ford, Model: Mustang, Year: 2021