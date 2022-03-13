A = [1,2,5,1,5,1]
freq = {}
for num in A:
    if num in freq:
        freq[num]+=1
    else:
       freq[num] = 1
print(freq)
for key, value in freq.items():
    for i in A:
        if key == i:
            print(value, end = " ")
