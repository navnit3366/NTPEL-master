def sieve(n):
    prime=[True for i in range(2,n+1)]
    p=2
    while p*p<=n:
        if prime[p-2]==True:
            for i in range(p*2,n+1,p):
                prime[i-2]=False
        p+=1
    print("The prime numbers are: ",end='')
    for p in range(2,n+1):
        if prime[p-2]:
            print(p,end=' ')

sieve(30)
