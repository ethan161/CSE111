import random
guess = 1.0000293858

magic_number = float(input("What is the magic number? "))

while guess > magic_number or guess < magic_number:
    guess = float(input("What is your guess? "))
    if guess > magic_number:
        print("Lower")
    else:
        print("Higher")
print("Congrats, you guessed the number!")