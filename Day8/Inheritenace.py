#Inheritenace:  Acquiring all the attributes(variables) & behavior(methods) from one class to another class is called as inheritance.
#Class A -> a,b,c   m1() m2() -> A is parent of N class (Base class/Super class)
#Class B(A) -> x,y,z  m3() ----> B is child of A class (subclass/Derived class)
#whatever methods are belong to parent class A there also belong to child class B.

#Objectives of Inheritance:
#1. Code re-usability
#2. Avoid duplication

#Types of Inheritance
#1. Single
#2. Multilevel
#3.Hierarchy
#4. Multiple


#Example 1: Single Inheritance
class A:
    def m1(self):
        print("this is m1 method from class A")
class B(A):
    def m2(self):
        print("this is m2 method from class B and B is child of class A")

bobject=B()
bobject.m1()
bobject.m2()

#Example 2: Single Inheritance
class A:
    x,y = 10,20
    def m3(self):
        print(self.x+self.y)
class B(A):
    a,b =100,200
    def m4(self):
        print(self.a-self.b)

bobj=B()
bobj.m3()
bobj.m4()

#Example 3: Multilevel Inheritance
class A:
    x,y = 20,20
    def m1(self):
        print(self.x+self.y)
class B(A):
    a,b =300,200
    def m2(self):
        print(self.a-self.b)
class C(B):
    i,j=5,2
    def m3(self):
        print(self.i*self.j)

cobj=C()
cobj.m1()
cobj.m2()
cobj.m3()

#Example 4: Hierarchy Inheritance
class A:
    x,y = 20,20
    def m1(self):
        print(self.x+self.y)
class B(A):
    a,b =300,200
    def m2(self):
        print(self.a-self.b)
class C(A):
    i,j=5,2
    def m3(self):
        print(self.i*self.j)

bobj=B()
bobj.m1()
bobj.m2()
cobj=C()
cobj.m1()
cobj.m3()

#Example 5: Multiple Inheritance
class A:
    x,y = 20,20
    def m1(self):
        print(self.x+self.y)
class B:
    a,b =300,200
    def m2(self):
        print(self.a-self.b)
class C(A,B):
    i,j=5,2
    def m3(self):
        print(self.i*self.j)

cobj=C()
cobj.m1()
cobj.m2()
cobj.m3()

#Example 6: overriding concept and invoking m1 method by child class B
class A:
    def m1(self):
        print("this is m1 method class A")
class B(A):
    def m1(self):
        print("this is m1 method class B")

bobj=B()
bobj.m1()

#Example 7: overriding concept and invoking m1 method by parent class A or calling parent class method using child class (super())
class A:
    def m1(self):
        print("this is m1 method class A")
class B(A):
    def m1(self):
        print("this is m1 method class B")
        super().m1() #using so that m1 function can invoke by parent class A.
bobj=B()
bobj.m1()

#Example 8:
class A:
    a,b=10,20
class B(A):
    i,j =100,200
    def m(self, x,y):
        print(x+y)
        print(self.i+self.j)
        print(self.a+self.b)
bobj=B()
bobj.m(1, 500)

#Example 9: Overriding variables
class Parent:
    #name = input("Enter name: ")
    name = "Durva"

class Child(Parent):
    #name = input("Enter name: ")
    name="Varshney" #overriding variable value

cobj=Child()
print(cobj.name) #lastest value printed

#Example 9: Overriding variables and invoking parent variable
class Parent:
    name = "Durva"

class Child(Parent):
    name="Varshney" #overriding variable value
    def test(self):
        print(super().name)

cobj=Child()
print(cobj.name) #lastest value printed
cobj.test()


#Example 10: overriding the methods
class Bank:
    def rateOfInterest(self):
        return 0
class XBank(Bank):
    def rateOfInterest(self):
        return 10
class YBank(Bank):
    def rateOfInterest(self):
        return 12

objX = XBank()
print(objX.rateOfInterest())

objY = YBank()
print(objY.rateOfInterest())






