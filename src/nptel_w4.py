def frequency(l):
    l.sort()
    l.append(-1)
    d={}
    temp=[l[0]]
    count=0
    for i in l:
        if i in temp:
            count+=1
        else:
            if count in d:
                d[count].append(temp[0])
            else:
                d[count]=temp
            count=1
            temp=[i]
    return (d[min(d)],d[max(d)])

def onehop(l):
    list=[]
    for i in l:
        for j in l:
            if i[1]==j[0] and i[0]!=j[1] and (i[0],j[1]) not in list:
                list.append((i[0],j[1]))
    list.sort()
    return list         
    



