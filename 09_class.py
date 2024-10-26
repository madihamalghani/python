# Employee is a class just like a blank paper with options:
class Employee:
    name="Enter your name"
    language="Programming language"
    salary="Enter your salary"
    def info(self):
        print(f'I am an employee with salary {self.salary}')
# madiha is the object with filled options:
madiha=Employee()
madiha.name="Madiha Fatima"
madiha.language="python"
madiha.salary=12000
print(madiha.name,madiha.language,madiha.salary)
madiha.name="Amna"
madiha.language="C++"
madiha.salary=11000
print(madiha.name,madiha.language,madiha.salary)
madiha.info()
# for static : we need not to pass self use @staticmethod:
class Greet:
    @staticmethod
    def greet():
    #  name=""
        print('----------Displaying static method---------')
        print('Hello have a nice day!')
greeting=Greet()

greeting.greet()
