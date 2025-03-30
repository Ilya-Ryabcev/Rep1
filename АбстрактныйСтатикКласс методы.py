




































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
#         return super().method() + f" на байке {self.brand}, {self.speed}"
#
#     @staticmethod
#     def statik():
#         return "Все хорошо"
#
#     attribute = "Я атрибут класса"
#     @classmethod
#     def class_method(cls):
#         print(cls.attribute)
#         print(Car.attribute)
#
#
# car = Car('bmv', 200)
#
# Car.statik()
# print(Car.statik())
#
# Car.class_method()
#
# print(car.method())