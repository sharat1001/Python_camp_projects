import random   
import string

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Add small case as well to the alphabet list to strengthen the password
small_letters = [ str(i) for i in string.ascii_lowercase]
letters.extend(small_letters)


print("Welcome to the PyPassword Generator!")
# Mandatory as the password rules required mix of letters, symbols and numbers
nr_letters = int(input("How many letters would you like in your password?\n")) # Adding a condition of having minimum 16 letters atleast in password.

if nr_letters < 16: 
    print("You need to have minimum 16 characters of the password")
    exit()
else:
    nr_symbols = int(input("How many symbols would you like?\n"))
    nr_numbers = int(input("How many numbers would you like?\n"))

password_list = []

for _ in range(0, nr_letters):
    password_list.append(random.choice(letters))
for _ in range(0, nr_symbols):
    password_list.append(random.choice(symbols))
for _ in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

print(''.join(password_list))
