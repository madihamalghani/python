# Base class
class Grandparent:
    def func1(self):
        print("This is Grandparent")

# Intermediate class inheriting from Grandparent (Multilevel Inheritance)
class Parent1(Grandparent):
    def func2(self):
        print("This is Parent1")

# Another base class
class Parent2:
    def func3(self):
        print("This is Parent2")

# Child class inheriting from both Parent1 and Parent2 (Multiple Inheritance)
class Child(Parent1, Parent2):
    def func4(self):
        print("This is Child")

# Create an instance of the Child class
obj = Child()
obj.func1()  # Output: This is Grandparent=> top-level class.
obj.func2()  # Output: This is Parent1=> multilevel inheritance chain (Grandparent -> Parent1).
obj.func3()  # Output: This is Parent2=>separate class.
obj.func4()  # Output: This is Child=> multiple inheritance
