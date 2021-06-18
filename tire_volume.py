import math
from datetime import datetime
loop = True

def tire_volume_function(width_tire, aspect_tire, diameter_tire):
    return (math.pi * width_tire * width_tire * aspect_tire * (width_tire * aspect_tire + 2540 * diameter_tire)) / 10000000

print("Enter the width of the tire in mm (ex 205):")
width_tire = int(input(">> "))
print("Enter the aspect ratio of the tire (ex 60):")
aspect_tire = int(input(">> "))
print("Enter the diameter of the wheel in inches (ex 15):")
diameter_tire = int(input(">> "))

volume = tire_volume_function(width_tire, aspect_tire, diameter_tire)
volume = round(volume, 1)
print(f"The approximate volume is {volume} milliliters.")

while loop:
    buy = input("Would you like to buy tires with these dimensions? (yes/no) ")
    if buy.lower() == "yes":
        print("Please enter a phone number, and we will contact you at a later time:")
        phone_number = input(">> ")
        print("Have a great day!")
        loop = False
    elif buy.lower() == "no":
        print("Have a great day!")
        phone_number = ("")
        loop = False
    else:
        print("Please enter yes or no.")

current_date_and_time = datetime.now()

with open("tire_volume.txt", "at") as dimens_file:
    print(f"\n{current_date_and_time}\n{width_tire}, {aspect_tire}, {diameter_tire}, {volume}\n{phone_number}", file=dimens_file)