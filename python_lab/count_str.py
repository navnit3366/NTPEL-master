'''
Q1. Write a program to count the number of strings where the string's length is equal or greater than 2 
	and it's first and last characters are the same from a given list of strings.
'''

l=['asf','jdff','ende','qq']
count=0
for i in l:
    if len(i)>=2 and i[0]==i[len(i)-1]:
        count+=1
print(count)
	
