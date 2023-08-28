'''
Q2: Write a program to display the common elements present in the given 2 lists.
'''

l1=[34,56,98,6,2,2,2,8,1,3,90]
l2=[88,47,92,44,5,2,1,2,34]
l3=[]
print('The common elements are:')
for i in l1:
        if i in l2 and i not in l3:
                l3.append(i)
                print(i)
