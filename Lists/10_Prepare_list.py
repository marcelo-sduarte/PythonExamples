print("Welcome to the shopping Cart Program!")
materials = []
answer = ""
while answer != "quit":
    print("Please enter the items of the shopping list (type: quit to finish):")
    answer = input ("Item:" )
    
    if answer == "quit":
        print("The shopping list is: ")
        for i in materials:
            print(i)
        
        print("The shopping list with index is: ")
        for i in range(len(materials)):
            material = materials[i]
            print(f"{i}. {material}")
        
        item_chance = int(input("Which item would you like to change: "))
        new_item = input("What is the new item? ")
        materials[item_chance] = new_item
        for i in range(len(materials)):
            material = materials[i]
            print(f"{i}. {material}")
            

            
    else:
        materials.append(answer)


    