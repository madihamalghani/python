# access class directly in methods
# ------------------simple form-----------
print('While using simple way:')
class Employee:
    a=1
    def show(self):
        print(f'Value of a is {self.a} ')
e=Employee()
e.a=45
e.show()
# --------------Class method-----------
print('Now we are implementing class method')
class Employee1:
    a=1
    @classmethod
    def show(cls):
        print(f'Value of a is {cls.a} ')
e1=Employee1()
e1.a=45
e1.show()