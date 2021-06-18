#This function converts degrees from Celsius to Fahrenheit
def celsius_to_fahrenheit(temperature_input):
    return (temperature_input * (5/9)) + 32


#This function computes the windchill based on the degrees in Fahrenheit and the hypothetical wind speed
def compute_windchill(temperature_final, current_wind_speed):
    windchill = 35.74 + (0.6215 * (temperature_final)) - (35.75 * (current_wind_speed**0.16)) + (0.4275 * (temperature_final)) * (current_wind_speed**0.16)
    return windchill

loop2 = False
print("What is the temperature?")
temperature_input = float(input(">> "))
while not loop2:
    print("Fahrenheit or Celsius? (F/C)")
    degree_type = input(">> ")
    if degree_type.lower() == "c":
        temperature_final = celsius_to_fahrenheit(temperature_input)
        loop2 = True
    elif degree_type.lower() == "f":
        temperature_final = temperature_input
        loop2 = True
    else:
        print("That is an invalid unit, try again.\n")

current_wind_speed = 0
while current_wind_speed != 60:
    current_wind_speed += 5
    windchill = compute_windchill(temperature_final, current_wind_speed)
    print(f"At temperature {temperature_final:.1f}F, and wind speed at {current_wind_speed:.0f} mph, the windchill is: {windchill:.2f}F")

