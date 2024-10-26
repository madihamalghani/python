class Employee:
    name="Enter your name"
    language="Programming language"
    salary="Enter your salary"
    # Yes, __init__ is considered a constructor in Python.
    #  def __init__(self,name,salary,language):  It is a special "dunder" method (double underscores, for "double underscore method") that Python automatically calls when creating a new instance of the Employee class.
    def __init__(self,name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language
        print('I am a dunder method which is called automatically. only init dunder method is called automatically')
        
    def info(self):
        print(f'I am an employee with salary {self.salary}')

amna=Employee("Amna",12000,"C++")
amna.age=30
print(amna.name,amna.salary,amna.language,amna.age)