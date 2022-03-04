'''Problem Description

You are given a constant array A and an integer B.

You are required to return another array where outArr[i] = A[i] + B.



Problem Constraints

1 <= A.size() <= 10000

1 <= A[i] <= 10000

1 <= B <= 10000



Input Format

First argument is a constant array A.

Second argument is an integer B.



Output Format

You have to return an integer array.'''

def solve(self, A,B):
    # Constant here we convert tuple into list
    A = list(A)
    C = []
    for i in range(len(A)):
        d = int(A[i])+B
        C.append(d)
        return C