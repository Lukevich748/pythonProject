import math

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area = math.pi * self.radius ** 2
        return area

    def get_perimeter(self):
        perimetr = 2 * math.pi * self.radius
        return perimetr

circle = Circle(10)
area = circle.get_area()
print(area)
perimeter = circle.get_perimeter()
print(perimeter)