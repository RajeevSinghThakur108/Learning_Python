def reverse(a : int ) -> int:
    rev = 0
    sign = 1
    if a<0:
        sign = -1
        a=abs(a)
    while a > 0:
        n=a%10
        rev = rev*10 + n
        a=a // 10
    return sign*rev 

print(reverse(-123))


