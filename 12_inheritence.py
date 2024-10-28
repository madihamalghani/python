"""
Types of inheritence:
single
double
multi-level
super
"""
# --------------single inheritence----------------#
class Employee: #parent class / base class
    company="9 TO 5 Marketing"
    def show(self):
        print(f'the name is {self.name} and the salary is {self.salary}')
# class Programmer:
#     company="6 hours work_from_home"

#     def show(self):
#         print(f'the name is {self.name} and the salary is {self.salary}')
#     def showLanguage(self):
#         print(f'the name is {self.name} and he is good in {self.language} language')

# ------------inherited class:-------------------
class Programmer(Employee):
    company="6 hours work_from_home"
    def showLanguage(self):
        print(f'the name is {self.name} and he is good in {self.language} language')
a=Employee()
b=Programmer()

print(a.company,b.company)