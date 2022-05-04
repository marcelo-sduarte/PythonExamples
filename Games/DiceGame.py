# Develop by Marcelo Duarte


import random

again = "yes"
score_total = 0

while again == "yes" or again == "y":
    score = 50
    listdice =[]


    for i in range(5):
        numberDice = random.randint(1, 6)
        listdice.append(numberDice)
    print("============================")
    print()
    print(f"Rollind Dice..{listdice}")

   
    for i in range(len(listdice)):
        if listdice[i] == 1:
            score += 100
        elif listdice[i] == 5:
            score += 50
    score_total += score    
            

    print(f"Score round: {score}")
    print(f"Score total: {score_total}")
    print()
    print("============================")    
    again = input("Do you want to continue? Yes or Not").lower()
 
print("******************************************************") 
print()    
print(f"Thanks for playing, your score final is: {score_total}")    
print()
print("******************************************************")     
