'''
Q1: Write a program to reverse a given integer.
'''

n=int(input("Enter an integer:"))
num=0
while(n>0):
	rem=n%10
	n//=10
	num=num*10 +rem
print("The reverse is ",num)
