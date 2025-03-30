




































# from abc import ABC, abstractmethod
# class Vehicle(ABC):
#     def __init__(self, brand):
#         self.brand = brand
#
#     @abstractmethod
#     def method(self):
#         return 'Я гоняю по Москве'
#
# class Car(Vehicle):
#     def __init__(self, brand, speed):
#         super().__init__(brand)
#         self.speed = speed
#
#     def method(self):
#         return super().method() + " на байке"
#
#     def drive(self):
#         print(f'Еду на машине {self.brand} {self.speed} км в час')
#
# car = Car('bmv', 200)
# car.drive()
# print(car.method())