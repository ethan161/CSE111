def display_regular(message):
    print(message)

def display_uppercase(message):
    print(message.upper())

def display_lowercase(message):
    print(message.lower())

print("What is your message?")
message = input(">>")

display_regular(message)
display_uppercase(message)
display_lowercase(message)
