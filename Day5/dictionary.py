#Dictionary
#A dictionary is a collection which is unordered, changeable(mutable) and indexed.
#In python dictionaries are written with curly brackets, and they have keys and values and keys are unique.

mydic ={101: "x", 102: "y", 103:"z"}
print(mydic)

#access items from the dictionary by
# using key
mydic ={
    "brand": "Hyundai",
    "model": "i10",
    "year": 2021
}
print(mydic["brand"]) #Hyundai
# using get() function
x = mydic.get("brand") #Hyundai
print(x)

#Change values in dictionary
print(mydic)
mydic["year"]= "2028"
print(mydic)

#reading items from dictionary using loop
for i in mydic:
    print(i) # print key only

#approach1:
for i in mydic:
    print(mydic[i]) #print values

#approach2:
for i in mydic.values():
    print(i) #print values

#reading key and value
for x,y in mydic.items():
    print(x,y)

#check key is exist in the dictionary or not
#approach1:
if "brand" in mydic:
    print("Key is present")
else:
    print("Key is not present")

#approach2:
print("Brand" in mydic)
print("brand" in mydic)


#find number of items in the dictionary
print(len(mydic))

#add items in the dictionary
mydic["color"]="Red"
print(mydic)

#remove items in the dictionary
#pop #del
mydic.pop("year")
print(mydic)

del mydic["model"]
print(mydic)

#delete complete dictionary
# del mydic
# print(mydic) #NameError: name 'mydic' is not defined

#clear the items in the dictionary
mydic ={
    "brand": "Hyundai",
    "model": "i10",
    "year": 2021
}
mydic.clear()
print(mydic)

#copy the dictionary

mydic1={
    "brand": "Hyundai",
    "model": "i10",
    "year": 2021
}
print(mydic1)

#approach1:
mydic2=mydic1
print(mydic2)

#approach2:
mydic2= mydic1.copy()
print(mydic2)
