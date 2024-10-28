# ------------Multiple Inheritence---------#
class Employee: #parent class / base class
    
    language="python"   
    company="9 TO 5 Marketing"
    salary=30000
    def show(self):
        print(f'the name is {self.company} and the salary is {self.salary}')

class Coder():
    print(f'I am the real coder')
class Programmer(Employee,Coder):
    company="6 hours work_from_home"
    salary=300
    def showLanguage(self):
        print(f'the name is {self.company} and he is good in {self.language} language and salary is {self.salary}')
a=Employee()
b=Programmer()
# ---------------display------------------
b.showLanguage()
a.show()