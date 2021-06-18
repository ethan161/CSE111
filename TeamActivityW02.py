from datetime import datetime
current = datetime.now()
weekday = current.isoweekday()

loop = True
discount = 0

while loop:
    print("Please enter the subtotal:")
    subtotal = (input(">> "))
    if subtotal == "done":
        loop = False
    else:
        subtotal = float(subtotal)
        if weekday == 2 or weekday == 3 and subtotal >= 50:
            discount = (subtotal * .10)
            subtotal = subtotal - discount
            print(f"Your discount was ${round(discount, 2)}")
        elif weekday == 2 or weekday == 3 and subtotal < 50:
            remainder = 50 - subtotal
            print(f"In order to receive the discount, you need to purchase ${remainder:.2f} more.")

        sales_tax = (subtotal * .06)
        total = subtotal + sales_tax

        print(f"Sales tax: {round(sales_tax, 2)}")
        print(f"Your total is {round(total, 2)}\n")
