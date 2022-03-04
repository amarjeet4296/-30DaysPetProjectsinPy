'''Problem Description

Given a number A. Return square root of the number if it is perfect square otherwise return -1.



Problem Constraints

1 <= A <= 108



Input Format

First argument is an integer A.



Output Format

Return an integer which is the square root of A if A is perfect square otherwise return -1.



Example Input

Input 1:

A = 4
Input 2:

A = 1001


Example Output

Output 1:

2
Output 2:

-1'''
class solution:
    def solve(self, A):
        B = abs(A)
        if round(B**(1/2))**2 == A:
            return A**(1/2)
        else:
            return -1