class Employee():
    a = 1
class Programmer(Employee):
    b=2
class Manager(Programmer):
    c=3
o=Employee()
print(o.a)
# print(o.b) this will throw error
o=Programmer()
print(o.a,o.b)
# print(o.c) this will throw error

o=Manager()
print(o.a,o.b,o.c)