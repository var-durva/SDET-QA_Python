#Control statements
# 3) jumping statements
#break
for i in range(1,10):
    if i==5:
        break
    print(i)
print("Program exited!")

#continue [skip that particular value]
for i in range(1,10):
    if i==5:
        continue
    print(i)
print("Program exited!")

#continue [skip that particular values]
for i in range(15,25):
    if i==16 or i==19 or i==23:
        continue
    print(i)
print("Program exited!")


