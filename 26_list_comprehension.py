# myList=[1,2,6,9,10]
# squaredList=[]
# for item in myList:
#     squaredList.append(item*item)
# print(squaredList)
# -------------------------------by list comprehension-----------------------------
myList=[1,2,6,9,10]
squaredList=[i*i for i in myList]
print(squaredList)