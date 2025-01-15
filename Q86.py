# Define a class Person with attributes name and age. Create an instance of this class and print its attributes.
class Person:
    def __init__(self, name, age):
        self.name = name  # Person's name
        self.age = age    # Person's age

if __name__ == "__main__":
    # Create an instance of Person
    person = Person(name="Alice", age=30)

    # Print the attributes of the person
    print(f"Name: {person.name}")  # Output: Name: Alice
    print(f"Age: {person.age}")    # Output: Age: 30