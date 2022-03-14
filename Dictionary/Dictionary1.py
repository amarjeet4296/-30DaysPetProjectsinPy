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
    
#Adding new key, value in a dictionary
currency['Polland'] = 'Zolty'

#Create an empty dictionary
country_currency = {}

#wipe out an existing dictionary
'''currency = {}'''

#Loop in the dictionary
for key in currency:
    print(key)
    print(currency[key])
