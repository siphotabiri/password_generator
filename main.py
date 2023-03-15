import random

#Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

""""
random_password = []

letter_count = 1
while letter_count <= nr_letters:
  random_password.append(random.choice(letters))
  letter_count += 1
  
symbol_count = 1
while symbol_count <= nr_symbols:
  random_password.append(random.choice(symbols))
  symbol_count += 1

number_count = 1
while number_count <= nr_numbers:
  random_password.append(random.choice(numbers))
  number_count += 1

random.shuffle(random_password)

final_password = "".join(random_password)
print(f"your random password is: {final_password}")



password = ""
for char in range(1, nr_letters + 1):
  password += random.choice(letters)

for symbol in range(1, nr_symbols + 1):
  password += random.choice(symbols)

for number in range(1, nr_numbers + 1):
  password += random.choice(numbers)
  
print(password)

password = list(password)
random.shuffle(password)
password = ''.join(password)
print(password)

"""

password = []
for char in range(1, nr_letters + 1):
    password.append(random.choice(letters))

for symbol in range(1, nr_symbols + 1):
    password.append(random.choice(symbols))

for number in range(1, nr_numbers + 1):
    password.append(random.choice(numbers))

random.shuffle(password)
password = ''.join(password)
print(password)