import random

letters = ['a','b','c','d','f','g','h','i','j','k','l','m','n','o','p','q','r','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','&','*','(',')','-','_','+']
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in you password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many number would you like?\n"))

password_list = []
for l in range(nr_letters):
    password_list.append(random.choice(letters))

for l in range(nr_symbols):
    password_list.append(random.choice(symbols))

for l in range(nr_numbers):
    password_list.append(random.choice(numbers))


# print(password_list)
random.shuffle(password_list)
# print(password_list)

password = ""
for i in password_list:
    password += i

print(f"Your password is : {password}")