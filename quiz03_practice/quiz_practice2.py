# write a class defintion for the following:
# rect: Rectangle = Rectangle(w=4.0, h=5.5)
# print(rect.area())


class Rectangle:
    width: float
    length: float

    def __init__(self, w: float, h: float):
        self.width = w
        self.length = h

    def area(self) -> float:
        area: float = self.length * self.width
        return area


rect: Rectangle = Rectangle(w=4.0, h=5.5)
print(rect.area())
