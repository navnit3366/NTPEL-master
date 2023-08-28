'''
Lab Experiment 5a: Write a program to find the sum and average of the given numbers using list.

'''

list=[]
sum=0
n=int(input("Enter the number of elements:"))
print("Enter the elements:")
for i in range(n):
	ele=int(input())
	list.append(ele)
	sum+=list[i]
avg=sum/n
print("Sum = ",sum," avg = ",avg)
