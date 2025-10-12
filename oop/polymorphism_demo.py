import math

class Shape:
    def area(self):
        """Raises a NotImplementedError, to be implemented by derived classes."""
        raise NotImplementedError("The area() method must be overridden in derived classes")


class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        """Initializes a Rectangle instance with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius: float):
        """Initializes a Circle instance with radius."""
        self.radius = radius

    def area(self):
        """Calculates and returns the area of the circle."""
        return math.pi * (self.radius ** 2)


# Example usage
if __name__ == "__main__":
    shapes = [
        Rectangle(5, 3),  # Rectangle with length 5 and width 3
        Circle(4)         # Circle with radius 4
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")