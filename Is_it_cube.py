'''Problem Description

You are given an integer A, You have to tell whether it is a perfect cube or not.

A perfect cube is an integer that is equal to some other integer raised to the third power. If X is a perfect cube of Y, then X = Y3.



Problem Constraints

1 <= A <= 109



Input Format

First and only argument is an integer A.


Output Format

Return 1 if A is a perfect cube, else return 0.'''

def isperfectcube(self, A):
    B = abs(A)
    if round(B**(1/3))**3 == A:
        return 1
    else:
        return 0