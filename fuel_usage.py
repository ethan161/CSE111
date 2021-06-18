def main():
    start_miles = float(input("What is your starting odometer value (in miles)? "))
    end_miles = float(input("What is your finishing odometer value (in miles)? "))
    amount_gallons = float(input("What is the fuel amount (in gallons)? "))

    mpg = miles_per_gallon(start_miles, end_miles, amount_gallons)
    lp100k = lp100k_from_mpg(mpg)

    mpg = round(mpg, 1)
    lp100k = round(lp100k, 2)

    print(f"{mpg} miles per gallon")
    print(f"{lp100k} liters per 100 kilometers")

def miles_per_gallon(start_miles, end_miles, amount_gallons):
    return (end_miles - start_miles) / amount_gallons

def lp100k_from_mpg(mpg):
    return 235.215 / mpg

main()