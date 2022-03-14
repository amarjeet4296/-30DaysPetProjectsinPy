currency = {
    "India": "INR",
    "USA": "Dollar",
    "Spain": "Euro",
    "Japan": "Yen",
    "Italy": "Euro",
}
#1 calling one value in a dictionary
print(currency['India'])

#2. Calling all values in a dictionary
for k, v in currency.items():
    print(k, " = " , v)