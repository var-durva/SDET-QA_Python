#Exception handling
#Exception is an event which will case program termination
#try #except
#else (using very rare)

#Except - executes only when exception occurred.
#else - executes only when exception not occurred.
#finally - always executes.



#example 1:
print("This is starting point of program.")
print("This is starting point of program.")
print("This is starting point of program.")
try:
    print(x)
except:
    print("Exception occurred")

print("This is end of the program")
print("This is end of the program")
print("This is end of the program")

#Example 2:
print("This is starting point of program.")
print("program in progress")
try:
    print(10/0)
except ZeroDivisionError:
    print("Exception occurred and handled.")
print("Program complemented")

#Example 3: Multiple except blocks --try, except, else, finally
try:
    num1, num2 =10, 0
    result=num1/num2
    print("Result is: ", result)
except ZeroDivisionError:
    print("Thrown ZeroDivisionError Exception.")
except SyntaxError:
    print("Thrown SyntaxError Exception.")
except:
    print("Exception handled.")
else:
    print("No exception occurred.")
finally:
    print("Always execute")


#Example 4: raising our exception.
def enterage(num):
    if num <0:
        raise ValueError("only integers are allowed")
    if num%2==0:
        print("even")
    else:
        print("odd")

# enterage(24)
# enterage(23)
# enterage(0)
print("Checking number is even or odd by calling function.")
num=-1
try:
    enterage(num)
except ValueError:
    print("Value error exception occurred and handled.")
print("program complemented.")