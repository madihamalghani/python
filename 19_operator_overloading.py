class Number1:
    def __init__(self,n):
        self.n=n

p=Number1(1)
q=Number1(2)
# print(p+q) # error
# -----------------------Using overloading---------------------
class Number:
    def __init__(self,n):
        self.n=n
    def __add__(self,num):
        return self.n + num.n
n=Number(1)
m=Number(2)
print(n+m)