initial_temp = int(input("What is the temperature? "))
degree_type = str(input("Is it in Fahrenheit or Celcius? "))
if degree_type.lower() == ("fahrenheit"):
    output_temp = (initial_temp - 32) * (5/9)
    output_degree_type = str("Celcius")
elif degree_type.lower() == ("celcius"):
    output_temp = (initial_temp * (9/5)) + 32
    output_degree_type = str("Fahrenheit")

print(f"The temperature in {output_degree_type} is {output_temp:.1f}.")

