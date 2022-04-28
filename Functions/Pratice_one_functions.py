def display_regular (str):
    print(str)

def display_uppercase (str):
    name = str.upper()
    print(name)

def display_lowercase (str):
    name = str.lower()
    print(name)

msg = input(" What is your message:")

display_regular(msg)
display_uppercase(msg)
display_lowercase(msg)
