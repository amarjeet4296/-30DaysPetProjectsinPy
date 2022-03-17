t = int(input())
for i in range(t):
    A = list(map(int, input().split()))
    d = 0
    for j in range(len(A)-1):
        if A[j] < A[j+1]:
            d = 1

    if (d == 0):
        print("sorted")
    else:
        print("Not Sorted")