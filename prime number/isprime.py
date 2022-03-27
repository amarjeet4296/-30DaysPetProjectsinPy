def isprime(N):
    for i in range(1, N+1):
        Count = 0
        if N%i == 0:
            Count+=1
    if Count == 2:
        return True
    else:
        return False


print(isprime(100))


