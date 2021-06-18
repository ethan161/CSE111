positive_number = -1
repeat_thing = True
while repeat_thing:
    positive_number = float(input("\nPlease input a positive number. "))
    if positive_number >= 0:
        print(f"The number is {positive_number}")
        repeat_thing = False
    else:
        print("That is not a negative number, try again.")

answer = True
while answer:
    response = input("May I have a piece of candy? ").lower()
    if response == "yes":
        answer = False
    else:
        answer = True
print("Thank you")