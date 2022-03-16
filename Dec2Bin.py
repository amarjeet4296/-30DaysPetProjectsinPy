n = int(input())
final_value = 0
while (n!=0):
    remainder = n%2
    z = remainder[::-1]
    print(z)
    n = n//2