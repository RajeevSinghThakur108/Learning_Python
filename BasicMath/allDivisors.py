def allDiv(val: int) -> list:
    arr=[]
    i=1
    while i * i <= val:
        if val%i == 0:
            arr.append(i)
            if val//i != i:
                arr.append(val//i)
        i=i+1
    return arr
print(allDiv(12))

