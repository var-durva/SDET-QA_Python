#range() function in python
#range(10) #0......10
#range(1,10) #1......9
#range(1,10,2) #1,3,5,7,9  #1-starting point, 10-ending point, 2-increment
#range(): Value b/w the range

print(range(10))
print(list(range(10)))
print(list(range(5,10)))
print(list(range(5,10,2)))
print(list(range(1,10,2))) #print odd numbers b/w 1 to 10
print(list(range(0,10,2))) #print even numbers b/w 1 to 10
print(list(range(10,1,-1))) #10,9,8,7,6,5,4,3,2
print(list(range(10,1,-2))) #10,9,8,7,6,5,4,3,2
print(list(range(-10,-5)))
print(list(range(-10,-5,2)))
print(list(range(-10,-1,-2))) #empty array