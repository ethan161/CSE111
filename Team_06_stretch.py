age1 = int(input("What is the age of the first rider? "))
height1 = int(input("What is the height of the first rider? "))
if age1 >= 12 and age1 <= 17:
    gold1 = input("Do you have a golden pass (yes/no)? ").lower()
    if gold1 == "yes":
        gold1 = True
    else:
        gold1 = False
    if gold1:
        age1 = 18

riders = input("Is there a second rider (yes/no)? ").lower()
if riders == "yes":
    age2 = int(input("What is the age of the second rider? "))
    height2 = int(input("What is the height of the second rider? "))
    if age2 >= 12 and age2 <= 17:
        gold2 = input("Do you have a golden pass (yes/no)? ").lower()
    # two riders code
        if gold2 == "yes":
            gold2 = True
        else:
            gold2 = False
        if gold2:
            age2 = 18
    # decisions
    if height1 < 36 or height2 < 36:
        can_ride = False
    else:
        if (age1 >= 18 or age2 >= 18) or ((age1 >= 16 and age2 >= 14) or (age1 >= 14 and age2 >= 16)):
            can_ride = True
        else:
            if (age1 >= 12 and age2 >= 12) and (height1 >= 52 and height2 >= 52):
                can_ride = True
            else:
                can_ride = False
# single rider
else:
    if height1 < 36:
        can_ride = False
    else:
        if age1 >= 18 and height1 >= 62:
            can_ride = True
        else:
            can_ride = False
# print
if can_ride:
    print("\n\nWelcome to the ride. Please be safe and have fun!")
else:
    print("Sorry, you may not ride.")
