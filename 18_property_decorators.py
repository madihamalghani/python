# basically aik property bna rhae hain or viewer ko yahi lag rha kae wo sirf aik attribute 
# jab kae hm  us pr methods b laga rhae hain 
class Employee:
    a=1
    @classmethod
    def show(cls):
        print(f'Value of a is {cls.a} ')
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]
e=Employee()
e.a=45
e.name="Madiha Fatima"
print(e.name)
e.show()