#A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets(). Tuple are immutable.
#Exampla1: creating tuple

mytuple = ("Apple", "banana", "orange")
print(mytuple)
print(mytuple[1])
print(mytuple[-1])
print(mytuple[0:2])

mytuple1 =() #empty
print(mytuple1)


#Changing tuple values -Not possible
#1 Cannot modify existing value
#2 cannot append new value
#3 cannot insert a new value
#4 cannot remove a value
#but we have indirect way to change tuple #tuple -> list(modify) -> tuple

mytuple = ("Apple", "banana", "orange")
print(mytuple)
mylist = list(mytuple)  #convert into list
print(mylist)
mylist[0] = "e"
mytuple = tuple(mylist)
print(mytuple) #convert into tuple

#Reading tuple items using loop
mytuple = ("Apple", "banana", "orange")
for i in mytuple:
    print(i)

#Checking if item exists(searching of item in tuple)
mytuple = ("Apple", "banana", "orange")

if "apple" in mytuple:
    print("Apple is present")
else:
    print("item is not present")

#Tuple length-counting items in tuple
mytuple = ("Apple", "banana", "orange", 1, "Test" )
print(len(mytuple))


#add items in the tuple -not possible

#copy tuple
mytuple1 = ("Apple", "banana", "orange")
print(mytuple1)
mytuple2 = tuple(mytuple1)
print(mytuple2)


#removing item from the tuple is not possible
mytuple6 = ("Apple", "banana", "orange")
#mytuple6.remove(1) #invalid/not possible to remove
# del mytuple6 #deleted tuple
# print(mytuple6)


#Join/combine tuple
tuple5=("Apple", "banana", "orange")
tuple7=("apple", "Banana", "Orange")
tuple8=tuple5 + tuple7
print(tuple8)

#compare
tuple10=(10, 20, 30)
tuple11=("a", "b", "c")
if tuple10==tuple11:
    print("Tuple are equal")
else:
    print("Tuple are not equal")
