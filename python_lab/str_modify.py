'''
Q3. Read a given string, change the character at a given index and then print the modified string.
'''
s=input("Enter a string: ")
i=int(input("Enter the index to modify at: "))
c=input("Enter the char: ")
s=s[:i]+c+s[i+1:]
print(s)
