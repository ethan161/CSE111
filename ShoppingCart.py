program_active = True
cart_items = []
cart_items_price = []
cart_total = 0

print("Welcome to the Shopping Cart Program!\n\n")
while program_active:
    menu_selection = input("Please select one of the following: \n1. Add item\n2. View cart\n3. Remove item\n4. Compute total\n5. Quit\nPlease enter an action: ")
    
    #Add a new item, and price:
    if menu_selection == "1":
        new_item = input("What item would you like to add? ")
        cart_items.append(new_item)
        new_item_price = float(input(f"What is the price of {new_item}? "))
        cart_items_price.append(new_item_price)
        print(f'"{new_item}" has been added to your shopping cart.\n')

    #Print the shopping cart contents:
    elif menu_selection == "2":
        number = 1
        if not cart_items:
            print("The cart is empty.")
        else:
            print("\nThe contents of the shopping cart are:")
            for i in range(len(cart_items)):
                cart_item = cart_items[i]
                cart_item_price = cart_items_price[i]
                print(f"{number}. {cart_item} - ${cart_item_price:.2f}")
                number += 1
        print("\n")

    #Remove an item from the place:
    elif menu_selection == "3":
        removal_number = -1
        removal_number = int(input("What item would you like to remove? (Enter the number): "))
        removal_number = removal_number - 1
        if removal_number > len(cart_items) or removal_number < 0:
            print("That is not a valid action. \n")
        else:
            cart_items.pop(removal_number)
            cart_items_price.pop(removal_number)
            print("Removal successful.")

    #Print the total of the items:
    elif menu_selection == "4":
        print("The current total of the shopping cart is: ")
        cart_total = sum(cart_items_price)
        print(f"${cart_total:.2f}\n")

    #Quit the program    
    elif menu_selection == "5":
        print("Thank you for shopping!")
        program_active = False
    else:
        print("\nPlease enter a number 1-5.\n")