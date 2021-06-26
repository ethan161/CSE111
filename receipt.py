import csv
from datetime import datetime
current_date_and_time = datetime.now()

def read_products():
    products = {}
    try:
        with open ("products.csv", "rt") as product_file:
            reader = csv.reader(product_file)
            next(reader)
            for row in reader:
                key = row[0]
                del row[0]
                products[key] = row
        return products
    except KeyError as key_err:
        print(type(key_err).__name__, key_err)

def process_request(products):
    this_count = 0
    item_count = 0
    subtotal = 0
    number_of_requests = 0
    item_price = []
    requested_item_name = []
    quantity_list = []
    try:
        with open ("request.csv", "rt") as request_file:
            reader = csv.reader(request_file)
            next(reader)
            for line in reader:
                product_number = line[0]
                quantity = float(line[1])
                number_of_requests +=1
                if product_number in products:
                    product_info = products[product_number]
                    requested_item_name.append(product_info[0])
                    quantity_list.append(quantity)
                    item_price.append(float(product_info[1]))
                    item_count += quantity
        for k in range(0, len(quantity_list)):
            item_count = item_count + quantity_list[k]

        print(f"Inkom Emporium\n")
    
        for i in range(number_of_requests):
            print(f"{requested_item_name[this_count]}: {quantity_list[this_count]:.2f} @ {item_price[this_count]}")
            subtotal += quantity_list[this_count] * item_price[this_count]
            this_count += 1
        sales_tax = (subtotal * .06)

        print(f"Number of items: {item_count:.0f}")
        print(f"Subtotal: {subtotal}")
    
        print(f"Sales tax: {sales_tax:.2f}")
        print(f"Total: {subtotal + sales_tax:.2f}")

        print("\nThank you for shopping at Inkom Emporium.")
        print(f"{current_date_and_time:%A %I:%M %p}")


    except FileNotFoundError as file_not_found_err:
        print(f"Error: cannot open {request_file}"
                " because it doesn't exist.")

    except PermissionError as perm_err:
        print(f"Error: cannot read from {request_file}"
                "because you don't have permission.")
                
    except KeyError as key_err:
        print(type(key_err).__name__, key_err)

def main():
    products = read_products()
    process_request(products)

if __name__ == "__main__":
    main()