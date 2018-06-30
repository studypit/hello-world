class Test1:
    pass

t1 = Test1()
print(t1)

class Test2:
    def __init__(self, name):
        self.name = name

t2 = Test2('test2')
print(t2)
print(t2.name)

class Test3:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Test: {}'.format(self.name)

t3 = Test3('test3')
print(t3)
print(t3.name)
