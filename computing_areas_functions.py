import math
loop = True
loop2 = True

def square_function(user_value1):
    user_value2 = user_value1
    area_square = rectangle_function(user_value1, user_value2)
    return area_square

def rectangle_function(user_value1, user_value2):
    area_rectangle = user_value1 * user_value2
    return area_rectangle

def circle_function(user_value1):
    area_circle = (user_value1 * user_value1) * math.pi
    return area_circle

def compute_area(shapeshifter, user_value1):
    if shapeshifter == "square":
        area_square = square_function(user_value1)
        return area_square
    elif shapeshifter == "circle":
        area_circle = (user_value1 * user_value1) * math.pi
        return area_circle
    
while loop:
    loop2 = True
    print("What shape would you like to compute? Type 'end' to quit")
    shape = input(">> ")
    shape = shape.lower()
    if shape == "square":
        print("What is the length of the sides?")
        user_value1 = float(input(">> "))
        computed_area = square_function(user_value1)
        print(f"The area is: {computed_area}\n")
    elif shape == "rectangle":
        print("What is the length of the first side?")
        user_value1 = float(input(">> "))
        print("What is the length of the second side?")
        user_value2 = float(input(">> "))
        computed_area = rectangle_function(user_value1, user_value2)
        print(f"The area is: {computed_area}\n")
    elif shape == "circle":
        print("What is the length of the radius? ")
        user_value1 = float(input(">> "))
        computed_area = circle_function(user_value1)
        print(f"The area is: {computed_area}\n")
    elif shape == "secret function":
        print("What is the shape? ")
        shapeshifter = input(">> ")
        shapeshifter = shapeshifter.lower()
        while loop2:
            if shapeshifter == "circle":
                print("What is the radius of the circle? ")
                user_value1 = float(input(">> "))
                computed_area = compute_area(shapeshifter, user_value1)
                print(f"The area is: {computed_area}")
                loop2 = False
            elif shapeshifter == "square":
                print("What is the length of the sides?")
                user_value1 = float(input(">> "))
                computed_area = compute_area(shapeshifter, user_value1)
                print(f"The area is: {computed_area}")
                loop2 = False
            else:
                print("That is not a valid shape. This only accepts squares and rectangles.")
    elif shape == "end":
        print("Have a great day.\n")
        loop = False
    else:
        print("That is not a valid shape. This program computes squares, rectangles, and circles.")


