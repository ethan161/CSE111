running_names = False
friend_list = []
while not running_names:
    friend_list.append(input("Type the name of a friend: "))
    if "end".lower() in friend_list:
        running_names = True

print("Your friends are:\n")
for friend in friend_list[:-1]:
    print(friend)