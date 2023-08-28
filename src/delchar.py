def delchar(s,c):
    s=list(s)
    a=''
    while c in s:
        s.remove(c)
    for i in s:
        a=a+i
    return a
