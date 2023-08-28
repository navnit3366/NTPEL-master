'''
Lab Experiment 6b: Write a program to add members in a set.
'''

s=set({})
n=int(input("Enter the number of elements to add to a new set:"))
print("Enter the elements-")
for i in range(n):
    s.add(int(input()))
print(s)
n=int(input("Enter the number of elements to update to a set:"))
print("Enter the elements-")
for i in range(n):
    s.update([int(input())])
print(s)
