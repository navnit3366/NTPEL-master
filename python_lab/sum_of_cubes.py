
'''
Q3 (Viva) : Write a Python program for finding cube sum of first n natural numbers.
'''
sum=0
n=int(input("Enter the value of n: "))
for i in range(1,n+1):
    sum += (i*i*i)
print("The sum of the cubes of first n natural numbers = ", sum)
