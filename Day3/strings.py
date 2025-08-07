#Example1:Way of creating string written in different ways
#from curses.ascii import isdigit

s="welcome"
s='Welcome'
str="Welcome"
str='Welcome'
print(str)

#empty string
name=""
name=''
print(name)

#Example 2:
#mutable or immutable
#immutable - can change the value of the variable
#mutable - cannot change the value of the variable

#string is immutable [If the value is changed after validation then it is immutable
str1 ="Welcome"
print(id(str1))

str1=str1 + "to Python"
print(id(str1))

#Example 3: Use + and * with string
str="Python"
print(str+"Learning") #concatenation/joining
print(str*9) #print the vale multiple times

#slicing
str="welcome"
print(str[1:3])
print(str[2:4])
print(str[:3])
print(str[:6])
print(str[2:])
print(str[:])
print(str[0:])
print(str[1:-1])
print(str[1:-2])
print(str[1:-3])
print(str[1:-4])
print(str[1:-5])
print(str[:-6])
print(str[:-1])

#--------------------------------------------------------------------------
#ord() and chr()

print(ord("A")) #returns the ASCII code of the character
print(ord("a"))

print(chr(67)) #returns character represented by ASCII number
print(chr(76))

#-----------------------------------------------------------------
#max() and min()
print(max("welcome"))
print(min("welcome"))
print(len("welcome"))
print(max("Durvavarshney"))
print(min("Durvavarshney"))
print(len("Durvavarshney"))

#--------------------------------------
#in, not in operators - returns boolean value
greeting = "Welcome"
print("come" in greeting)
print("lome" in greeting)
print("come" in greeting)
print("lome" not in greeting)

#string comparison -  returns boolean value
print("tim" == "tie")
print("free" != "freedom")
print("arrow" > "aron")
print("right" >= "left")
print("teeth" < "tee")
print("yellow" <= "fellow")
print("abc" > " ")

#Testing conditional function - returns boolean value
s = "Welcome to python"
print(s.isalnum()) # is all number
print(s.isalpha()) # is all alphabet
print("Welcome".isalpha())
print("2013".isdigit()) #is all digit
print("first number".isidentifier()) #see python reserved keywords
print(s.islower()) #is all lower case
print(s.isupper()) # is all upper case
print("WELCOME".isupper())
print(" ".isspace())  # is all string has space

#searching for substrings
s = "Welcome to python"
print(s.endswith("thon")) #string end with thon
print(s.startswith("good")) #string start with good
print(s.find("come")) #string has 'come' text #3
print(s.find("become")) #staring has 'become' text if Not found the text then -1
print(s.count("o"))  #2 #Returns number of occurrences of substring the string
print(s.count("x")) #0 when Not Found #Returns number of occurrences of substring the string

#Converting string
s ="string in PYTHON"
s1=s.capitalize()
print(s1) #String in python

s1=s.title()
print(s1) #String In Python

s1=s.lower()
print(s1) #string in python

s1=s.upper()
print(s1) #STRING IN PYTHON

s1=s.swapcase()
print(s1) #STRING IN python

s1=s.replace("in", "on")
print(s1) #strong on PYTHON

#Reverse a string
#approch 1
s = "welcome"
rev_str=""
for i in s:
    rev_str = i+rev_str
print(rev_str)

#approch 2
s = "Welcome"
rev_str = s[::-1]
print(rev_str)

#print add under loop
s = "welcome"
rev_str=""
for i in s:
    rev_str = i+rev_str
    print(rev_str)

