'''Write a program to input two numbers(A & B) from user and print the minimum element among A & B in each line.'''

'''Problem Constraints
1 <= A <= 1000000

1 <= B <= 1000000



#Input Format
First line is a single integer A.
Second line is a single integer B.



Output Format
One line containing an integer as per the question.'''


A, B = map(int, input().split())
if A>B:
    print(B)
else:
    print(A)