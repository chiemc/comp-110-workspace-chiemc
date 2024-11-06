import math

# try writing a class definition for the following:
# circ: Circle = Circle(r=2.0)
# print(circ.area())


class Circle:
    radius: float
    # change r to radius if you want

    def __init__(self, r: float):
        self.radius = r

    def area(self) -> float:
        area: float = math.pi * (self.radius**2)
        return area


circ: Circle = Circle(r=2.0)
print(circ.area())
