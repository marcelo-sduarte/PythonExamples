price = float (input("Price is:"))
if price >= 1.00:
    tax = .07
else:
    tax= 0
print("Tax rate is "+ str(tax))

# ------------------------------------------------
country = input(" What are you from?")
if country.lower() == 'canada':
    print("Oh look a Canadian")
else:
    print("you are not from Canada")
# ------------------------------------------------

province = input ("Please insert province name")
tax = 0
 if province in('Alberta','Nunavut','Yukon'):
     tax = 0.05
 elif province == 'Ontario' or 'Quebec':
     tax = 0.13
 else:
     tax = 0.15
print(tax)        