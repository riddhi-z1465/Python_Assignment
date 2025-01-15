# Add a method greet to the Person class that prints "Hello, my name is <name>".
class Person:
    def __init__(self, name):
        """Initialize the Person with a name."""
        self.name = name

    def greet(self):
        """Print a greeting message."""
        print(f"Hello, my name is {self.name}.")

if __name__ == "__main__":
    # Create an instance of Person
    person = Person("Alice")
    # Call the greet method
    person.greet()