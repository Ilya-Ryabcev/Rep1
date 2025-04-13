# Сложение __add__
# Вычитание __sub__
# Умножение __mul__
# Деление __truediv__

# Сравнение(больше) __gt__(работает как __lt__)
# Сравнение(меньше) __lt__
# Сравнение(равно)  __eq__(работает как !=)

# Сравнение полное через @total_ordering и 2 дандера __gt__ и __eq__ >, <, ==, !=, >=, <=
# from functools import total_ordering
# @total_ordering

# Делает из обЪекта функцию __call__
# __str__

# Получаем итератор и перебираем значения обЪекта __iter__, __next__

# __str__



































# class Path:
#     def __init__(self, value):
#         self.value = value
#
#     def __add__(self, other):
#         return Path(self.value + other.value)
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

# class Func:
#     def __init__(self, value):
#         self.value = value
#
#     def __add__(self, other):
#         return self.value + other.value
#
#     def __call__(self, *args, **kwargs):
#         return [x*2 for x in range(self.value)]
#
#     def __str__(self):
#         return str(self.value)
#
# a = Func(10)
# print(a())
# b = Func(5)
# print(b())
# c = Func(8)
# print(c())
# print(a() + b() + c())



# class Varuable:
#     def __init__(self, value):
#         self.value = value
#         self._current_value = 0
#
#     def __iter__(self):
#         print('START ITER')
#         return self
#
#     def __next__(self):
#         if self._current_value < self.value:
#             self._current_value += 1
#             return self._current_value
#         raise StopIteration
#
# a = Varuable(10)
# for i in a:
#     print(i)

# numbers = [1,2,3,4,5]
# iterator = iter(numbers)
# try:
#     while True:
#         print(next(iterator))
# except StopIteration:
#     print('Итерация завершена')



# class Variable:
#     def __init__(self, value):
#         self.value = value
#
#     def __len__(self):
#         return len(str(self.value))
#
# a = Variable(555)
# print(len(a))


