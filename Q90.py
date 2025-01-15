# Create a base class Animal and a derived class Dog. The Dog class should inherit attributes and methods from Animal.
class Animal:
    def __init__(self, name, species):
        self.name = name      # Attribute for the animal's name
        self.species = species  # Attribute for the animal's species

    def speak(self):
        return "Some sound"

    def info(self):
        return f"{self.name} is a {self.species}."

class Dog(Animal):
    def speak(self):
        return "Woof!"

if __name__ == "__main__":
    animal = Animal("Generic Animal", "Unknown")
    dog = Dog("Buddy", "Dog")

    print(animal.info())  # Output: Generic Animal is a Unknown.
    print(animal.speak())  # Output: Some sound

    print(dog.info())      # Output: Buddy is a Dog.
    print(dog.speak())     # Output: Woof!