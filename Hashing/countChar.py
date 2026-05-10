# s = "abcabcd"
# hash_char = {}
# for c in s:
#     if c in hash_char:
#         hash_char[c] += 1
#     else:
#         hash_char[c] = 1

# print(hash_char)


s = "abcabcd"
map = {}
for i in s:
    map[i] = map.get(i,0) + 1

if map.get("k"):
    print("yes")
else:
    print("No")
