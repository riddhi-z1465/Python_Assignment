# Demonstrate polymorphism by defining a method draw() in multiple classes (Circle, Triangle, etc.) and calling draw() on a list of shapes.
class Circle:
    def draw(self):
        return "Drawing a Circle"

class Triangle:
    def draw(self):
        return "Drawing a Triangle"

class Square:
    def draw(self):
        return "Drawing a Square"

# Function to draw shapes
def draw_shapes(shapes):
    for shape in shapes:
        print(shape.draw())

# Example usage
if __name__ == "__main__":
    # Create a list of shape objects
    shapes = [Circle(), Triangle(), Square()]

    # Call the draw method on each shape
    draw_shapes(shapes)