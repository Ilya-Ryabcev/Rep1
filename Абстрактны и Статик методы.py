




































from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def method(self):
        return 'Я гоняю по Москве'

class Car(Vehicle):
    def __init__(self, brand, speed):
        super().__init__(brand)
        self.speed = speed

    @staticmethod
    def statik():
        return "Все хорошо"

    def method(self):
        return super().method() + f" на байке {self.brand}, {self.speed}"


car = Car('bmv', 200)
print(Car.statik())
print(car.method())