# enumerate:
l=[3,513,53,535]
# -------------------Simple method:---------------
# index =0
# for item in l:
#     print(f'The item number at index {index} is {item}')
#     index+=1
# This an be simplified using enumerate function:
for index,item in enumerate(l):
    print(f'The item number at index {index} is {item}')
