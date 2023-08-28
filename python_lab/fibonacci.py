'''
Q4: Write a program to get the fibonacci's series b/w 0 to 50
'''

a=0
b=1
print("The fibonacci series is here:\n",a,b,end=" ")
while( (a+b) <= 50):
        c=a+b
        a=b
        b=c
        print(c,end=" ")
	
print(" ......and it goes on") 
	
