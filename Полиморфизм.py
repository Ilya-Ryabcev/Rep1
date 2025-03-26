# import math
#
# class Shape:
#     def area(self):
#         raise NotImplementedError("Subclasses should implement this method!")
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return math.pi * (self.radius ** 2)
#
# class Rectangle(Shape):
#     def __init__(self, wigth, height):
#         self.wigth = wigth
#         self.height = height
#
#     def area(self):
#         return self.wigth * self.height
#
# shapes = [Circle(5), Rectangle(5,10), Circle(5)]
# areas = [x.area() for x in shapes]
#
# for x in shapes:
#     x.area()
#
#
# for i in areas:
#     print(i)


