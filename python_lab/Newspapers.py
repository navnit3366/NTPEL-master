'''
Q2. Students of District College have a subscription to English and French newspapers.
Some students have subscribed to only English, some to only French and few to both.
For the given 2 sets of rollnumbers, one set of students subscribed to English and the other to French newspapers,
find the number of students who have subscribed only to English newspaper.
'''

s1=set({})
s2=set({})
n=int(input("Enter the number of students who have subscribed to English newspapers:"))
print("Enter their rollnumbers-")
for i in range(n):
    s1.add(int(input()))
print("Rollnumber of students with English Newspaper Subscription: ",s1) 
n=int(input("Enter the number of students who have subscribed to French newspapers:"))
print("Enter their rollnumbers-")
for i in range(n):
    s2.add(int(input()))
print("Rollnumber of students with French Newspaper Subscription: ",s2)
print("The number of students who have subscribed to only English Newspaper: ",len(s1-s2))
