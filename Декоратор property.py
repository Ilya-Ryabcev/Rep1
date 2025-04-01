# Декоратор Property превращает метод в свойство, в атрибут поля, что позволяет изменить значение обЪекта перед его вызовом
# Также декоратор Property создает сеттер, который  устанавливает значение результата функции

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

class Namber:
    def __init__(self, value, multiplayer):
        self.value = value
        self.multiplayer = multiplayer

    @property
    def resalt(self):
        return self.value * self.multiplayer

namber = Namber(5, 10)
print(namber.resalt)
namber.value = 100
namber.multiplayer = 20
print(namber.resalt)

