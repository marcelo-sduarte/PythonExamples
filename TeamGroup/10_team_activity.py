

accounts = []
balances = []

new_account = ''
total = 0
print('Enter the names and balances of bank accounts (type: quit when done) ')

while new_account != 'quit' :
    new_account = input('What is the name of this account? ')
    if new_account.lower() != 'quit' :
        balance = float(input('What is the balance? '))
        accounts.append(new_account)
        balances.append(balance)
        
print(' \
    \nAccount Information: ')

for i in range(len(accounts)) :
    print(f'{accounts[i]} - ${balances[i]:,.2f}')
    total += balances[i]

# MATH PART
total = total
average = total / len(accounts)
print(f'\
    \nTotal: ${total:,.2f} \
    \nAverage: ${average:,.2f} \
    \n')

