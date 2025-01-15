# Use the abc module to define an abstract base class Shape with an abstract method area(). Implement subclasses Circle and Rectangle.
from abc import ABC, abstractmethod
import math

# Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

# Subclass for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2)

# Subclass for Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

# Example usage
if __name__ == "__main__":
    # Create a Circle object
    circle = Circle(radius=5)
    print(f"Area of the circle: {circle.area():.2f}")

    # Create a Rectangle object
    rectangle = Rectangle(width=4, height=6)
    print(f"Area of the rectangle: {rectangle.area()}")