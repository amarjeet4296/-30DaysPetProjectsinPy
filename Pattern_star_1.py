#1. Pattern Star Problem
T = int(input())
for i in range(1, T+1):
    for j in range(i):
        print("*", end = " ")
    print()

# 2. Star numeric problem
'''1
2 2
3 3 3
4 4 4 4
5 5 5 5 5'''
T = int(input())
for i in range(1, T+1):
    for j in range(i):
        print(i, end = " ")
    print()



# 3. Pattern Problem
'''1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''

T = int(input())
for i in range(1, T+1):
    C = 0
    for j in range(i):
        C+=1
        print(C, end = " ")
    print()