def rev(a: int) -> int :
    sign = 1
    if a<0:
        sign = -1
    a=a*sign
    rev=0
    while a>0:
        n=a%10
        rev = rev*10 + n
        a = a//10
    return sign * rev

def checkPalindrome(b : int ) -> int:
    c = rev(b)
    if b == c:
        return 1
    else:
        return 0
    
    
if checkPalindrome(-1331) == 1 :
    print("Palindrome")
else:
    print("not a Palindrome")



