# Декоратор Property превращает метод в свойство, в атрибут поля, что позволяет изменить значение обЪекта перед его вызовом
# Также декоратор Property создает сеттер, который устанавливает значение результата функции
# и делитер, который удаляет значение

# Декоратор dataclass используется, если нужно обращаться к полям не по индексам а по именам

# class Variable:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def age_new(self):
#         return self.age* 10
#
# variable = Variable('Mr.Jonson', 25)
# print(variable.age_new()) # вызывает метод со скобками ()

# class Variable:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @property
#     def age_new(self):
#         return self.age* 10
#
# variable = Variable('Mr.Jonson', 25)
# print(variable.age_new) # вызывает без () уже не метод, а свойство

# class Namber:
#     def __init__(self, value, multiplayer):
#         self.value = value
#         self.multiplayer = multiplayer
#         self.resalt = self.value * self.multiplayer
#
# namber = Namber(5, 10)
# print(namber.resalt)
# namber.value = 100
# namber.multiplayer = 20
# print(namber.resalt) # 50

# class Namber:
#     def __init__(self, value, multiplayer):
#         self.value = value
#         self.multiplayer = multiplayer
#
#     @property
#     def resalt(self):
#         return self.value * self.multiplayer
#
#     @resalt.setter
#     def resalt(self, value):
#         self.resal = value
#
#     @resalt.deleter
#     def resalt(self, value):
#         self.resal = value
#
# namber = Namber(5, 10)
# print(namber.resalt)
# namber.value = 100
# namber.multiplayer = 20
# print(namber.resalt) # 2000
#
# namber.resal = 23
# print(namber.resal)
#
# del namber.value
# print(namber.value) # ошибка

from dataclasses import dataclass

# @dataclass()
# class Humen:
#     name: str
#     age: int
#     phone: str
# humen = Humen('Stone', 40, 555555)
# print(humen)

