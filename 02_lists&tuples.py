friend=["Amna",20,'Medical','Nishtar',30.33]
print('List without change: ')
print(friend)
# append
friend.append('2567')
print('List after using append: ')
print(friend)
# insert
friend.insert(3,'Internship')
print('List after inserting at index 3 : ')
print(friend)
# sort and reverse
l1=[20,40,89,60,70]
print('List of numbers without sorting')
print(l1)
# sorting
print('List of numbers with sorting: ')
l1.sort()
print(l1)
# reverse the sorted list
print('List of sorted numbers after reverse: ')
l1.reverse()
print(l1)
# pop=>del 
l1.pop(3)
print(l1.pop(3)) 
# if return case write in the form: it will return the poped value and that value will be deleted from the list
print(l1)
# remove method
l1.remove(70)
print(l1)
# -------------------------Tuples-----------------------
# tuple immutable while list is mutable
a=(1,2,5,6)
print(type(a))
b=(1,)
print(type(b))
c=(1,45,342,False,'Madiha','Fatima')
print(c)
print(type(c))
no=c.count(45)
print(no)
i=c.index(45)
print(i)
# -------------------------------------------------------------
# input 7 fruit in list 
fruits=[]
fruit1=input('Enter fruit1 ')
fruits.append(fruit1)
fruit2=input('Enter fruit2 ')
fruits.append(fruit2)
fruit3=input('Enter fruit3 ')
fruits.append(fruit3)
fruit4=input('Enter fruit4 ')
fruits.append(fruit4)
fruit5=input('Enter fruit5 ')
fruits.append(fruit5)
fruit6=input('Enter fruit6 ')
fruits.append(fruit6)
fruit7=input('Enter fruit7 ')
fruits.append(fruit7)
print(fruits) 
# let's sum a list:
l=[1,3,4,59,9]
print('sum is: ',sum(l))