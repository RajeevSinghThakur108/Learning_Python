def add(a,b,c):
    return a + b + c

r=add(2,4,5)
print(r)


r1= lambda n1,n2,n3:n1+n2+n3 # it is one line anonymous func  before : value after : return anonymous 
# func does not have name so store in variable 
print(r1(4,6,7))


check = lambda n: n%2==0
# print(check(13))

n=int(input("enter the value : "))
if check(n):
    print("even")
else:
    print("odd")
