print("\nWelcome to your adventure!\n-\n-\n-\n")

print("You find yourself in a strange field, armed with some matches and a water bottle. In the distance, you see a structure \npoking out of the landscape.")
print("\nDo you...")


choice1 = input("TRAVEl to the structure, or STAY and set up camp: ")
if choice1.lower() == "travel":
    print("\n" + "As you travel to the structure, you quickly realize you have run out of water. You see some rainclouds forming on the horizon.\n")
    print("Do you...")
    choice2 = input("Finish your journey to the TOWER, or search for a place to gather more WATER? ")
    if choice2.lower() == "tower":
        print(f"\nYou persist through your discomfort, and eventually reach the tower, exhausted and demoralized.\nHowever, you hurriedly approach to avoid the incoming storm. You notice that the building has signs of life, but as you look around\nthe first floor, you find nothing of interest. The storm starts.\n\n")
        choice3 = input("Do you continue to SEARCH the area, or settle down for the NIGHT? ")
        if choice3.lower() == "search":
            print("\nYou decide that looking around would be a better idea. As you are outside, a load groan is followed by a huge crash.\nThe ceiling collapses, leaving wood and brick. After the rain stops, you light the remaining structure on fire, creating a smoke beacon, and you are quickly found and rescued. \n\nTHE END")
        elif choice3.lower() == "night":
            print("As the rain continues, you decide it is better to get some rest. As you are drifting off, there is a huge crash, waking you up just\nin time to see a large beam fall from the ceiling right above you. About a week later, a crew comes to remove the tower,\nand as they later discover, your body. \n\nTHE END\n")
        else:
            print("-\n" + "You die a horrible and slow death for not conforming to the programmers wishes. Better luck next time.")
    elif choice2.lower() == "water":
        print("\nAlthough the tower piques your interest, you decide it is smarter to play it safe. It takes a few minutes, you locate a small pool that looks like will fill up with the coming rain. ")
        choice4 = input("\nDo you...\nDIG the pool larger to collect more water, or try and construct a makeshift SHELTER? ")
        if choice4.lower() == "dig":
            print("\nYou dig the pool larger just as the rain starts. The storm passes uneventfully, and you live off your water for another week before you are discovered by locals, and eventually find your way home.\n\nTHE END")
        elif choice4.lower() == "shelter":
            print("\nThe shelter takes longer than you anticipated, you finish it in time for the rainstorm. Throughout the coming days, you eventually run out of water, and dehydrate, and your remains are picked off by rodents.\n\nTHE END")
        else:
            print("-\n" + "You die a horrible and slow death for not conforming to the programmers wishes. Better luck next time.")
    else: 
        print("-\n" + "You die a horrible and slow death for not conforming to the programmers wishes. Better luck next time.")
elif choice1.lower() == "stay":
    print("-\n" + "While setting up camp, you quickly realize that your water is not going to last very long. You rush through the rest of your \npreparations, start a fire, and scan your surroundings. With the exception of the mysterious structure, the field is totally void \nof anything.\n-\n-\n-\n")
    choice5 = input("Do you...\nEXPLORE your surroundings or CONTINUE building a campsite? ")
    if choice5.lower() == "explore":
        print("\nYou decide it would not hurt to take a look around. After a few minutes of walking, you see a huge plume of smoke in the opposite direction of the tower, as well as a large rainstorm. ")
        choice6 = input("Do you...\nTravel to the plume of SMOKE, or stick around your CAMP? ")
        if choice6.lower() == "smoke":
            print("The smoke tower gets larger and larger. You are short on water, so by the time you reach the source, you are close to collapsing. A local farmer burning his crops catches you, and takes you back to civilization.\n\nTHE END")
        elif choice6.lower() == "camp":
            print("You decide the only priority is your survival, so you build yourself a shelter as well as collect some food from some nearby plants. After ten days, someone comes by, assumes you are a mountain man, but hesitantly gives you a ride back to town.\n\nTHE END")
        else:
            print("-\n" + "You die a horrible and slow death for not conforming to the programmers wishes. Better luck next time.")
    elif choice5.lower() == "continue":
        print("While continuing with your campsite, you hear some rustling and talking in the distance.")
        choice7 = input("Do you...\nHIDE in your shelter or MEET the crowd? ")
        if choice7.lower() == "hide":
            print("\nYou duck down into the bushes to hide from the incoming noise. It comes, passes, and you are left alone again. In the end, you wish you would have said something, because those are the last voices you heard.\nTHE END")
        elif choice7.lower() == "meet":
            print("As you rush out to meet the group of wandering people, the first thing you realize is they are not speaking your language. And as you get closer, you find they are not friendly either. Eventually someone finds your body, but with a few limbs missions.\nTHE END")
        else:
            print("-\n" + "You die a horrible and slow death for not conforming to the programmers wishes. Better luck next time.")
    else:
        print("-\n" + "You die a horrible and slow death for not conforming to the programmers wishes. Better luck next time.")


else:
    print("-\n" + "You die a horrible and slow death for not conforming to the programmers wishes. Better luck next time.")

