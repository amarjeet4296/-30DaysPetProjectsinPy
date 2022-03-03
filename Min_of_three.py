'''Write a program to input three numbers(A, B & C) from user and print the minimum element among A, B & C in each line.



Problem Constraints
1 <= A <= 1000000

1 <= B <= 1000000

1 <= C <= 1000000



Input Format
First line is a single integer A.
Second line is a single integer B.
Third line is a single integer C.



Output Format
One line containing an integer as per the question.'''

A,B,C = map(int, input().split())

print(min(A,B,C))
'''if A<B and A<C:
    print(A)
elif B<C:
    print(B)
else:
    print(C)'''