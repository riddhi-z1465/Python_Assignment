# Demonstrate multiple inheritance with two parent classes providing different functionalities to a child class.
# Parent class 1
class Vehicle:
    def start_engine(self):
        return "Engine started."

# Parent class 2
class Radio:
    def play_music(self):
        return "Playing music."

# Child class that inherits from both Vehicle and Radio
class Car(Vehicle, Radio):
    def drive(self):
        return "Car is now driving."

# Create an instance of the Car class
my_car = Car()

# Demonstrate functionalities from both parent classes
print(my_car.start_engine())  # From Vehicle
print(my_car.play_music())    # From Radio
print(my_car.drive())         # From Car