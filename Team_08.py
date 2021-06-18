user_number = int(input("How many columns and rows do you want in your multiplication table? "))
counter = 2
largest = user_number * user_number
while (largest) > 10:
    largest = largest / 10
    counter += 1
'''if counter == 1:
    counter = 2'''
for x in range (1, user_number + 1):
    for y in range (1, user_number + 1):
        if y == user_number:
            print(f"{x * y:{counter}}")
        else:
            print(f"{x * y:{counter}}", end = " ")

#12 * 12= 144

#14    counter 3
#1.4   counter 4
