print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

first_name = name1.lower()
second_name = name2.lower()

combined_name = first_name + second_name

combined_name.count("t")
combined_name.count("r")
combined_name.count("u")
combined_name.count("e")


combined_name.count("l")
combined_name.count("o")
combined_name.count("v")
combined_name.count("e")

true_combined_name = (
    combined_name.count("t")
    + combined_name.count("r")
    + combined_name.count("u")
    + combined_name.count("e")
)
# print(true_combined_name)

love_combined_name = (
    combined_name.count("l")
    + combined_name.count("o")
    + combined_name.count("v")
    + combined_name.count("e")
)
# print(love_combined_name)

total_score = str(true_combined_name) + str(love_combined_name)
total_score_int = int(total_score)
# print(total_score_int)


if (total_score_int < 10) or (total_score_int > 90):
    print(f"Your score is {total_score_int}, you go together like coke and mentos.")
elif (total_score_int >= 40) and (total_score_int <= 50):
    print(f"Your score is {total_score_int}, you are alright together.")
else:
    print(f"Your score is {total_score_int}.")
