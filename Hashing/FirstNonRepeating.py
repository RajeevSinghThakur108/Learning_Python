def nonrepat(arr : int ) -> int:
    map = {}
    for i in arr:
        map[i] = map.get(i,0) + 1
    for i in arr:
        if map[i] == 1:
            return i
arr = [1,2,1,3,2,4]
print(nonrepat(arr))
    
   



