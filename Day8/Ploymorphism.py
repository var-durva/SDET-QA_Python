#Polymorphism  -  one thing can have many form.
#shape - circle, square
#Ploymorphism we can implement using overloading concept

#Example 1: overloading concept (Polymorphism)
class Human:
    def sayHello(self, name=None):
        if name is not None:
            print("Hello " + name)
        else:
            print("Hello")

h=Human()
h.sayHello("Durva")
h.sayHello()

#Example 2:
class Calculation():
    def add(self, a=0,b=0, c=0):
        print(a+b+c)

calobj=Calculation()
calobj.add(1,4,6)
calobj.add()
calobj.add(1,8)





