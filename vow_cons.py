str=input("Please enter a string as you wish: ");
vowels=0

L = []
for i in str:
    if(i == 'a'or i == 'e'or i == 'i'or i == 'o'or i == 'u'):
        vowels=vowels+1 #vowel counter is incremented by 1
#should be outside the scope of for loop not inside, all else is correct.
Rest = len(str)- vowels
L.append(vowels)
L.append(Rest)


print(vowels)
print(Rest)