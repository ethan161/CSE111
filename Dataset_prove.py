lowest_life = 200
highest_life = 1
#In this program, I found myself typing "year of interest" and "country of interest" a lot, so from this point on, "yof" and "cof" are my abbreviations of choice.
yof_life_expectancies = []
yof_lowest_life = 200
yof_highest_life = 1

country_check = False
year_check = False

cof_life_expectancies = []
cof_lowest_life = 200
cof_highest_life = 1

print("\nEnter the year of interest:")
yof = input(">>")
print("\nEnter the country of interest:")
cof = input(">>")
cof = cof.lower()
cof = cof.capitalize()

with open("life-expectancy.csv") as data_file:
    next(data_file)
    for line in data_file:
        #This goes through all the data and assigns them all to different lists.
        clean_line = line.strip()
        parts = clean_line.split(",")
        country = parts[0]
        country_abbreviation = parts[1]
        year = parts[2]
        life_expectancy = float(parts[3])
        #This chunk of code is what determines the general highs and lows.
        if life_expectancy > highest_life:
            highest_life = life_expectancy
            highest_life_country = country
            highest_life_year = year
        if life_expectancy < lowest_life:
            lowest_life = life_expectancy
            lowest_life_country = country
            lowest_life_year = year
        #Here, the year of interest gathers all its data and assigns them to their different lists / maxes and mins.
        if year == yof:
            yof_life_expectancies.append(life_expectancy)
            year_check = True
            if life_expectancy > yof_highest_life:
                yof_highest_life = life_expectancy
                yof_highest_life_country = country
            elif life_expectancy < yof_lowest_life:
                yof_lowest_life = life_expectancy
                yof_lowest_life_country = country
        #Country of interest is processed here:         
        if country == cof:
            cof_life_expectancies.append(life_expectancy)
            country_check = True
            if life_expectancy > cof_highest_life:
                cof_highest_life = life_expectancy
                cof_highest_life_year = year
            elif life_expectancy < cof_lowest_life:
                cof_lowest_life = life_expectancy
                cof_lowest_life_year = year
        

#The final outputs
print(f"The highest life expectancy is: {highest_life:.3f} from {highest_life_country} in {highest_life_year}.")
print(f"The lowest life expectancy is: {lowest_life:.3f} from {lowest_life_country} in {lowest_life_year}.")

#If the year provided was in the data, then this will run all the required math and print statements.
if year_check:
    yof_total_average = sum(yof_life_expectancies) / len(yof_life_expectancies)
    print(f"\nFor the year {yof}:")
    print(f"The average life expectancies across all countries was {yof_total_average:.2f}")
    print(f"The highest life expectancy was in {yof_highest_life_country} with {yof_highest_life}")
    print(f"The lowest life expectancy was in {yof_lowest_life_country} with {yof_lowest_life}\n")
else:
    print("Your year did not provide any data.\n")
    
#This is all the data required for our "country of interest,".
if country_check:
    cof_total_average = sum(cof_life_expectancies) / len(cof_life_expectancies)
    print(f"For the country of {cof.capitalize()}:")
    print(f"The average life expectancy is: {cof_total_average:.2f}")
    print(f"The highest life expectancy was {cof_highest_life} in {cof_highest_life_year}.")
    print(f"The lowest life expectancy was {cof_lowest_life} in {cof_lowest_life_year}.")
else:
    print("Your country did not provide any data.\n")