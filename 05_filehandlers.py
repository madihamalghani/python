# write file
str="Hi! I am na amazing girl with an amazing heart. I love to be kind. I love humanity"
f=open("myfile.txt","w")
f.write(str)
f.close()
# read file:
p=open("myfile.txt","r")
data=p.read()
print(data)
p.close()
# same as read file can be written in this way:
with open("file.txt") as f:
    print(f.read()) # don't need to explicitly close the file



