item_list = []
check1 = True

print("Please enter the items on your shopping list (Type 'quit' to exit).")
while check1:
    item = input("Item: ")
    if item == "quit":
        check1 = False
    else:
        item_list.append(item)

print("\nYour shopping list is: ")
for i in range(len(item_list)):
    item = item_list[i]
    print(f"{i}. {item.capitalize()}")

index = int(input("Which item would you like to change? "))
item_replacement = input("What is the new item? ")

item_list[index] = item_replacement

for i in range(len(item_list)):
    item = item_list[i]
    print(f"{i}. {item.capitalize()}")