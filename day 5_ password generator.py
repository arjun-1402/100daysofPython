import random
import string

print("Welcome to the Password Generator!")

# User inputs for number of letters, symbols, and numbers in the password
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

# Lists for characters
letters = list(string.ascii_letters)  # Uppercase and lowercase letters
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = list(string.digits)         # Digits 0-9

# Generate random letters, symbols, and numbers
password_letters = random.choices(letters, k=num_letters)
password_symbols = random.choices(symbols, k=num_symbols)
password_numbers = random.choices(numbers, k=num_numbers)

# Combine all parts into a single list
password_list = password_letters + password_symbols + password_numbers

# Shuffle the password characters to randomize the order
random.shuffle(password_list)

# Convert the list into a string
password = ''.join(password_list)

print(f"Your generated password is: {password}")
