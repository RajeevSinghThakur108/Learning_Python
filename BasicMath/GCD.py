def minOf(a:int , b:int) -> int:
    return a if a<b else b

   
def gcd(a:int , b:int) -> int:
    n=minOf(a,b)
    for i in range(n , 1 , -1):
        if(a%i == 0 and b%i==0):
            return i
    return 1

print(gcd(12,18))
            



 



    