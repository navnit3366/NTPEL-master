'''
Q. Create the following pattern:

*     *

 *   *
      
  * * 
      
   *  

'''

for i in range(4):
    j=0
    while j!=i:
        print(" ",end="")
        j+=1
    print("*",end=" ")
    if i==3:
        break
    elif i==0: 
        print("    ",end="")
    elif i==1:
        print("  ",end="")
    print("*\n")
    
    
