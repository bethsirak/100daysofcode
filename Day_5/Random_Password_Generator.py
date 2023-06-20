#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbols, 2 number = JduE&!91

'''random_index_letter = random.randint(0,25)
print(letters[random_index_letter])

random_index_number = random.randint(0,9)
print(numbers[random_index_number])

random_index_symbol = random.randint(0,8)
print(symbols[random_index_symbol]) '''

password = ""
for char in range (1, nr_letters +1):
  random_index_letter = random.randint(0,25)
  password += letters[random_index_letter]

for symbol in range (1, nr_symbols +1):
  random_index_symbol = random.randint(0,8)
  password += symbols[random_index_symbol]

for num in range (1, nr_numbers +1):
  random_index_number = random.randint(0,9)
  password += numbers[random_index_number]

p_shuffled = ''.join(random.sample(password, len(password)))
print(f"Your new password is {p_shuffled}")


  


