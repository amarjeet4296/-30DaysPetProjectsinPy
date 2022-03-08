'''
0 0 0 0 1 0 0 0 0
0 0 0 1 2 2 0 0 0
0 0 1 2 3 3 3 0 0
0 1 2 3 4 4 4 4 0
1 2 3 4 5 5 5 5 5
'''
'''Numerical Diamond'''


A = int(input())
for i in range(1, A+1):
    for j in range(i, A):
        print("0 ", end = "")
    for j in range(1, i+1):
        print(j, end = " ")
    for j in range(1, i):
        print(i, end=" ")
    for j in range(i, A):
        print("0", end=" ")
    print()