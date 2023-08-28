
# Q: Find the longest recurring substring in a given string

s='12345123576584644444412345'
d={}
flag=0
for j in range(len(s)-1,1,-1): 
    for i in range(0,len(s)-j+1):
        count=s.count(s[i:j+i])
        if count>1:
            p=s[i:j+i]
            if flag==0:
                flag=1
            if count not in d:
                d[count]=[p]
            elif s[i:j+i] not in d[count] :
                d[count].append(p)
    if flag==1:
        flag=-1
        print("The longest repeating substrings are: ",d)
print("The repeating substrings are:",d)