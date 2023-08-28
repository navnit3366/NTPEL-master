'''
Lab Experiment 7a: Write a python function to find the max of 3 numbers
'''

def maxf(a, b, c):
    l=[a,b,c]
    key=0
    for i in l:
        if i>key:
            key=i
    return key

print(maxf(1,-34,28))