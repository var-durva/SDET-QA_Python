#Types of argument/parameters we can pass to the function.
#1. Positional arguments
#2. Keyword arguments

#Example 1:
def fun(i, j):
    print(i,j)
fun(10,20) #Positional arguments
fun(j=20, i=10) #keyword arguments

#Example 2: Default values assigned to Positional arguments
def func(i, j=10):
    print(i, j)
func(100, 200) #100 300
func(300) # 300 10

def func(i=1, j=10):
    print(i, j)
func() #1 10

#Example 3: keyword arguments
def func(greeting, name):
    print(greeting +" Miss " +name)
func(greeting="Hello", name ="Durva")
func(name ="Durva", greeting="Hello")

#Example 4:
def my_func(a,b,c):
    print(a,b,c)
my_func(10,20,300)
my_func(a=10, b=20, c=30)
my_func(10, 40, c=300)
my_func(20, b=23, c = 50)
#my_func(10, b=3, 20) #positional argument follows keyword argument
#my_func(10, 30, b=20) #TypeError: my_func() got multiple values for argument 'b'

#Example 5: Function can return values
def largest(a,b):
    if a>b:
        return a, b
    else:
        return b,a

res=largest(10, 20)
print(res)

print(type(res))

print(largest(100, 200))
print(largest(20, 10))