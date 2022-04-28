
people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

min_age = 99
min_name = "" # It doesn't matter what you set this to, it just needs to be declared

for item in people:
    parts = item.split(" ")
    name = parts[0] 
    age = int(parts[1]) 

    if age < min_age:
        min_age = age
        min_name = name

print(f"The yougest person is: {min_name} with an age of {min_age}")
