people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
minimum_age = 150
minimum_name = "fail"
for item in people:
    clean_line = item.strip()
    parts = clean_line.split(" ")
    name = parts[0]
    age = int(parts[1])
    if age < minimum_age:
        minimum_age = age
        minimum_name = name
print(minimum_age)
print(minimum_name)