# Q: Find the non-overlapping recurring substrings from a given string

s='ABCDEGHJABCDGHABCDE'
d={}
for j in range(len(s)-1,1,-1): 
    for i in range(0,len(s)-j+1):
        flag=0
        count=s.count(s[i:j+i])
        if count>1:
            p=s[i:j+i]
            for x in d.values():
                for ele in x:
                    if p in ele:
                        flag=1
                        break
            if flag==0:
                if count not in d:
                    d[count]=[p]
                else:
                    d[count].append(p)


print("The non-overlapping recurring substrings are:",d)
