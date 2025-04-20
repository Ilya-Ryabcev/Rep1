import pickle
class New:
    def __init__(self, name, age, city=456):
        self.name = name
        self.age = age
        self.city = city

    def __reduce__(self):
        cls = self.__class__
        args = (self.name, self.age)
        state = self.__dict__
        return (cls, args, state)


obj = New('Bob', 40, '123')
string_ser = pickle.dumps(obj)
print(string_ser)
string_unser = pickle.loads(string_ser)
print(obj.__reduce__())