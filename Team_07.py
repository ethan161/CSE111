import random

repeat_game = True
while repeat_game:
    the_number = random.randint(1, 100)
    guess_number = ""
    number_of_guesses = 0
    while guess_number != the_number:
        guess_number = int(input("\nWhat is your guess? "))
        number_of_guesses += 1
        if guess_number > the_number:
            print("Lower")
        elif guess_number < the_number:
            print("Higher")
        else:
            print("You've guessed it!")
    print(f"\n\nIt took you {number_of_guesses} tries to figure out the number.")
    repeat_answer = input("Would you like to try again? Y/N: ").upper()
    if repeat_answer == "Y":
        repeat_game = True
    elif repeat_answer == "N":
        repeat_game = False
    else:
        print("I will take that as a no.")
        repeat_game = False
print("Have a great day.")
