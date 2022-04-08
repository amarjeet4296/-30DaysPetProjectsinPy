

arr = list(map(int, input().split()))
n = len(arr)
Suf = [None]*n
Suf[n-1] = arr[n-1]
for i in range(n-2,-1,-1):
    Suf[i] = Suf[i+1] + arr[i]
print(Suf)