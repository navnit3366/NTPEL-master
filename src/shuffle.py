def shuffle(l1,l2):
    l3=[]
    len1=len(l1)
    len2=len(l2)
    for i in range(max(len1,len2)):
        if i<len1:
            l3.append(l1[i])
        if i<len2:
            l3.append(l2[i])
    return l3
    
