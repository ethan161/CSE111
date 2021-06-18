#inputs of meals, people, and sales tax
child_price = float(input("What is the price of a child meal? "))
adult_price = float(input("What is the price of an adult meal? "))
child_number = int(input("How many children are there? "))
adult_number = int(input("How many adults are there? "))
sales_tax = float(input("What is the sales tax rate? "))

#the dirty work; doing the math for the outputs
subtotal = float((child_price * child_number) + (adult_price * adult_number))
computed_sales_tax = (subtotal * sales_tax) / 100
total = computed_sales_tax + subtotal

#displaying the math
print("\n" + f"Subtotal: ${subtotal:.2f}")
print(f"Sales Tax: ${computed_sales_tax:.2f}")
print(f"Total: ${total:.2f}")

#inputs and computations for a tip
tip_10 = total * 0.1
tip_15 = total * 0.15
tip_20 = total * 0.2
tip_selection = input("Would you like to leave a tip? yes/no ")
if tip_selection.lower() == "yes":
    print("\n" + "Type the tip percentage you would like to leave: (i.e. '10,' leave out the percentage sign)")
    print(f"10% tip is: ${tip_10:.2f}")
    print(f"15% tip is: ${tip_15:.2f}")
    print(f"20% tip is: ${tip_20:.2f}")
    custom_tip = float(input("Tip: "))
    tip_percentage = (custom_tip / 100) + 1
    total_and_tip = total * tip_percentage
    print(f"Your new total is: ${total_and_tip:.2f}.")

#computing payment and change
payment = float(input("\n" + "What is the payment amount? "))
if tip_selection.lower() == "yes":
    change = payment - total_and_tip
else:
    change = payment - total
print(f"Your change is ${change:.2f}.")