#file handling/working with the text file
#Example 1: writing data into text file
file = open("C:/demopy/myfile.txt", "w") #mode: r- reading, w- writing, a- append
file.write("This is my first statement.\n")
file.write("Finally 10 lecture completed of Python.")
file.close()
print("Program completed.")


#Example2:reading data from text file
file=open("C:/demopy/myfile.txt", "r")
#print(file.read()) #only first line printed.
print(file.readline())
file.close()

#Example 3 append new data in the text file
file=open("C:/demopy/myfile.txt", "a")
file.write("\nWelldone Durva Varshney")
file.close()
print("Program completed.")


