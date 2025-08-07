#InputFunction: How to take input from user & Type conversion: Input from the console window
num1=input("Enter first number:")
num2=input("Enter second number:")

print(type(num1))   #str
print(type(num2))

#What ever value provide in the console window consider as string

print(num1 + num2)

#approach 1  change into int
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

print(type(num1))
print(type(num2))

print(num1 + num2)

#approach 2  change into int
num1=input("Enter first number:") #10.7
num2=input("Enter second number:") #23.09

print(int(num1) + int(num2))

#decimal number
num1=input("Enter first decimal number:")
num2=input("Enter second decimal number:")

print(num1 + num2) #10.723.09

print(float(num1) + float(num2)) #10.723.09