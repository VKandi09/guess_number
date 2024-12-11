import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Enter a valid number")
        quit()
else:
    print("Enter only numbers")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make your guess: ")
    
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Enter only numbers")
    
    if user_guess == random_number:
        print("You got it right!")
        break
    else:
        print("You got it wrong!")
