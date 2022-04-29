

with open ("hr_system.txt") as newfile:
    for line in newfile:
        lines = line.strip()
        lines = line.split(" ")
        name = lines[0]
        id = lines[1]
        job = lines[2]
        salary = float(lines[3])
        

        print(f"Name: {name} (ID: {id}), Title: {job} - ${salary:.2f}")
