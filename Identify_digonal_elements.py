'''Identify the digonal elements'''


A = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(A)):
    for j in range(len(A[i])):
        if i == j:
            print(A[i][j])