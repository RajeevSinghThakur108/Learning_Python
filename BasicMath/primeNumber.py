# tahe number exactly have 2 factor 1 and itself

def checkPrime(p:int) -> int:
    cnt = 0
    i=2
    while(i*i<=p):
        if(p%i == 0):
            cnt = cnt + 1
        i=i+1
    return cnt

p = int(input("enter a val : "))
print ("prime number" if checkPrime(p) == 0 and p>1 else "not a prime number")
