from datetime import datetime
import csv

def retrieve_datetime():
    current_date_and_time = datetime.now()
    #current_date_and_time:%A %I:%M %p
    return current_date_and_time
    
def calculate_shooting_percentage(shots_made, shots_taken):
    shooting_percentage = round(((shots_made/shots_taken) * 100), 2)
    return shooting_percentage

def calculate_season_predictions():
    games_played = int(input("How many games have been played this season? "))
    games_left = int(input("How many games are left in the season? "))
    desired_stat = (input("What stat are you tracking? (points, rebounds, assists, or steals): "))
    stat_so_far = int(input(f"How many total {desired_stat} do you have so far this season? "))
    desired_statline = int(input("What is the desired statline? (i.e. 32 points per game, or 2 steals per game. Only input the number) "))
    averages_so_far = stat_so_far / games_played
    games_total = games_played + games_left
    total_stats_wanted = (desired_statline * games_total)
    required_stats_per_game = (total_stats_wanted - stat_so_far) / games_left
    print(f"\nSo far, you are averaging {averages_so_far:.2f} {desired_stat} per game. In order to average {desired_statline} {desired_stat} per game, you need to average {required_stats_per_game:.2f} {desired_stat} per game for the rest of the season.\n")

def read_csv_file(file_name):
    stats = {}
    try:
        with open (f"{file_name}.csv", "rt") as stats_file:
            reader = csv.reader(stats_file)
            next(reader)
            for row in reader:
                key = row[0]
                del row[0]
                stats[key] = row
        return stats
    except KeyError as key_err:
        print(type(key_err).__name__, key_err)

def calculate_global_practice_shooting_percentage(): 
    total_shots_made = 0
    total_shots_taken = 0   
    file_name = "shooting_stats"  
    stats = read_csv_file(file_name)
    for key in stats:
        row = stats[key]
        total_shots_made += float(row[0])
        total_shots_taken += float(row[1])
    global_shooting_percentage = round(total_shots_made / total_shots_taken, 2)
    return global_shooting_percentage

def calculate_game_averages(stats):
    total_minutes = 0
    total_points = 0
    total_assists = 0
    total_rebounds = 0
    total_steals = 0
    total_blocks = 0
    total_shots_made = 0
    total_shots_taken = 0
    averages_list = []
    for key in stats:
        row = stats[key]
        total_minutes += float(row[0])
        total_shots_made += float(row[1])
        total_shots_taken += float(row[2])
        print(total_shots_taken)
        total_points += float(row[4])
        total_assists += float(row[5])
        total_rebounds += float(row[6])
        total_steals += float(row[7])
        total_blocks += float(row[8])
    shooting_percentage = calculate_shooting_percentage(total_shots_made, total_shots_taken)
    #minutes(0)
    averages_list.append(int(round((total_minutes / len(stats)), 0)))
    #shots_made(1)
    averages_list.append(round((total_shots_made / len(stats)), 1))
    #shots_taken(2)
    averages_list.append(round((total_shots_taken / len(stats)), 1))
    #shooting_percentage(3)
    averages_list.append(shooting_percentage)
    #points(4)
    averages_list.append(round((total_points / len(stats)), 1))
    #assists(5)
    averages_list.append(round((total_assists / len(stats)), 1))
    #rebounds(6)
    averages_list.append(round((total_rebounds / len(stats)), 1))
    #steals(7)
    averages_list.append(round((total_steals / len(stats)), 1))
    #blocks(8)
    averages_list.append(round((total_blocks / len(stats)), 1))
    return averages_list

