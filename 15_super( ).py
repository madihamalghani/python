class Employee():
    def __init__(self):
        print('Constructor of the employee')
    a = 1
class Programmer(Employee):
    def __init__(self):
        print('Constructor of the programmer')    
    b=2
class Manager(Programmer):
    def __init__(self):
        print('Constructor of the manager')
    c=3
class Super(Programmer):
    print('Super method runs all the constructors in the parent classes')
    def __init__(self):
        super().__init__()
        print('Constructor of the manager')
    d=4
o=Employee()
print(o.a)
# print(o.b) this will throw error
o=Programmer()
print(o.a,o.b)
# print(o.c) this will throw error

o=Manager()
print(o.a,o.b,o.c)
o=Super()
print(o.a,o.b,o.d)