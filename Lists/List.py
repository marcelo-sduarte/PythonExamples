'''
#1. starting variable list and new_client
clients = [] 
new_client = ""

#2. Loop until variable equals quit
while new_client != "quit":
    new_client = input ("What is the name of a Client? For exit digit (quit)qyur") 
#3. adicionando variable new_client in list clients
    clients.append(new_client) 

#4. loop to show
for client in clients:
    print(client)
'''
friends = ["Luc", "Kristi", "Rex"]
tips = [12.25, 13.95, 8.80]

running_total = 0

for tip_amount in tips:
    #running_total = running_total + tip_amount
    running_total += tip_amount
print(f"The total is: {running_total:.2f}")
