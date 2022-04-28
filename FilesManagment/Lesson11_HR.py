with open ("hr_system.txt") as newfile:
    for file in newfile:
        file = file.strip()
        file = file.split(" ")
        name = file[0]
        title = file[2]
        print(f"Name: {name}, Title: {title}")