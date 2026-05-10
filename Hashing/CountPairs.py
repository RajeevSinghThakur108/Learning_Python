def CountPairs(arr:list) -> int :
    map = {}
    for i in arr:
        map[i] = map.get(i,0) +1
        cnt = 0
    for k , v in map.items():
        if v > 1:
            cnt += v//2
    return cnt

arr = [1,1,2,2,3,3]
print(CountPairs(arr))