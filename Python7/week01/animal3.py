class Animal(object):
    owner = 'jack'
    def __init__(self, name):
        self._name = name

    @classmethod
    def get_owner(cls):
        return cls.owner

class Cat(Animal):
    pass

print(Animal.get_owner())
print(Cat.get_owner())

print( '-' * 20 )
class Animal2:
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if isinstance(value, int):
            self._age = value
        else:
            raise ValueError

cat = Animal2()
#cat.age = 'h'
cat.age = 3
print(cat.age)
