'''
Linear Search 2
Given an array containing duplicate numbers and a target value, find the index of 2nd occurence of the target value
Sample Input:

6
9 2 8 2 4 2
2
'''

A = int(input())
N = list(map(int, input().split()))
res = {}
for i in N:
    res[i] = N.count(i)
L = 0
for k,v in res.items():
    if v>1:
        for i in range(len(N)):
            if (N[i] == k):
                print(i)


