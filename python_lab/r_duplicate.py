'''
Q1: Write a program to remove the duplicate elements from the list.

'''

list=[13,12,13,14,14,12]
empty_list=[]
for i in list:
         if i not in empty_list:
                empty_list.append(i)
print(empty_list)

       
