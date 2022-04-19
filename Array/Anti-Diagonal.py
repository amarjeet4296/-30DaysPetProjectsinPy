#--InterviewBit--

'''
Problem Description

Give a N*N square matrix, return an array of its anti-diagonals. Look at the example for more details.
Example:

Input:

1 2 3
4 5 6
7 8 9
Return the following:
[
  [1],
  [2, 4],
  [3, 5, 7],
  [6, 8],
  [9]
]


Input:
1 2
3 4
Return the following:
[
  [1],
  [2, 3],
  [4]
]
'''

class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        n = len(A)

        dia = []
        for k in range(2*n-1):
            temp = []
            for i in range(k+1):
                j = k-i
                if j >= 0 and j < n and i < n:
                    temp.append(A[i][j])
            dia.append(temp)
        return dia
