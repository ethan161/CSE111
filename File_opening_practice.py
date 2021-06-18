with open("books.txt") as books_file:
    for line in books_file:
        clean_line = line.strip()
        print(clean_line)
