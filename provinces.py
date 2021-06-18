province_list = []
alberta_counter = 0
counter = 0

with open("provinces.txt", "rt") as province_file:
    for line in province_file:
        line = line.strip()
        province_list.append(line)
    print(province_list)
    province_list.pop(0)
    province_list.pop()
    for item in province_list:
        if item == "AB":
            province_list.pop(counter)
            province_list.append("Alberta")
            alberta_counter += 0
        elif item == "Alberta":
            alberta_counter += 1
        counter += 1

    print(f"Alberta occurs {alberta_counter} times in the modified list.")
    
