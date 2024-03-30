import random
import string

print("      PASSWORD GENERATOR      ")

lower_latters=int(input("enter the length of the lower case latter:"))
upper_latters=int(input("enter the length of the upper caase latter:")) 
digits=int(input("enter the length of the digits: "))
symbols=int(input("enter the length of the symbols: "))


lower = string.ascii_lowercase
upper = string.ascii_uppercase
digit = string.digits
symbol= string.punctuation

password_list=[]

for i in range (1,lower_latters+1):
    char = random.choice(lower)
    password_list += char

for i in range (1,upper_latters+1):
    char = random.choice(upper)
    password_list += char

for i in range (1,digits+1):
    char = random.choice(digit)
    password_list += char

for i in range (1,symbols+1):
    char = random.choice(symbol)
    password_list += char 

print (password_list)

random.shuffle(password_list)
print(password_list)

password=""

for x in password_list:
    password += x

print(password)

