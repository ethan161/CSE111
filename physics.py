import math
print("\nWelcome to the velocity calculator. Please enter the following: \n")
mass = float(input("Mass (in kg): "))
gravity = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
time = float(input("Time (in seconds): "))
density = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
area = float (input("Cross sectional area (in m^2): "))
constant = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

c_variable = float(0.5 * density * area * constant)
velocity_at_t = math.sqrt((mass*gravity)/c_variable)*(1 - math.exp((-math.sqrt(mass*gravity*c_variable)/mass) * time))
print(f"\nThe inner value of c is: {c_variable:.3f}.")
print(f"The velocity after {time:.1f} seconds is: {velocity_at_t:.3f} m/s")