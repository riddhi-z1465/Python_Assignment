# Define a class Point(x, y) that overloads the + operator to add the coordinates of two Point objects.
class Point:
    def __init__(self, x, y):
        """Initialize the Point with x and y coordinates."""
        self.x = x
        self.y = y

    def __add__(self, other):
        """Overload the + operator to add two Point objects."""
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented  # Return NotImplemented if other is not a Point

    def __repr__(self):
        """Return a string representation of the Point."""
        return f"Point({self.x}, {self.y})"

# Example usage
point1 = Point(2, 3)
point2 = Point(4, 5)

# Add two Point objects using the overloaded + operator
result_point = point1 + point2

# Print the result
print("Result of adding points:", result_point)  # Output: Result of adding points: Point(6, 8)