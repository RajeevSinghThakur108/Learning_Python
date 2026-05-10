def FreqCount(arr:list) -> dict:
    freq = {}
    for i in arr:
        freq[i] = freq.get(i,0)+1


    return freq

arr = [1,2,1,3,2,1,4]
# print(FreqCount(arr))

for k, v in FreqCount(arr).items():
    print("Key " , k , "Value " , v)

