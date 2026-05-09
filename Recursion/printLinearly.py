def printLinearly(i,n):
    if i>n:
        return
    print(i)
    printLinearly(i+1 , n)


printLinearly(1,4)