import csv

def main():
    INUMBER_INDEX = 0
    NAME_INDEX = 1
    dictionary = read_dict("students.csv", INUMBER_INDEX)
    print(dictionary)
    #name = find_name(dictionary, NAME_INDEX)



def read_dict(students_csv, INUMBER_INDEX):
    dictionary = {}
    with open(students_csv, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            inumber = int(row[INUMBER_INDEX])
            dictionary[inumber] = row
    return dictionary

def find_name(dictionary, NAME_INDEX):
    inumber = input("What is the I-Number you want to search (xx-xxx-xxxx)? ")
    inumber = int(inumber.replace("-", ""))
    if inumber in dictionary:
        student = dictionary[inumber]
        name = student[NAME_INDEX]
        print(name)
    else:
        print("I-number does not exist in our system.")

if __name__ == "__main__":
    main()

