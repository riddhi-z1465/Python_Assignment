# Define classes Circle, Square, and Triangle each with a draw() method. Call draw() on a list of shape objects to demonstrate polymorphism.
class Circle:
    def draw(self):
        """Draw a circle."""
        print("Drawing a Circle.")

class Square:
    def draw(self):
        """Draw a square."""
        print("Drawing a Square.")

class Triangle:
    def draw(self):
        """Draw a triangle."""
        print("Drawing a Triangle.")

# List of shape objects
shapes = [Circle(), Square(), Triangle()]

# Call the draw() method on each shape object
for shape in shapes:
    shape.draw()