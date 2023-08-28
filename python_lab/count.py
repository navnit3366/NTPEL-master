'''
Lab Experiment 4b: Write a program to count the frequency of each character in a string
'''

s='This is me'
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print("The frequency of characters in the given string '",s,"' is:")
for i in d:
    print(i,': ',d[i])