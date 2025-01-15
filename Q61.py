# Create a class Person with attributes name and age. Include a method greet() that prints "Hello, my name is <name>."
class Person:
    def __init__(self, name, age):
        """Initialize the attributes name and age."""
        self.name = name
        self.age = age

    def greet(self):
        """Print a greeting message."""
        print(f"Hello, my name is {self.name}.")
person1 = Person("Alice", 30)
person1.greet()  # Output: Hello, my name is Alice.

person2 = Person("Bob", 25)
person2.greet()  # Output: Hello, my name is Bob.