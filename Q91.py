# In the Dog class, override a method speak defined in Animal (e.g., Animal says “Some sound”, but Dog says “Woof!”).
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"


if __name__ == "__main__":
    animal = Animal()
    dog = Dog()

    print(f"Animal: {animal.speak()}")  # Output: Some sound
    print(f"Dog: {dog.speak()}")          # Output: Woof!