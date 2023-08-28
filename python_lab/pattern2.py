'''
Q5: Write a program to construct the given pattern using a nested loop.

1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
6 6 6 6 6 6
7 7 7 7 7 7 7
8 8 8 8 8 8 8 8
9 9 9 9 9 9 9 9 9

'''

i=1
while(i<10):
        count=1
        while(count<=i):
                print(i,end=" ")
                count+=1
        print("\n",end='')
        i+=1
