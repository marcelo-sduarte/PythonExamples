# Program by Marcelo Duarte
print("--------------------------------------")
print("Welcome to the Shopping Cart Program!")
print("--------------------------------------")
print()
menu = ["1. Add item","2. View cart", "3. Remove item", "4. Compute total", "5. Quit"]
item_add = []
itens_price = []
item_menu = ""
count = 0

while item_menu != "5. Quit":
    print("-------------------------------------------------------")
    print("Please select one the following:")    
    for index in menu:
        print(index)
    item_menu = input("Please enter the action: ")
    if item_menu == "5":
        item_menu = "5. Quit"
    elif item_menu == "1":
        answer_item = input("What item would you like to add? ")
        answer_price = float(input("What price of item? "))
        count = count + 1
        answer_item = str(count) +". " + answer_item + " - $ "+str(answer_price)
        item_add.append(answer_item)
        itens_price.append(answer_price)

        print(f"{answer_item}, has been added to the cart")
    elif item_menu == "2":
        print("The contents of the shopping cart are:")
        for i in item_add:
            print(i)
    elif item_menu == "3":
        item_remove = int(input("What item would you like to remove? "))
        #LOOP TO LIST ITEM_ADD  
        for i in range(len(item_add)):
            if item_remove == i:
                i_remove = item_add[i]
                item_add.remove(i_remove)
                print(f"{i}, item removido")
            elif i == 0:
                i_remove = item_add[i]
                item_add.remove(i_remove)

        #LOOP TO LIST ITENS_PRICE
        for j in range(len(itens_price)):
            if item_remove == j:                
                price = itens_price[j]
                itens_price.remove(price)
            elif j == 0:
                price = itens_price[j]
                itens_price.remove(price)
  
        print(f"{j}, has been removed to the cart")             
                
            
    elif item_menu == "4":
        sum= 0
        for index in itens_price:
            sum += index
        print(f"The total price of the items in the shopping cart is $ {sum:.2f} ")

    print()
print("Thank you! Goodbye.")