def main():
    program_running = True
    input_loop = True
    while program_running:
        input_loop = True
        print("\n---\n\nWelcome to your Personal Basketball Stats Assistant! (PBSA)")
        print("\nI can do a couple things. What are you looking help with today?")
        print(" 1. I would like to do math on a few statistics, but not save them to any database.")
        print(" 2. I shot a few times in practice and want to save my percentages to my global shooting percentage.")
        print(" 3. I just played a full-length game and would like to save my stats to my global file.")
        print(" 4. I would like to view my global shooting percentage in practice.")
        print(" 5. I would like to view my global game stats.")
        print(" 6. I would like to close the program.")
        while input_loop:
            print("\nPlease enter a number.")
            intro_input = int(input(">> "))
            print("")
            if intro_input == 1:
                loop_1A = True
                while loop_1A:
                    print("What stat are you hoping to compute?")
                    print(" A. Basic shooting percentages")
                    print(" B. How many of a certain stat (points, rebounds, assists) will I need to have a higher average?")
                    print(" C. I would like to exit this module.")
                    input_1A = input(">> ")
                    print("")
                    if input_1A.lower() == "a":
                        shots_made = int(input("How many shots were made? "))
                        shots_taken = int(input("How many shots were taken? "))
                        shooting_percentage = calculate_shooting_percentage(shots_made, shots_taken)
                        print(f"You made {shots_made}/{shots_taken}, which is a shooting percentage of {shooting_percentage}%.\n")
                    elif input_1A.lower() == "b":
                        loop_1B = True
                        while loop_1B:
                            calculate_season_predictions()
                            input_1B = input("Hit enter to return to the statisics module. ")
                            if input_1B == "":
                                loop_1B = False
                            else:
                                loop_1B = False
                    elif input_1A.lower() == "c":
                        loop_1A = False
                        input_loop = False
                    else:
                        print("That is not a valid input.")
            elif intro_input == 2:
                loop_2A = True
                while loop_2A:
                    print("Please input the following numbers.")
                    shots_made = int(input("How many shots did you make? "))
                    shots_taken = int(input("How many shots did you take? "))
                    shooting_percentage = calculate_shooting_percentage(shots_made, shots_taken)
                    current_date_and_time = retrieve_datetime()
                    with open("shooting_stats.csv", "at") as dimens_file:
                        print(f"{current_date_and_time:%A %I:%M %p},{shots_made},{shots_taken},{shooting_percentage}", file=dimens_file)
                    print(f"Overall, you shot {shooting_percentage}% from the field. This data has been saved to your global file.")
                    loop_2B = True
                    while loop_2B:
                        input_2B = input("Hit enter to return to the home screen. ")
                        if input_2B == "":
                            loop_2B = False
                            loop_2A = False
                        else:
                            loop_2B = False
                            loop_2A = False

                input_loop = False
            elif intro_input == 3:
                game_dict = {}
                day = input("When was the game? (mm/dd/yyyy) ")
                location = input("Where was your game played? ")
                minutes = int(input("How many minutes did you play? "))
                shots_made = int(input("How many shots did you make? "))
                shots_taken = int(input("How many shots did you take? "))
                points = int(input("How many points did you have? "))
                assists = int(input("How many assists did you have? "))
                rebounds = int(input("How many rebounds did you have? "))
                steals = int(input("How many steals did you have? "))
                blocks = int(input("How many blocks did you have? "))
                shooting_percentage = calculate_shooting_percentage(shots_made, shots_taken)
                filler_variable = ""
                game_dict[day] = (location, minutes, shots_made, shots_taken, shooting_percentage, points, assists, rebounds, steals, blocks, filler_variable)
                with open("gameplay_stats.csv", "at") as dimens_file:
                    print(f"{game_dict}", file=dimens_file)
                print("\nYour game has been saved to your global data.")
                loop_3A = True
                while loop_3A:
                    input_3A = input("Hit enter to return to the home screen. ")
                    if input_3A == "":
                        loop_3A = False
                    else:
                        loop_3A = False
                input_loop = False
            elif intro_input == 4:
                global_shooting_percentage = calculate_global_practice_shooting_percentage()
                print(f"In practice, you are averaging {global_shooting_percentage}%.")
                loop_4A = True
                while loop_4A:
                    input_4A = input("Hit enter to return to the home screen. ")
                    if input_4A == "":
                        loop_4A = False
                    else:
                        loop_4A = False
                input_loop = False
            elif intro_input == 5:
                loop_5A = True
                print("\nWhat gameplay statistic would you like reviewed?")
                print(" A. All")
                print(" B. Minutes played")
                print(" C. Shots made")
                print(" D. Shots taken")
                print(" E. Shooting percentage")
                print(" F. Points")
                print(" G. Assists")
                print(" H. Rebounds")
                print(" I. Steals")
                print(" J. Blocks")
                print(" K. Exit this module")
                while loop_5A:
                    gameplay_input = input(">> ")
                    if gameplay_input.lower() in "abcdefghij":
                        stats = read_csv_file("gameplay_stats")
                        averages_list = calculate_game_averages(stats)
                        if gameplay_input.lower() == "a":
                            print("Here are your global averages in gameplay:")
                            print(f"Minutes played: {averages_list[0]}")
                            print(f"Shots made: {averages_list[1]}")
                            print(f"Shots taken: {averages_list[2]}")
                            print(f"Shooting percentage: {averages_list[3]}")
                            print(f"Points: {averages_list[4]}")
                            print(f"Assists: {averages_list[5]}")
                            print(f"Rebounds: {averages_list[6]}")
                            print(f"Steals: {averages_list[7]}")
                            print(f"Blocks: {averages_list[8]}")
                            loop_5B = True
                            while loop_5B:
                                input_5B = input("Hit enter to return to the home screen. ")
                                if input_5B == "":
                                    loop_5A = False
                                    loop_5B = False
                                else:
                                    loop_5A = False
                                    loop_5B = False
                        elif gameplay_input.lower() == "b":
                            print(f"You average {averages_list[0]} minutes per game.")
                        elif gameplay_input.lower() == "c":
                            print(f"You average {averages_list[1]} shots made per game.")
                        elif gameplay_input.lower() == "d":
                            print(f"You average {averages_list[2]} shots taken per game.")
                        elif gameplay_input.lower() == "e":
                            print(f"You average a shooting percentage of {averages_list[3]}%.")
                        elif gameplay_input.lower() == "f":
                            print(f"You average {averages_list[4]} points per game.")
                        elif gameplay_input.lower() == "g":
                            print(f"You average {averages_list[5]} assists per game.")
                        elif gameplay_input.lower() == "h":
                            print(f"You average {averages_list[6]} rebounds per game.")
                        elif gameplay_input.lower() == "i":
                            print(f"You average {averages_list[7]} steals per game.")
                        elif gameplay_input.lower() == "j":
                            print(f"You average {averages_list[8]} blocks per game.")
                    elif gameplay_input.lower() == "k":
                        loop_5A = False
                    else:
                        print("That is not a valid input.")
                input_loop = False
            elif intro_input == 6:
                input_loop = False
                program_running = False

            else:
                print("That is not a valid number.")

    print("Have a great day!")    

if __name__ == "__main__":
    main()