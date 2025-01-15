# Create a class Point that overloads the + operator (using __add__) to add the coordinates of two Point objects.
class Point:
    def __init__(self, x, y):
        self.x = x  # x-coordinate
        self.y = y  # y-coordinate

    def __add__(self, other):
        """Overload the + operator to add two Point objects."""
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented  # Return NotImplemented if other is not a Point

    def __repr__(self):
        """Return a string representation of the Point."""
        return f"Point({self.x}, {self.y})"

# Example usage
if __name__ == "__main__":
    point1 = Point(2, 3)
    point2 = Point(4, 5)

    # Add two Point objects
    point3 = point1 + point2

    # Print the result
    print(f"Point 1: {point1}")
    print(f"Point 2: {point2}")
    print(f"Point 3 (Point 1 + Point 2): {point3}")