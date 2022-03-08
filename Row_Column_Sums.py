'''You are given a matrix A, you have to return a vector containing sum of each row elements followed by each column elements of the matrix .

NOTE: In the resultant vector of integers there will be rows+columns elements where ans[i] is the sum of ith row elements and ans[rows+j] is the sum of jth column.



Problem Constraints

1 <= A.size() <= 1000

1 <= A[i].size() <= 1000

1 <= A[i][j] <= 1000



Input Format

First argument is vector of vector of integers representing matrix A.



Output Format

You have to return a vector of integers after doing required operations.'''

A = [[1,2,3],[4,5,6],[7,8,9]]

result = []

for i in range(len(A)):
    row = 0
    for j in range(len(A[i])):
        row += A[i][j]
    result.append(row)
for i in range(len(A[i])):
    col = 0
    for j in range(len(A)):
        col += A[j][i]
    result.append(col)
print(result)