class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_area(self):
        area = self.width * self.height
        return area

rectangle = Rectangle(4, 50)
print(rectangle.get_area())