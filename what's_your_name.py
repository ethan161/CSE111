#project requirements:
first_name=input("What's your first name? ")
last_name=input("What's your last name? ")

print("Your name is " + last_name.capitalize() + ", " + first_name.capitalize() + " " + last_name.capitalize() + ".")

#if your first name is james, the system will give you a special introduction
test=first_name.lower().count("james")
if test == 1:
    print("Welcome, 007.")