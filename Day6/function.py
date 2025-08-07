#functions: Function means set of statements which will perform a task.
#1. Function declaration/creation
#2. Calling the function/invoking function
#Example 1:
def myfun(): #def means define a function or definition of the function. myfun is the name of the function, function is always represent to the bracket and colon
    print("hello") #intention is also needed.
myfun()  #call the function


#Example 2:
def myfun(name): #name as a parameter
    print("Hello", name)
myfun("Durva")

#Example 3:
# def myfun(name): #name as a parameter
#     print("Hello", name)
# myfun(input("Enter name: "))

#Example 4:
def cal(a,b):
    return(a+b)

#approch1
sum=cal(20,30)
print(sum)

#approch2
print(cal(20,30))

#Example 5:
def calu(a,b):
    return(a*b)
mul=calu(2, 30)
print(mul)

#Example6 #received None
def func():
    return
print(func())  #None

#Example7 #received None
def func():
    i=10
print(func())  #None

#Function does not take arguments not returns any value(None).
#Function does not take arguments but returns some value.
#Function takes arguments but no return value.
#Function takes arguments and also return value.


