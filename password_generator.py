#dictionary
import string
import random


from art import logo
print(logo)


capital_alphabet= list(string.ascii_uppercase)
alphabet_list = list(string.ascii_lowercase)
symbol = list(string.punctuation)
numbers_list = list(string.digits)

nr_capital = int(input("How many capital letter? \n"))
nr_lowercase = int(input("How manylowercase letter? \n "))
nr_symbol = int(input("how many symbol ? \n"))
nr_number = int(input("how many number?\n"))

password = []
for a in range(1, nr_capital + 1):
  password += random.choice(capital_alphabet)

for b in range (1, nr_lowercase + 1):
  password += random.choice(alphabet_list)

for c in range(1, nr_symbol + 1):
  password += random.choice(symbol)

for d in range(1, nr_number + 1):
  password += random.choice(numbers_list)

random.shuffle(password)
new_password = ""
for all in password:
  new_password += all
  
print(f"Your final password is {new_password}")
print(f"DON'T GIVE YOUR USERNAME AND PASSWORD TO ANYONE")


