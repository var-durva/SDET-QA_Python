#Python - structured + object-oriented
#oops (object-oriented programming concepts)
#class
#object
#Inheritenace
#Ploymorphism

#class - collection of variables(attributes) & method(behavior)
#A class is blueprint. #logical entity #Does not occupy space in the memory.

#object- is an instance of class
#Physical entity # Occupy certain amount space in the memory.

#For one class we can create multiple objects but objects are independent.

#Function VS Method
#Function - we can create without class.
#Method - creates in side class, a function create inside class called as method.


#2 types of methods we can define within the class.
#1 instance method (we can call only through object).
#2 static method (we can directly call using class).
# @staticmethod  called annotation


#method and Constructor
#method : give any name
           # return the value/s
           #method can take arguments/parameters
           #we have to se an object to invoke the method

#Constructor: name is fixed # _init_(self):
                #Constructor will not return any value
                #Constructor can take arguments/parameters
                #Constructor will be called at the time of object creation itself.

                #__str__(self):  #another Constructor, and it will only return the string data.



#------------------------------------------------------
#class MyClass: #MyClass is the name of the class.
#Inside the class we write the method or variable or method and variable
    #def myfunc(self):  #here def is method # #By default every method take a argument "self", if this function taking multiple argument that we need pass after
# entering comma but don't remove 'Self'.
# Self id representing class name. Ex. MyClass is belonged to this myfunc function.
#inside the not implemented anything, only empty function but should not leave the function like that so enter keyword "pass". Pass is like as none.

#Example1:
class MyClass:
    def myfunc(self):
        pass
    def display(self):
        print("john")
mc1=MyClass()   #object
mc1.myfunc()
mc1.display()

#Example2:
class MyClass:
    def myfunc(self):
        pass
    def display(self, name):
        print(name)
mc1=MyClass()   #object
mc1.myfunc()
mc1.display("Mohan")  #call the function

#Example 3
class MyClass:
    def m1(self):
        print("this is instance method.")
    @staticmethod
    def m2(self, num):
        print(self, num)

mc =MyClass()
mc.m1()
mc.m2(100, 200)

MyClass.m2(10, 20)  #here calling static method directly using class not through object.

#Example 4:
class MyClass:
    a,b = 10,20 #class variable
    def add(self):
        print(self.a + self.b)
    def mul(self):
        print(self.a * self.b)
mc1=MyClass()
mc1.add()
mc1.mul()

#Example 5:
i,j =10,25 #global variable
class MyClass:
    a,b=10,20 #class variable
    def add(self, x,y):  #local variable
        print(x+y)  #accesing local variable
        print(self.a+self.b) #accesing class variable
        print(i+j) #accesing global variable
mc=MyClass()
mc.add(5,10)

#Example 6: when variables name are same of a; variables.
a,b =10,25 #global variable
class MyClass:
    a,b=10,20 #class variable
    def add(self, a,b):  #local variable
        print(a+b) #accesing local variable
        print(self.a+self.b) #accesing class variable
        print(globals()['a']+globals()["b"]) #accesing global variable
mc=MyClass()
mc.add(500,1000)

#Example 7: Create multiple objects with one single class
class MyClass:
    def display(self, name):
        print("This is display method.")
        print(name)

obj1 = MyClass()
obj1.display("Durva")
#obj1.display(input("enter name1: "))


obj2=MyClass()
obj2.display("Dev")
#obj2.display(input("enter name2: "))

#---------------------------------------------------
#example 8: Constructor
class MyClass:
    def __init__(self):  #If Constructor is not take argument then Constructor called default Constructor.
        print("This is a Constructor")
    def m1(self):
        print("Hello")
    def m2(self, x,y):
        return(x+y)

mc=MyClass() #invoke the Constructor automatically
mc.m1() #method we have to call explicit by using object
addi=mc.m2(10,20)
print(addi)

#Example 9:emp

class MyClass:
    name= "john" #class variable
    def __init__(self, name): #Constructor local variable #If Constructor is taking any argument then Constructor called parameterize Constructor.
        print(name)
        print(self.name)
mc=MyClass("Durva") #passing parameter to the Constructor.

#Example 10:
#Req: Employee class
    #Constructor: Add three parameter eid, name, sal
    #display(): print eid, ename, sal

class Emp:
    def __init__(self, eid, ename, sal):
        self.eid=eid #class variable
        self.ename = ename
        self.sal=sal
    def display(self):
        print(self.eid, self.ename, self.sal)

e1=Emp(1, "John", 100)
e1.display()

e2=Emp(2, "Ram", 200)
e2.display()


#Example 11:
#Req: Employee class
    #Constructor: Add three parameter eid, name, sal
    #Constructor: print eid, ename, sal

class Emp:
    def __init__(self, eid, ename, sal):
        self.eid=eid #class variable
        self.ename = ename
        self.sal=sal
    def __str__(self):  #another Constructor
        return(self.ename)
        #return (self.ename, self.sal) invalid bcoz __str__() returns only string data
e1=Emp(1, "John", 20)
print(e1)





