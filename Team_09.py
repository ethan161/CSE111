print("Enter a list of numbers, type 0 when finished.")
number_list = []
positive_list= []
user_number = ""
counter = 0
while user_number != 0:
    user_number = float(input("Enter number: "))
    if user_number != 0:
        number_list.append(user_number)
    if user_number > 0:
        positive_list.append(user_number)


print(f"The sum is: {sum(number_list)}")
print(f"The average is: {(sum(number_list))/(len(number_list))}")
print(f"The largest number is: {max(number_list)}")
print(f"The smallest positive number is: {min(positive_list)}")
print("The sorted list is:")
number_list.sort()
for number in number_list:
    print(f"{number}")