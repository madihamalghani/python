# dictionary => key value pairs
marks={
    "Madiha": 100,
    "Laiba":100,
    "Hamazia":90
}
print(marks,type(marks))
print(marks["Madiha"])
# -------------------------methods---------------------
# items()
print(marks.items())
# keys()
print(marks.keys())
# values
print(marks.values())
# update
marks.update({"Madiha":99,"Ayesha":30}) # ayesha is added, marks of madiha changes
print(marks)
# get
print(marks.get("Madiha"))
# get vs [] => these are not same
print(marks.get("Ayesha")) #if i write Amna instead of Ayesha it will give none
print(marks["Ayesha"])   #if i write Amna instead of Ayesha it will give error
# ======================Sets========================
d={} #empty dictionary
print(type(d))
s={1,3,4,5} # set
print(type(s))
# to make empty set:
e=set()
print(type(e))
#set don't contain a specific order and repeative elements are ignored
g={1,89,5,5,4,3}
print(g)
f={1,2,3,"Madiha"} # so we can add insert int and string both
print(f,type(f))
# ---------methods---------
# add
f.add(566)
f.add("Amna")
print(f)
# len 
print(len(f))
f.remove(1)
print(f)
# pop=> remove random element from set
# clear=> remove all valuess from sets
# union:
s1={1,4,5,6,7}
s2={3,5,6,7}
print(s1.union(s2))
# intersection:
print(s1.intersection(s2))
# ==========================Programs========================
# dictionary conatins words in urdu and its translation in english
# options for users to look it up
words={
    "madad":"Help",
    "umeed":"Hope",
    "janat":"Mother,Heaven",
    "gunnah":"Sin"
}
word=input('Enter the word whose meaning you want to know(madad,umeed,janat,gunnah): ')
print(words[word])
# a set can contain 18 as a string and 18 as an integer
p=set()
p.add(18)
p.add("18")
print(p)
# what will be length of set if we input 3 numbers in set i.e: 20 , 20.0, "20"
set_length=set()
set_length.add(20)
set_length.add(20.0)
set_length.add("20")
print('Set length is: ',len(set_length))
# Can you change values inside a list which is contained in set S?
problem={8,7,12,"Madiha",[1,2]} # set can not change a value as there is no proper indexing, set is immutable
