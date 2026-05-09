def revArray(a, left, right):
    if left >= right:
        return a
    a[left], a[right] = a[right], a[left]
    return revArray(a, left+1, right-1)

a = [1,2,3,4,5]
print(revArray(a, 0, len(a)-1))
    