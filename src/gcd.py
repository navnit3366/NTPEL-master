def Euclid_gcd(m,n):
    if m>n and n>=0:
        while n!=0:
            temp=n
            n=m%n
            m=temp
        return m
    else:
        return ("invalid input")

def consecutive_gcd(m,n):
    temp=min(m,n)
    while temp>0:
        if m%temp==0:
            if n%temp==0:
                return temp
            else:
                temp-=1
        else:
            temp-=1
    return("Invalid input")

print("GCD of 60 and 24 using Euclid's Algorithm: ",Euclid_gcd(60,24))
print("GCD of 60 and 24 using Consecutive Method: ",consecutive_gcd(60,24))
