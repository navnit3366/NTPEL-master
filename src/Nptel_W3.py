def contracting(l):
    flag=0
    diff1=abs(l[0]-l[1])
    for i in range(1,len(l)-1):
        diff2=abs(l[i]-l[i+1])
        if diff2>=diff1:
            flag=1
            break
        diff1=diff2

    if flag==1:
        print(False)
    else:
        print(True)

def counthv(l):
    hc=vc=0
    for i in range(1,len(l)-1):
        if l[i-1]>l[i] and l[i+1]>l[i]:
            vc+=1
        if l[i-1]<l[i] and l[i+1]<l[i]:
            hc+=1
    return [hc,vc]

import copy

def leftrotate(m):
    last=len(m)-1
    count=0
    n=copy.deepcopy(m)
    while last>1 or len(m)==2:
        for i in range(0,4):
            k=0
            for j in range(count,last):
                if i==0:
                    m[count][j]=n[j][last]
                elif i==1:
                    m[j][last]=n[last][last-k]
                elif i==2:
                    m[last][last-k]=n[last-k][count]
                else:
                    m[last-k][count]=n[count][j]
                k+=1
        last-=1
        count+=1
        if(len(m)==2):
            break
    return m
