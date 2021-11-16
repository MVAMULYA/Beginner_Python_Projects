# !usr/bin/env python3
'''
    Python Script For password generator

'''
import random
import string

small_case = list(string.ascii_lowercase)
upper_case = list(string.ascii_uppercase)
digit = list(string.digits)
characters = list(string.punctuation)

def password_gen(s_n, u_n, d, c):
    password = []
    password.extend(random.sample(small_case, k = s_n))
    password.extend(random.sample(upper_case, k = u_n))
    password.extend(random.sample(digit, k = d))
    password.extend(random.sample(characters, k = c))  
    random.shuffle(password)
    return ''.join(password)

min_len, max_len = map(int, input("enter min and max length of password seperated by space").split())
small = int(input("enter 1-5 num of small case alphabets "))
upper = int(input("enter 1-5 num of upper case alphabets "))
digits = int(input("enter 1-5 num of digits "))
charac = int(input("enter 1-2 num of punctuation characters "))

if min_len <= small + upper + digits + charac <= max_len:
    if 1 <= small <= 5 and 1 <= upper <= 5 and 1 <= digits <= 5 and 1 <= charac <= 2:
        print(password_gen(small, upper, digits, charac))
    else:
        print("invalid input for password requirements")
else:
    print("password lenght insufficient")