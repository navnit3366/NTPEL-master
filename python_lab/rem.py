'''
1.Write a program that prompts the user for two integers,
and then prints them out in a sentence like

The quotient of 13 and 3 is 4 with a remainder of 1
'''

print("Enter 2 integers:")
a=int(input())
b=int(input())
rem=a%b
q=a/b
print("The quotient of",a," and " ,b, " is " ,int(q), "with a reminder of ",rem)  
