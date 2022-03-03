'''Problem Description

Write a program to print sum of elements of the input array A of size N where you have to take integer N and further N elements as input from user.



Problem Constraints

1 <= N <= 1000

1 <= A <= 1000



Input Format

A single line representing N followed by N integers of the array A



Output Format

A single integer containing sum of elements from the input array.'''

A = input().split()
S = 0
for i in range(1, len(A)):
    S += int(A[i])
print(S)