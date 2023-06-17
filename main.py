import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_area(self):
        area = round(math.pi * self.radius ** 2, 2)
        return area

circle = Circle(7)
print(circle.get_area())




