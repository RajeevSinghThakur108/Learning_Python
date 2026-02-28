# create matrix 

# col = []
# for i in range(5):
#     row = []
#     for j in range(4):
#         row.append(j)
#     col.append(row)

# for i in col:
#     print(i)


# Row-wise Sum of a Matrix

# Matrix = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]

# rowWise = []
# for col in Matrix:
#     sum = 0
#     for row in range(len(col)):
#         sum = sum + col[row]
#     rowWise.append(sum)
# print(rowWise)



# Column-wise Sum of a Matrix

# Matrix = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]

# colWise = []
# for col in range(len(Matrix[0])):
#     total = 0
#     for row in range(len(Matrix)):
#         total=total + Matrix[row][col]
#     colWise.append(total)
# print(colWise)




Matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

dignal =[]
total =0 
for i in range(len(Matrix[0])):
    
    for j in range (len(Matrix)):
        if i == j :
            total = total + Matrix[i][j]
print(total)


    
