denial = ("Sorry, you may not ride.")
approval = ("Enjoy the ride!")

age1 = float(input("What is the age of the first rider? "))
height1 = float(input("What is the height of the first rider? "))
if height1 < 36:
    print(f"{denial}")
else:
    second_check = input("Is there a second rider? (yes/no) ")
    if second_check.lower() == ("no"):
        if age1 < 18 or height1 < 62:
            print(f"{denial}")
        else:
            print(f"{approval}")
    elif second_check.lower() == ("yes"):
        age2 = float(input("What is the age of the second rider? "))
        if age1 < 18 and age2 < 18:
            print(f"{denial}")
        else:
            height2 = float(input("What is the height of the second rider? "))
            if height2 < 36:
                print(f"{denial}")
            else:
                print(f"{approval}")


