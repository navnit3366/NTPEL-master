'''
Q: Write a program that calls a function that takes a list of words as parameter 
    and returns the length of the longest element.
'''

def fun(l):
    key=0
    for i in l:
        if len(i)>key:
            key=len(i)
    return key

print("length of longest word is: ",fun(['sdjgdvjdgja2793hdjf','dhgfk','hhd','a','hdjhffjbskc']))
