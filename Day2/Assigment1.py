#Ques 1: Check a given number is positive or negative
#Approch 1
# num=0
# if num>=0:
#     print("Number is positive")
# else:
#     print("Number is negative number")
#
# #Approch 2
# num=float(input("Enter number "))
# if num>=0:
#     print("Number is positive")
# else:
#     print("Number is negative number")
#
# #Ques 2: Check the largest of two numbers
# num1 = float(input("Enter number1 "))
# num2 = float(input("Enter number2 "))
#
# if num1 > num2:
#     print("Number1 is greater:", num1)
# else:
#     print("Number2 is greater:", num2)

# #Ques 3: Check the largest of three numbers
num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))
num3 = float(input("Enter num3: "))

if num1 >= num2 and num1 >= num3:
    print("Number1 is greater:", num1)
elif num2 >= num1 and num2 >= num3:
    print("Number2 is greater:", num2)
else:
    print("Number3 is greater:", num3)



# #Ques 4: Print week number if you provide week name as input.
# weekName = input("Enter week name: ")
# if weekName == "Sunday":
#     print("Week number 1")
# elif weekName == "Monday":
#     print("Week number 2")
# elif weekName == "Tuesday":
#     print("Week number 3")
# elif weekName == "Wednesday":
#     print("Week number 4")
# elif weekName == "Thursday":
#     print("Week number 5")
# elif weekName == "Friday":
#     print("Week number 6")
# elif weekName == "Saturday":
#     print("Week number 7")
# else:
#     print("Not exist week name and week number.")
