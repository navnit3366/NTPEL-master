'''
Lab Experiment 7b: Write a python function to multiply all the numbers in a list
'''

def mul(l):
    prod=1
    for i in l:
        prod*=i
    return prod

print(mul([2,3,4,5]))