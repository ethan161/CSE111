import math

squarelength=input("What is the length of the square in centimeters? ")
print(f"The area of the square is {int(squarelength)*int(squarelength)} centimeters squared, and {(int(squarelength)*int(squarelength))/10000} meters squared.\n")

circlelength=input("What is the radius of the circle in centimeters? ")
print(f"The area of the circle is {(int(circlelength)*int(circlelength))*math.pi} centimeters squared, and {((int(circlelength)*int(circlelength))*math.pi)/10000} meters squared.\n")

rectanglelength=input("What is the length of the rectangle in centimeters? ")
rectanglewidth=input("What is the width of the rectangle in centimeters? ")
print(f"The area of the rectangle is {int(rectanglelength)*int(rectanglewidth)} centimeters squared, and {(int(rectanglelength)*int(rectanglewidth))/10000} meters squared.\n")

biginput=input("What is your favorite number? ")
print(f"\nA square with the side length {biginput} has the area {int(biginput)**2}.")
print(f"A cube with the side length {biginput} has the volume {int(biginput)**3}.\n")

print(f"A circle with the radius {biginput} has the area {(int(circlelength)*int(circlelength))*math.pi}")
print(f"A sphere with the radius {biginput} has the volume {(4/3)*(int(biginput)**3)*(math.pi)}")


#stretch challenges include:
#Using the actual number for pi instead of 3.14;
#Calculating different shapes using a single input. Square, circle (input is the radius), cube, and sphere
#Calculate the original program to give the answer in centimeters and meters