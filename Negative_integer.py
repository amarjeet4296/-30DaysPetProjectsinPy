'''Write a program to print all negative numbers from input array A of size N where you have to take integer N and further N elements as input from user.



Problem Constraints

1 <= N <= 1000



-1000 <= A <= 1000



Input Format

A single line representing N followed by N integers of the array A



Output Format

A single line containing elements from the input array which are negative in the same order.'''

A = input().split()
for i in range(len(A)):
    B = int(A[i])
    if B<0:
        print(B, end= " ")