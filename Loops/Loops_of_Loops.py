table = int(input("How many columns and rows do you want in your multiplication table?"))
table = table + 1
#count = 0,
# columns
for i in range (1,table):
    for j in range (1,table):
        multiply = i * j
        print(f"{multiply:3}", end= " ")
    print()





