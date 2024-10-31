from CQs.cq09.point import Point


obj1: Point = Point(2.0, 3.0)

obj1.scale_by(2)
print(obj1.x, obj1.y)

scaled_obj = obj1.scale(3)
print(scaled_obj.x, scaled_obj.y)
