def highestCount(arr:int) -> int:
    freq = {}
    for i in arr:
        freq[i] = freq.get(i,0) + 1

    temp = 0
    ans = 0
    for k , v in freq.items():
        if v > temp:
            temp = v
            ans = k
    return ans

arr = [1,2,2,3,2]
print(highestCount(arr))

