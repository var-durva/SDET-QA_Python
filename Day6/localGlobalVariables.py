#Global and local variables
#The variables create outside of function are called global variables.
#The variables create inside of function are called local variables.
#Example 1:
global_var=20

def fun():
    local_var = 30
    print(local_var)
    print(global_var)

fun()
#print(local_var) #invalid bcoz local_var is local variable of fun()
print(global_var) #valid bcoz global_var is global variable of fun()

#Example 2:
xy = 100 #global variable
def cool():
    xy =200 #local variable
    print(xy)
cool()

#Example 3: Using global variable in local variable and update value
xy=100

def cam():
    global xy
    xy=300  #global variable
    #global xy =300 invalid statement in Python
    print(xy)
cam()  #300
print(xy) #300


#Example 4
x=100

def cam():
    global x
    x=300  #global variable
    print(x)
#cam()
print(x) #100 as not calling cam function

#There is no need to declare global variable outside the function.
#you can declare them global inside the function but we need to specify global text.

#Example 5:
def fun():
    global x
    x =30
    print(x)
fun()
