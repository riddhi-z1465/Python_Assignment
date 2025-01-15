# Implement a Python class that overloads the __str__ method to return a string representation of the object.
class Person:
    def __init__(self, name, age):
        self.name = name  # Name of the person
        self.age = age    # Age of the person

    def __str__(self):
        """Return a string representation of the Person object."""
        return f"{self.name} is {self.age} years old."

# Example usage
if __name__ == "__main__":
    person1 = Person("Alice", 30)
    person2 = Person("Bob", 25)

    # Print the Person objects
    print(person1)  # Calls person1.__str__()
    print(person2)  # Calls person2.__str__()