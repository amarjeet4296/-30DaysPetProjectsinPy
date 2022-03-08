'''Write a program to input an integer N from user and print hollow inverted right triangle star pattern of N lines using '*'.
See example for clarifications.
Problem Constraints
1 <= N <= 1000
Input Format
First line is an integer N
Output Format:
N lines conatining only char '*' as per the question.
Input 1:

7
Output:
*******
*    *
*   *
*  *
* *
**
*
'''
n = int(input())
print('*'*n)
for i in range(n-2):
	print('*'+ (' '*((n-i-3))) + '*' )
if n>1:
	print('*')