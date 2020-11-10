# mat = [ [1,2,3],
#         [4,5,6],
#         [7,8,9]]

mat = [[7,9,8,6,3],
       [3,9,4,5,2],
       [8,1,10,4,10],
       [9,5,10,9,6],
       [7,2,4,10,8]]

sum = 0
n =len(mat)
mid = n//2
for i in range(n):
    sum+=mat[i][i]
    sum+=mat[n-i-1][i]

if n%2 == 1:
    sum -= mat[mid][mid]

print(sum)
