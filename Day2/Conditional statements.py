#Control statements
#1) Conditional statements
    #if else elif
#2) Looping statements
    # while for
#3) Jumping statements
    #break continue
#----------------------------------------------------------
#Conditional statements
#Example 1: Print a person is eligible for vote or not

age=19
if age>=18:
    print("Eligible for vote")
else:
    print("Not eligible for vote")

#Example 2 written boolean value

if True:
    print("True statements")
else:
    print("False statements")

#Example 3 written boolean value

if False:
    print("True statements")
else:
    print("False statements")

#Example 4 written boolean value as 0 and 1

if 1:
    print("True statements")
else:
    print("False statements")

#Example 5 written boolean value as 0 and 1

if 0:
    print("True statements")
else:
    print("False statements")

#Example 6 Find a number is even or not
num=11
if num%2==0:
    print("Number is an even number")
else:
    print("Number is an odd number")

#Example 7: if else in single line (ternary mumber)
num =29
print("Even number") if num%2==0 else print("Odd number")

#Example 8: if else in single line with multiple statements

# num =29
{print("Even number"), print("Divided by 2")} if num%2==0 else {print("Odd number"), print("Not divided")}

 #Example 8: Multiple conditions using elif

weekno =10
if weekno==1:
    print("Sunday")
elif weekno==2:
    print("Monday")
elif weekno==3:
    print("Tuesday")
elif weekno==4:
    print("Wednesday")
else:
    print("Invalid weekName")
