N = list(map(int, input().split()))
n = len(N)
pre = [None]*n
pre[0] = N[0]
for i in range(1, n):
    pre[i] = pre[i-1] + N[i]
print(pre)
# '''

# '''