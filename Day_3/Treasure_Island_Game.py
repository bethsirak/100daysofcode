first_cr = input(
    "You're at a cross road. Which way would you like to go? Type 'Left' or 'Right'  "
)

if first_cr.lower() == ("left"):
    print("\nWell done you avoided falling off a cliff \n")

    second_cr = input(
        "You passed your first test... now its time to pick again!\n\nYou're at a lake on the island but need to cross the lake to find the treasure.\n\nWould you like to wait for a boat or swim across? Type 'Wait' or 'Swim' "
    )

    if second_cr.lower() == "wait":
        print("\nYou've arrived at the island unharmed \n")

        final_cr = input(
            "There is a house with 3 doors: Blue, Pink and Grey. Pick a colour! "
        )
        if final_cr.lower() == "pink":
            print("\nYou Win!")
        else:
            print("Game Over")

    elif second_cr.lower() == ("swim"):
        print("\nYou've been eaten by sharks - Game Over")

elif first_cr.lower() == ("right"):
    print("RIP you fell off a cliff and broke all your bones... Game Over")

else:
    print(
        "Invalid option... You took too long and now you've been eaten by a bear - Game Over"
    )

    # To improve - create a loop which will allow you to rest game once game is over
