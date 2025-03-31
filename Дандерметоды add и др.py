# Сложение __add__
# Вычитание __sub__
# Умножение __mul__
# Деление __truediv__
# Сравнение(больше) __gt__(работает как __lt__)
# Сравнение(меньше) __lt__
# Сравнение(равно)  __eq__(работает как !=)
































# class Path:
#     def __init__(self, value):
#         self.value = value
#
#     def __add__(self, other):
#         return Path(self.value - other.value)
#
#     def __str__(self):
#         return str(self.value)
#
# a = Path(100)
# b = Path(5)
# c = Path(15)
# print(a + b + c)

# from functools import total_ordering
# @total_ordering
# class Number:
#     def __init__(self, value):
#         self.value = value
#
#     def __gt__(self, other):
#         return self.value > other.value
#
#     def __eq__(self, other):
#         return self.value == other.value
#
# a = Number(10)
# b = Number(10)
#
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)
# print(a == b)
# print(a != b)


