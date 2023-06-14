import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# print(names)

list_length = len(names)
# print(list_length)

random_integer = random.randint(0, list_length - 1)

print(f"{names[random_integer]} is going to buy the meal today!")

# using choice()
bill_payer = random.choice(names)
print(f"{bill_payer} is going to buy the meal today!")
