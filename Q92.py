# Create classes Rectangle and Square. Square should inherit from Rectangle (or implement composition) in a way that automatically sets the length and width to the same value.
class Rectangle:
    def __init__(self, length, width):
        self.length = length  # Length of the rectangle
        self.width = width    # Width of the rectangle

    def area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width

    def __str__(self):
        """Return a string representation of the rectangle."""
        return f"Rectangle(length={self.length}, width={self.width})"


class Square(Rectangle):
    def __init__(self, side_length):
        # Call the constructor of Rectangle with the same value for length and width
        super().__init__(side_length, side_length)

    def __str__(self):
        """Return a string representation of the square."""
        return f"Square(side_length={self.length})"


# Example usage
if __name__ == "__main__":
    rectangle = Rectangle(4, 5)
    print(rectangle)  # Print rectangle details
    print(f"Area of Rectangle: {rectangle.area()}")

    square = Square(3)
    print(square)  # Print square details
    print(f"Area of Square: {square.area()}")