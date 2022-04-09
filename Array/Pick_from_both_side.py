'''
Problem Description

You are given an integer array A of size N.

You can pick B elements from either left or right end of array A to get the maximum sum.

Find and return this maximum possible sum.

NOTE: Suppose B = 4, and array A contains 10 elements, then

You can pick the first four elements or can pick the last four elements, or can pick 1 from front and 3 from the back, etc. You need to return the maximum possible sum of elements you can pick.


Problem Constraints

1 <= N <= 105

1 <= B <= N

-103 <= A[i] <= 103



Input Format

First argument is an integer array A.

Second argument is an integer B.



Output Format

Return an integer denoting the maximum possible sum of elements you picked.



Example Input

Input 1:

 A = [5, -2, 3 , 1, 2]
 B = 3
'''

arr = list(map(int, input().split()))
B = 4

n = len(arr)
pre = [None] * n
Suf = [None]*n
pre[0] = arr[0]
for i in range(1, n):
    pre[i] = pre[i - 1] + arr[i]
print(pre)

Suf[n-1] = arr[n-1]
for i in range(n-2,-1,-1):
    Suf[i] = Suf[i+1] + arr[i]
print(Suf)
Li = [pre[B-1],Suf[n-B]]
for i in range(1,B):
    MaxSum = pre[i-1] + Suf[n-(B-i)]
    Li.append(MaxSum)
Z = max(Li)

print(Z)
