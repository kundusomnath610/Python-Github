from abc import ABC, abstractmethod
import math

# Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

# Rectangle Class inheriting from Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)
    
# Circle Class inheriting from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return round(math.pi * self.radius ** 2, 2)
    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)
    
# Taking input from user
length = float(input("Enter the first input: "))
width = float(input("Enter the second input: "))
radius = float(input("Enter the third input: "))

# Creating instances
rectangle = Rectangle(length, width)
circle = Circle(radius)

# Displaying area and perimeter
print(f"Rectangle Area: {rectangle.area()}")
print(f"Rectangle Perimeter: {rectangle.perimeter()}")
print(f"Circle Area: {circle.area()}")
print(f"Circle Perimeter: {circle.perimeter()}")
