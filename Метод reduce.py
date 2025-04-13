import pickle
class New:
    def __init__(self, name, age, city='234'):
        self.name = name
        self.age = age
        self.city = city

    def __reduce__(self):
        return (self.__class__, (self.name, self.age))


obj = New('Bob', 40, '123')
string_ser = pickle.dumps(obj)
print(string_ser)
string_unser = pickle.loads(string_ser)
print(obj.__reduce__())