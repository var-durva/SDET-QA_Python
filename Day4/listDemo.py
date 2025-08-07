#List: A list id a collection which is ordered and changeable.
#In Python lists are written with square brackets[].List is mutable.
#Example 1: How to create list
mylist1=[10,20,30,40,50]
mylist2=["apple", "banana", "cherry"]
mylist3=[10, "apple"]
mylist=list() #empty list

print(mylist1)
print(mylist2)
print(mylist3)
print(mylist)

#Example 2: Accessing items from the list
mylist=["apple", "banana", "cherry"]
print(mylist[1])
print(mylist[0])
print(mylist[2])
print(mylist[-1])


#Example3: Range of list
mylist4=["apple", "banana", "cherry",10,20,30,40,50]
print(mylist4[2:5])
print(mylist4[-4:-1])

#Example4:Change items value
mylist5=["apple", "banana", "cherry"]
print(mylist5)
mylist5[0]="orange"
print(mylist5)

#Example5: Read the list items using loop

for i in mylist:
    print(i)

#Example 6: Check if the item is present in the list
mylist6=["apple", "banana", "cherry"]
if "apple" in mylist6:
    print("Yes, item is present")
else:
    print("No, item is not present")

#Example7: List of length
mylist6=["apple", "banana", "cherry"]
print(len(mylist6)) #3

#Example 8: Add items append() and insert()
mylist6=["apple", "banana", "cherry"]
mylist6.append("orange")  #['apple', 'banana', 'cherry', 'orange']
print(mylist6)

mylist7 = ['apple', 'banana', 'cherry', 'orange']
mylist7.insert(1, "mango")
print(mylist7)


#Note: Function is when a command with bracket, pop() is a function and del is a command.

#Example9: Remove item from the list #del #pop() #clear()
mylist8 = ['apple', 'banana', 'cherry', 'orange']
mylist8.pop(1) #1 is the index here  #pop is a function
print(mylist8)

del mylist8[1] #delete a particular index function    #de is the keyword
print(mylist8)

mylist8.clear() #delete all items and received empty array  #clear is the function
print(mylist8)

#copy list
#list
#approch 1
myList1 =['apple', 'banana', 'cherry', 'orange']
myList2 = list(myList1)
print(myList1)
print(myList2)

#approch 2
myList3 = myList1.copy()
print(myList3)


#joining/combine list
#using + operator
list1 = ["1", "2", "3"]
list2 = ["a", "b", "c", "d"]
list3 = list1 + list2
print(list3)

list4=list2 + list1
print(list4)

#Using loop statement
list1 = ["1", "2", "3"]
list2 = ["a", "b", "c", "d"]
for i in list2:
    list1.append(i)
print(list1)

#using extend()
list5 = ["1", "2", "3"]
list6 = ["a", "b", "c", "d"]
list5.extend(list6)


#compare
mylist10=[10, 20, 30]
mylist11=["a", "b", "c"]
if mylist10==mylist11:
    print("Mylist are equal")
else:
    print("Mylist are not equal")
