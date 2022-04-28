print("=============== Avaliation for loan ==============")
print()
print("For each of these questions, please provide a 1-10 rating:")
print()
large_loan = int(input("How large is the loan?"))
credit = int(input("How good is your credit history?"))
income = int(input("How high is your income?"))
down_payment = int(input("How large is your down payment?"))
give_loan = True
#------------------------------------------------
# process to verify loan score 5
#------------------------------------------------
if large_loan >= 5:
    if credit >= 7 and income >= 7:
        give_loan == True
    elif credit >= 7 or income >= 7:
        if down_payment >= 5:
            give_loan == True
        else:
            give_loan == False
    else:
        give_loan == False
#------------------------------------------------
# process to verify loan score > 5
#------------------------------------------------
elif large_loan <5:
    if credit < 4:
        give_loan == False
    else:
        if income >= 7 or down_payment >= 7:
            give_loan == True
        elif income >= 4 and down_payment >= 4:
            give_loan == True
        else:
            give_loan == False
#------------------------------------------------
# Message Screen
#------------------------------------------------
if give_loan:       
    print("Your decision is Yes. The loan was accept")
else:
    print("Your decision is no. The loan wasn't accept")
