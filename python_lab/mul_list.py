#Q: Write a Python function to multiply all the numbers in a list

def mul(list):
    product=1
    for i in list:
        product*=i
    return product

print(mul([2,3,4,5]))
