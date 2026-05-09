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




# Matrix = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]
# total =0 
# for i in range(len(Matrix[0])):
#     for j in range (len(Matrix)):
#         if i == j :
#             total = total + Matrix[i][j]
# print(total)

# for row  in range(len(Matrix)):
#     for col in range(len(Matrix)):
#         if row + col == len(Matrix) - 1:
#             total = total + Matrix[row][col]
# print(total)
    

# Spiral matrix 



# Matrix = [
#   [1,2,3,4,5,6],
#   [7,8,9,10,11,12],
#   [13,14,15,16,17,18],
#   [19,20,21,22,23,24],
#   [25,26,27,28,29,30]
# ] 
# top = 0;
# left = 0;
# bottom = len(Matrix) - 1;
# right = len(Matrix[0]) -1;
# result = [];
# while(top <= bottom and left <= right):
#     for i in range(left , right + 1):
#         #  move left to right across the top row
#         result.append(Matrix[top][i])
#     top +=1
#     for i in range(top, bottom +1):
#         result.append(Matrix[i][right])
#     right -=1

#     if top <= bottom:
#         for i in range(right, left-1, -1):
#             result.append(Matrix[bottom][i])
#         bottom -=1
    
#     if left <= right:
#         for i in range(bottom , top-1 ,-1):
#             result.append(Matrix[i][left])
#         left +=1


# print(result)



# Transpose Matrix

# Matrix = [
#     [1,2,3],
#     [4,5,6]
# ]

# trans = []
# rows = len(Matrix)
# cols = len(Matrix[0])
# for col in range(cols):
#     new_row = []
#     for row in range(rows):
#         # Matrix[row][col] = Matrix[col][row]
#         new_row.append(Matrix[row][col])
#     trans.append(new_row)
# print(trans)

# rev = []
# for row in range(len(trans)):
#     nrow = []
#     for col in range(len(trans[0]) -1 , -1 ,-1):
#         nrow.append(trans[row][col])
#     rev.append(nrow)
# print(rev)


# def check():
#     Matrix = [
#   [1, 4, 7, 11],
#   [2, 5, 8, 12],
#   [3, 6, 9, 16],
#   [10,13,14,17]
# ]
#     target = 5
#     row = len(Matrix)
#     col = len(Matrix[0])
#     for i in range(row):
#         for j in range(col):
#              if Matrix[i][j] == target:
#                  return True
#     return False
# print(check())


Matrix = [
  [1, 4, 7, 11],
  [2, 5, 8, 12],
  [3, 6, 9, 16],
  [10,13,14,17]
]
# print(Matrix)
# rows = len(Matrix)
# cols = len(Matrix[0])

# for row in range(rows):
#     for col in range( cols):
#         print(Matrix[col][row] , end=" ")
#         # Matrix[col][row],Matrix[row][col] = Matrix[row][col],Matrix[col][row]
#         # Matrix[row][col], Matrix[col][row] = Matrix[col][row], Matrix[row][col]
#     print()



       
    









            
