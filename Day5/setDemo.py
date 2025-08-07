#Set: A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
#Creating set
myset={"apple", "banana", "cherry"}
print(myset)

#Accessing items from set
myset={"apple", "banana", "cherry"}
for i in myset:
    print(i)

#value is existing in set
#arrorch1
if "apple" in myset:
    print("apple is set")
else:
    print("apple is not in set")

#approch2
print("apple" in myset)
print("Apple" in myset)


#adding items to the set
#add() - add single item
#update() --multiple item

myset.add("Orange")
print(myset)

myset.add("mango")
print(myset)

myset.update(["Veg", "watermelon"])
print(myset)

#length of the set
print(len(myset))

#Remove the items
#remove(), #discard()
myset.remove("Veg")
print(myset)

#myset.remove("Veg") # received KeyError: 'Veg'

myset.discard("Orange")
print(myset)

myset.discard("Orange") # Not received any error

#Clear all items from set
myset.clear()
print(myset) #set()

#delete set
# myset={"apple", "banana", "cherry"}
# del myset
# print(myset) #NameError: name 'myset' is not defined

#Joining 2 sets -
# approach 1: using union()
set1 = {"a", "b", "c"}
set2= {1,3,5.6}
set3 = set1.union(set2)
print(set3)

#approach2: using update()
set1 = {"a", "b", "d"}
set2= {1,4,5.6}
set1.update(set2)
print(set1)
