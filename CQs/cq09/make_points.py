from CQs.cq09.point import Point


point: Point = Point(2.0, 3.0)

point.scale_by(2)
print(point.x, point.y)

scaled_point = point.scale(3)
print(scaled_point.x, scaled_point.y)
