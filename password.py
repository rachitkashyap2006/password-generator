import random
import string

print("=== PASSWORD GENERATOR ===")

# Ask user for password length
length = int(input("Enter password length: "))

# Ask user preferences
use_upper = input("Include CAPITAL letters? (y/n): ")
use_lower = input("Include small letters? (y/n): ")
use_digits = input("Include numbers? (y/n): ")
use_symbols = input("Include symbols? (y/n): ")

# Empty string to store characters
characters = ""

if use_upper == 'y':
    characters += string.ascii_uppercase

if use_lower == 'y':
    characters += string.ascii_lowercase

if use_digits == 'y':
    characters += string.digits

if use_symbols == 'y':
    characters += string.punctuation

# Check if user selected at least one option
if characters == "":
    print(" You must select at least one character type!")
else:
    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("\n Your Generated Password is:")
    print(password)
