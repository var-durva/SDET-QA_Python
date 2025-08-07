#FormattingOutput
name = "John"
age = 20
sal = 500
print(name)
print(age)
print(sal)

#Approch 1
name, age, sal = "John", 30, 500
print(name, age, sal)

#Approch 2
print("Name is:",name)
print("Age is:",age)
print("Salary is:",sal)

#Approch3 by % operator
print("Name is:%s Age is:%d Salary is: %g" %(name, age, sal))

#Approch4 {}
print("Name is:{} Age is:{} Salary is: {}" .format(name, age, sal))
print("Age is:{} Name is:{} Salary is: {}" .format(name, age, sal))
print("Age is:{} Name is:{} Salary is: {}" .format(age, name, sal))
