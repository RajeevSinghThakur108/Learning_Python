def countTotalDigit (a : int) -> int:
    cnt = 0
    a=abs(a)
    while(a>0):
        a=a//10
        cnt = cnt + 1
    return cnt

def power(digit : int , n : int ) -> int:
    res = 1
    while(n>0):
        res=res*digit
        n=n-1
    return res

def totalOfDigit(a : int) -> int:
    temp = a
    n = countTotalDigit(a)
    total = 0
    while(temp>0):
        total = total + power((temp%10), n)
        temp=temp//10
    return total

def check(a):
    if totalOfDigit(a) == a:
        print("armstrong")
    else:
        print(" Not an armstrong ")

check(371)
    
   

 
