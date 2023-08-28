'''
Lab Experiment 7c: Write a python function to calculate the factorial of a number
'''

def fac(n):
    if n==0:
        return 1
    else:
        return n*fac(n-1)

n=int(input("Enter a number: "))
if n>=0:
    print("Factorial of ",n," is ",fac(n))
else:
    print("Invalid Input")
