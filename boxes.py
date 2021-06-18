import math

print("Enter the number of items: ")
box_quantity = int(input(">> "))
print("Enter the number of items per box: ")
box_item_ratio = int(input(">> "))

items_per_box = math.ceil(box_quantity / box_item_ratio)
print(f"For {box_quantity} items, packing {box_item_ratio} items in each box, you will need {items_per_box} boxes.")