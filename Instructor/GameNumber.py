import random
magic_number = random.randint(1,100)
guess_number = -1
count = 1
answer = True
#magic_number = float(input("What is the magic number?"))
while answer == True:
    while guess_number != magic_number:    
        guess_number = float(input("What is your guess?"))
        if guess_number < magic_number:
            print(" Higher")
            count = count + 1
        elif guess_number > magic_number:
            print("Lower")
            count = count + 1
    print(f"You guessed it! You try {count}x")
    answer = input( "Are you contine? (yes or not)")
    if answer == "yes":
        answer = True
        magic_number = random.randint(1,100)
        guess_number = -1
    else:
        answer = False
print("Bye")