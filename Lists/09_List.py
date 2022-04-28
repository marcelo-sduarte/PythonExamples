friends = []
name_friend= ""
while name_friend != "end":
    name_friend = input("Type the name of a friend: [end to exit] ")
    friends.append(name_friend) 
print()
print(" Your friends are:")
for friend in friends:   
    if friend != "end":
        print(friend)