# Create a base class Animal and a derived class Dog. Override a method speak() in the Dog class to print "Woof!".
class Animal:
    def speak(self):
        """Method to be overridden in derived classes."""
        raise NotImplementedError("Subclasses must implement this method.")

class Dog(Animal):
    def speak(self):
        """Override the speak method to print 'Woof!'."""
        print("Woof!")

# Example usage
animal = Animal()  # This will raise an error if you try to call speak()
# animal.speak()  # Uncommenting this line will raise NotImplementedError

dog = Dog()
dog.speak()  # Output: Woof!