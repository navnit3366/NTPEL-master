#Q: Write a Python program to find the median among three given numbers.

num=[]
for i in range(3):
    num.append(int(input("Enter a number: ")))
print("The median of three given number: ",end='')

if num[0]>num[1] and num[0]>num[2]:
    if num[1]>num[2]:
        print(num[1])
    else:
        print(num[2])

if num[1]>num[0] and num[1]>num[2]:
    if num[0]>num[2]:
        print(num[0])
    else:
        print(num[2])

if num[2]>num[1] and num[2]>num[0]:
    if num[1]>num[0]:
        print(num[1])
    else:
        print(num[0])

    
