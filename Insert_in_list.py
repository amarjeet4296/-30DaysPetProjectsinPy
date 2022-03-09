N = int(input())
A = list(map(int, input().split()))
pos = int(input())
num = int(input())
index = (pos - 1)
A.insert(index, num)
print(*A)'''